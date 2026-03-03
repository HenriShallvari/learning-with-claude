from fastapi import APIRouter, HTTPException, Response
from src.schemas.task_schemas import TaskCreate, TaskRead, TaskUpdate
from src.services.task_service import TaskService

router = APIRouter()
service = TaskService()


@router.get("/tasks")
def get_tasks(completato: bool = False) -> list[TaskRead]:

    try:
        tasks = service.get_all()

        if completato:
            tasks = [t for t in tasks if t.completato]
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="There was a problem retrieving all tasks.")

    return tasks

@router.get("/tasks/{id}")
def get_by_id(id: int):

    try:
        task = service.get_by_id(id)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="There was a problem retrieving the requested task.")
    
    if not task:
        raise HTTPException(status_code=404)

    return task    

@router.post("/tasks")
def create_task(body: TaskCreate):

    try:
        service.create(body)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="There was a problem creating the task.")
    
    return body

@router.put("/tasks/{id}")
def update_task(id: int, body: TaskUpdate):

    try:
        service.update(id=id, task_to_up=body)
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=404, detail=e)
    except Exception as e: 
        print(e)
        raise HTTPException(status_code=500, detail="There was a problem updating the task.")
    
    return body

@router.delete("/tasks/{id}")
def delete_task(id: int):
    
    try:
        service.delete(id=id)
    except Exception as e: 
        print(e)
        raise HTTPException(status_code=500, detail="There was a problem while deleting the task.")
    
    return Response(status_code=204)