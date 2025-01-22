from fastapi import FastAPI

from api.v1.api import api_router
from core.configs import settings

app = FastAPI(
    title="to-do list utilizando fastAPI",
    description="API que simula uma lista de tarefas.",
    version="0.0.1",
)

app.include_router(api_router, prefix=settings.API_V1_STR)
