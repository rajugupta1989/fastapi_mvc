# FastAPI MVC

FastAPI project following the MVC (Model-View-Controller) architecture pattern. It includes an endpoint for processing data with request and response validation using Pydantic models, and uses Python's multiprocessing for performing addition on input lists of integers.

## Project Structure

fastapi_mvc/
|- app/
| |- init.py
| |- main.py
| |- models/
| | |- init.py
| | |- models.py
| |- controllers/
| | |- init.py
| | |- controller.py
| |- views/
| | |- init.py
| | |- view.py
| |- utils/
| | |- init.py
| | |- utils.py
| |- logs/
| | |- init.py
| | |- logger.py
|- tests/
| |- init.py
| |- test_app.py
|- requirements.txt
|-README.md



## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic
- Pytest

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd fastapi_mvc
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn app.main:app --reload

The application will be available at http://127.0.0.1:8000.

API Endpoint
Process Data
URL: /process

Method: POST

Request Body:

{
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
}


Response:
{
    "batchid": "id0101",
    "response": [3, 7],
    "status": "complete",
    "started_at": "<timestamp>",
    "completed_at": "<timestamp>"
}

