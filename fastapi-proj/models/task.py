from pydantic import BaseModel, field_validator

class TaskBase(BaseModel):
    titolo: str | None = None
    descrizione: str | None = None
    completato: bool | None = None
    

class Task(TaskBase):
    id: int
    completato: bool | None = False

    # in a real world scenario, this shit would be auto-generated
    # but I do not know how to do that right now, so I'll let someone else
    # take responsibility of providing an ID.

    # Also, we make some properties mandatory here
    @field_validator("id")
    @classmethod
    def positive_id(cls, v: int) -> int:
        if v < 0:
            raise ValueError("ID deve essere positivo.")
        return v
    
    @field_validator("titolo")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("Titolo deve avere un valore.")
        return v


class TaskPut(TaskBase):
    pass