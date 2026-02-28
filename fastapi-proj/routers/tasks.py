from fastapi import APIRouter, HTTPException
from db.dbconnector import DBConnector
from models.task import Task

router = APIRouter()
db = DBConnector()


@router.get("/tasks")
def get_all_tasks(completato: bool = False) -> list[Task]:
    tasks: list[Task] = db.get_tasks()

    filtered_tasks: list[Task] = [task for task in tasks if task.completato] if completato else tasks

    return filtered_tasks

@router.get("/tasks/{id}")
def get_task(id: int) -> Task:
    tasks: list[Task] = db.get_tasks()

    # here it works because id is an int, in the real world it might not
    # depending on the type of id.
    if id > len(tasks) or id < 1:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found.")

    final_task = [task for task in tasks if task.id == id]

    if len(final_task) == 0:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found.")

    return final_task[1]

@router.post("/tasks")
def add_new_task(task: Task):
    try:
        db.add_task(task)
    except IndexError as e:
        raise HTTPException(status_code=400, detail=e)
    except Exception as e:
        raise HTTPException(status_code=500)
    
@router.put("/tasks/{id}")
def edit_task(id: int, titolo: str = "", descrizione: str = "", completato: bool = False):
    try:
        db.edit_task(id, titolo, descrizione, completato)
    except Exception as e:
        raise HTTPException(status_code=500)

@router.delete("/tasks/{id}")
def delete_task(id: int):
    db.delete_task(id)