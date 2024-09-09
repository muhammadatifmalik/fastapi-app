from fastapi import FastAPI
from pydantic import BaseModel
from task_executer import execute_task

app = FastAPI()

class ResourceModel(BaseModel):
    cpu: str
    gpu: str
    ram: str
    storage: str

class TaskModel(BaseModel):
    task_type: str
    code: str
    resources: ResourceModel

@app.post("/execute")
async def execute_code(task: TaskModel):
    result = execute_task(task)
    return {"result": result}
