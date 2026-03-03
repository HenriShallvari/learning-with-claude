from pydantic import BaseModel, field_validator

class TaskBase(BaseModel):
    titolo: str | None = None
    descrizione: str | None = None
    completato: bool | None = None
    

class TaskCreate(TaskBase):
    completato: bool | None = False
    
    @field_validator("titolo")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if not v or v.strip() == "":
            raise ValueError("Titolo deve avere un valore.")
        return v


class TaskRead(TaskCreate):
    id: int
    pass

class TaskUpdate(TaskBase):
    pass