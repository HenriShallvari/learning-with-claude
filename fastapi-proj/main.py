# main.py
from fastapi import FastAPI

# importiamo tutti i nostri routers
from routers import tasks

app = FastAPI()

app.include_router(tasks.router)