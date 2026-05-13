from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title = 'TalentRadar API',
    description = 'Backend API for job ingestion and candidate job matching',
    version = '0.1.0'
)

app.include_router(router)

