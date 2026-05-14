from fastapi import FastAPI
from app.routes.jobs import router as jobs_router
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = 'TalentRadar API',
    description = 'Backend API for job ingestion and candidate job matching',
    version = '0.1.0'
)

app.include_router(jobs_router)

