# FastAPI Pub/Sub Example with REST and Streaming

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/) [![Loguru](https://img.shields.io/badge/Logging-Loguru-success.svg)](https://github.com/Delgan/loguru)

This project demonstrates a robust FastAPI application implementing a Publish/Subscribe (Pub/Sub) pattern using Server-Sent Events (SSE) for real-time updates. It also includes standard REST endpoints, asynchronous operations, configuration via environment variables, and advanced logging with daily rotation and automatic retention using Loguru.

## ✨ Features

* **FastAPI Framework**: Modern, high-performance web framework for building APIs.
* **REST Endpoints**: Standard `GET` (`/api/get/...`) and `POST` (`/api/post`) endpoints.
* **Pub/Sub Pattern**:
    * Clients can subscribe to real-time updates via an SSE streaming endpoint (`/api/stream`).
    * Messages can be published via a POST request (e.g., `/api/post`), broadcasting to all subscribers.
* **Server-Sent Events (SSE)**: Efficient server-to-client communication for streaming updates.
* **Asynchronous**: Leverages Python's `async`/`await` for non-blocking I/O.
* **Environment Configuration**: Uses `.env` files and `pydantic-settings` for easy and secure configuration.
* **Advanced Logging**: Powered by `Loguru` with:
    * Console and File logging.
    * Date-based filenames (e.g., `logs/YYYY-MM-DD.log`).
    * Automatic daily rotation (`00:00`).
    * Configurable retention period (automatic deletion of old logs).
    * Asynchronous logging for better performance.
* **CORS Middleware**: Configured to allow requests from specified origins.
* **Structured Code**: Organized into modules for configuration, pub/sub logic, routers, and logging.

## 🛠 Prerequisites

* Python 3.8 or higher
* `pip` (Python package installer)
* `git` (for cloning the repository)

## 🚀 Setup and Installation

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone <your-repository-url> # Replace with your repo URL
cd <repository-directory-name> # Replace with the name of the cloned directory
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r service/requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env-example` file to `.env` and modify it as needed:

```bash
cp service/.env-example service/.env
```

### 5. Run the Application

Start the FastAPI application using `uvicorn`:

```bash
python service/run.py
```

The application will be available at `http://localhost:8000`.

## 📖 Usage

### REST Endpoints

* **GET** `/api/get/hello/{name}`: Returns a greeting message.
* **GET** `/api/get/data`: Fetches sample data.
* **POST** `/api/post`: Creates an item and notifies subscribers.

### Streaming Endpoint

* **GET** `/api/stream`: Subscribes to real-time updates using Server-Sent Events (SSE).

### Root Endpoint

* **GET** `/`: Basic health check or welcome message.

## 🧪 Testing

You can test the endpoints using tools like [Postman](https://www.postman.com/) or `curl`. For example:

```bash
curl http://localhost:8000/api/get/hello/World
```

## 📂 Project Structure

```
service/
├── run.py                 # Entry point for running the application
├── requirements.txt       # Python dependencies
├── .env-example           # Example environment variables
├── src/
│   ├── main.py            # FastAPI application setup
│   ├── config.py          # Configuration using pydantic-settings
│   ├── logger_config.py   # Loguru logger configuration
│   ├── pubsub.py          # Pub/Sub manager for real-time updates
│   ├── routers/
│   │   ├── rest_endpoints.py  # REST API endpoints
│   │   ├── stream_endpoints.py # Streaming API endpoints
│   │   └── __init__.py    # Router module initialization
│   └── __init__.py        # Source module initialization
└── logs/                  # Directory for log files (auto-created)
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.