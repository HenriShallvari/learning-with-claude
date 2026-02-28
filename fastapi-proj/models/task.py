from pydantic import BaseModel, field_validator

class TaskBase(BaseModel):
    titolo: str
    descrizione: str
    completato: bool = False
    
    @field_validator("titolo")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if v.strip() == "" or v == None:
            raise ValueError("Titolo deve avere un valore.")
        return v
    
    @field_validator("descrizione")
    @classmethod
    def description_not_empty(cls, v: str) -> str:
        if v.strip() == "" or v == None:
            raise ValueError("Descrizione deve avere un valore.")
        return v

class Task(TaskBase):
    id: int

    # in a real world scenario, this shit would be auto-generated
    # but I do not know how to do that right now, so I'll let someone else
    # take responsibility of providing an ID.
    @field_validator("id")
    @classmethod
    def positive_id(cls, v: int) -> int:
        if v < 0:
            raise ValueError("ID deve essere positivo.")
        return v

class TaskPut(TaskBase):
    
    ...