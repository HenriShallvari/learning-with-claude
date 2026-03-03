import json
from models.task import Task, TaskPut


class DBConnector:
    __json_path: str

    def __init__(self):
        self.__json_path = "./data/tasks.json"

    def get_data_path(self):
        return self.__json_path
    
    def get_tasks(self) -> list[Task]:
        with open(self.__json_path, "r") as t:
            json_file_data = json.load(t)

        tasks = self.json_to_tasklist(json_file_data)

        return tasks
    
    def add_task(self, task: Task):
        tasks = self.get_tasks()
        
        existing_task = [t for t in tasks if t.id == task.id]

        if len(existing_task) > 0:
            raise IndexError(f"Element with id {task.id} already exists.")

        tasks.append(task)

        self.write_to_json(tasks)

    def edit_task(self, id: int, task_put: TaskPut):
        tasks = self.get_tasks()

        for task in tasks:
            if task.id == id:
                if task_put.titolo is not None:
                    task.titolo = task_put.titolo
                if task_put.descrizione is not None:
                    task.descrizione = task_put.descrizione
                if task_put.completato is not None:
                    task.completato = task_put.completato
                break

        self.write_to_json(tasks)
    
    def delete_task(self, id: int):
        tasks = self.get_tasks()
        
        final_tasks = [t for t in tasks if t.id != id]

        with open(self.__json_path, "w") as writer:
            writer.write(self.tasklist_to_json(final_tasks))

    def write_to_json(self, tasks: list[Task]):
        with open(self.__json_path, "w") as writer:
            writer.write(self.tasklist_to_json(tasks))


    # converters
    def json_to_tasklist(self, file_data) -> list[Task]:

        task_list: list[Task] = [
            Task(id= line["id"], titolo=line["titolo"], descrizione=line["descrizione"], completato=line["completato"]) 
            for line in file_data
        ]

        return task_list
    
    def tasklist_to_json(self, task_list: list[Task]) -> str:
        return json.dumps(
            [
                {
                    'id': task.id,
                    'titolo': task.titolo,
                    'descrizione': task.descrizione,
                    'completato': task.completato
                } 
                for task in task_list
            ]
        )
