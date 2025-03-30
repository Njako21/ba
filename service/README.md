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

##  Prerequisites

* Python 3.8 or higher
* `pip` (Python package installer)
* `git` (for cloning the repository)

## 🚀 Setup and Installation

Follow these steps to set up and run the project locally.

**1. Clone the Repository**

```bash
git clone <your-repository-url> # Replace with your repo URL
cd <repository-directory-name> # Replace with the name of the cloned directory