# FastAPI Task Executor with Docker

This project is a FastAPI-based application that allows you to dynamically execute Python code inside Docker containers. The system dynamically allocates CPU and memory resources based on task requirements and returns the execution result.

## Installation

**Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/fastapi-task-executor.git
   cd fastapi-task-executor

docker build -t fastapi-app .
docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock fastapi-app

API Endpoints
POST /execute

Executes the given Python code inside a Docker container.
Request Body

{
  "task_type": "python",
  "code": "print('Hello, World!')",
  "resources": {
    "cpu": "1",
    "gpu": "0",
    "ram": "512m",
    "storage": "1G"
  }
}
Example Request
curl -X 'POST' \
  'http://localhost:8000/execute' \
  -H 'Content-Type: application/json' \
  -d '{
    "task_type": "python",
    "code": "print(\"Hello, Docker!\")",
    "resources": {
      "cpu": "1",
      "gpu": "0",
      "ram": "512m",
      "storage": "1G"
    }
  }'

