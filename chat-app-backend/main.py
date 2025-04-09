from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from connection_manager import ConnectionManager
from googletrans import Translator

# Initialize FastAPI app and connection manager
app = FastAPI()
manager = ConnectionManager()

# Initialize Google Translate API
translator = Translator()
user_languages = {}

def translate_message(text: str, target_lang: str = "fr") -> str:
    """
    Translate the given text to the target language using Google Translate.
    :param text: The message text to translate
    :param target_lang: The language to translate to (default is French 'fr')
    :return: The translated message
    """
    try:
        # Translate the text
        result = translator.translate(text, dest=target_lang)
        return result.text
    except Exception as e:
        # In case of failure, return the error message
        return f"[Error: {str(e)}]"

@app.websocket("/ws/{username}")
async def websocket_chat(websocket: WebSocket, username: str):
    await manager.connect(username, websocket)
    
    # Default to English ("en") if no language is set
    user_language = "en"
    
    try:
        while True:
            # Receive message data from WebSocket client
            data = await websocket.receive_json()
            
            message = data["message"]
            recipient = data["recipient"]
            
            # If language is provided, store it for the user
            if "language" in data:
                user_language = data["language"]
                user_languages[username] = user_language  # Save to memory
                
            # If no language is specified, use the stored one
            elif username in user_languages:
                user_language = user_languages[username]
            
            # Translate the message
            translated = translate_message(message, user_language)
            
            # Combine the original and translated message
            combined = f"{username}: {message}\n(Translated: {translated})"
            
            # Send the combined message to the recipient
            await manager.send_message(recipient, combined)
    
    except WebSocketDisconnect:
        await manager.disconnect(username)

