from sqlalchemy.orm import Mapped, mapped_column
from src.shared.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titolo: Mapped[str] = mapped_column(nullable=False)
    descrizione: Mapped[str] = mapped_column(nullable=False)
    completato: Mapped[bool]  = mapped_column(default=False)