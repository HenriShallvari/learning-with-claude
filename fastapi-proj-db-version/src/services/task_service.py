from src.models.task import Task
from src.schemas.task_schemas import TaskCreate, TaskRead, TaskUpdate
from src.shared.database import SessionLocal

class TaskService():

    def get_by_id(self, id: int | None = None) -> TaskRead | None:
        db = SessionLocal()
        task: TaskRead | None = None

        try:
            query = db.query(Task).filter(Task.id == id).first()

            if query:
                task = TaskRead(
                    id = int(query.id), 
                    titolo = str(query.titolo), 
                    descrizione = str(query.descrizione), 
                    completato = bool(query.completato)
                )
        except Exception as e:
            raise
        finally:
            db.close()

        return task
    
    def get_all(self) -> list[TaskRead]:
        db = SessionLocal()

        try:
            query = db.query(Task).all()
            resultset = [
                TaskRead(
                    id = line.id, 
                    titolo = line.titolo, 
                    descrizione = line.descrizione, 
                    completato = line.completato
                ) 
                for line in query
            ]
        except:
            raise
        finally:
            db.close()

        return resultset
    
    def create(self, task_in: TaskCreate):
        db = SessionLocal()

        try:
            task: Task = Task(**task_in.model_dump())
            db.add(task)

            db.commit()
        except:
            db.rollback()
            raise
        finally:
            db.close()

    def update(self, id: int, task_to_up: TaskUpdate):
        db = SessionLocal()
        try:
            task = db.query(Task).filter(Task.id == id).first()
            
            if task is None:
                raise ValueError(f"Task with id {id} not found.")
            
            if task_to_up.titolo is not None:
                task.titolo = task_to_up.titolo
            if task_to_up.descrizione is not None:
                task.descrizione = task_to_up.descrizione
            if task_to_up.completato is not None:
                task.completato = task_to_up.completato

            db.commit()
            db.refresh(task)
            return task

        except:
            db.rollback()
            raise
        finally:
            db.close()

    def delete(
        self, 
        id: int
    ):
        db = SessionLocal()

        try:
            db.query(Task).filter(Task.id == id).delete()
            db.commit()
        except:
            db.rollback()
            raise
        finally:
            db.close()