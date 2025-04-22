# Chat-app-backend

A real-time chat backend built with FastAPI and WebSockets.

## 🚀 Features

- **Real-time communication** using WebSockets
- **FastAPI** for RESTful API endpoints
- **Asynchronous** handling for scalability
- **User authentication** and session management

## 🛠️ Installation

**Clone the repository:**
```bash
git clone https://github.com/adeltraboulsi/Chat-app-backend.git
cd Chat-app-backend
```
**Create and activate a virtual environment:**

On macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```
On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

**Install dependencies:**

After activating the virtual environment, install the dependencies:

```bash
pip install -r requirements.txt
```
## ▶️ Usage

**Run the FastAPI server**

To start the development server with hot reload:

```bash
uvicorn main:app --reload
```
**View API documentation**

Once the server is running, open your browser and go to:

```bash
http://localhost:8000/docs
```
## 📚 API Endpoints

| Method | Endpoint        | Description                         |
|--------|-----------------|-------------------------------------|
| GET    | `/`             | Health check                        |
| POST   | `/login`        | User login                          |
| POST   | `/register`     | User registration                   |
| GET    | `/ws/{room_id}` | WebSocket endpoint for chat rooms   |


## 🤝 Contributing

### Step 1: Fork the repository  
Click the **Fork** button on the top-right of the GitHub page.

### Step 2: Create a new branch

```bash
git checkout -b your-feature
```
### Step 3: Make your changes and commit them

```bash
git add .
git commit -m "Add your feature"
```
### Step 4: Push to your fork and submit a pull request

```bash
git push origin your-feature
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.













