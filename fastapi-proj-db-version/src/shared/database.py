from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

engine = create_engine("sqlite:///./data/development.db")
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def db_init():
    if not os.path.exists("./data"):
        os.makedirs("./data/")
    Base.metadata.create_all(engine)