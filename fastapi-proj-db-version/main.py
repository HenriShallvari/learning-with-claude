from fastapi import FastAPI
from src.routers import tasks_router
from src.shared import database as db_manager

db_manager.db_init()

app = FastAPI()

app.include_router(tasks_router.router)