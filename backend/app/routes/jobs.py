from app.schemas.job import JobCreate, JobResponse
from app.models.job import JobDB
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.repositories.job_repository import (
    create_job,
    get_all_jobs,
    get_job_by_id,
    delete_job,
    update_job
)

router = APIRouter()

jobs = []


#--------------------------------
#  Create Job
#--------------------------------
@router.post('/jobs', response_model = JobResponse)
def create_job(job : JobCreate, db : Session = Depends(get_db)):

    return create_job(db, job)



#--------------------------------
#  Get all jobs
#--------------------------------

@router.get('/jobs', response_model = list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):

    return get_all_jobs(db)



#--------------------------------
#  Get Job By ID
#--------------------------------

@router.get('/jobs/{id}', response_model = JobResponse)
def get_requested_job(id : int, db: Session=Depends(get_db)):

    job = get_job_by_id(db, id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")

    return job
        

#--------------------------------
#  Update Job By ID
#--------------------------------

@router.put('/jobs/{id}', response_model = JobResponse)
def update_existing_job(id: int, updated_job: JobCreate, db: Session = Depends(get_db)):

    job = update_job(db, id, updated_job)

    if job is None:
        raise HTTPException(status_code=404, detail='Job not found')
    
    return {
        "message": "Job updated successfully",
        "job": job
    }


#--------------------------------
#  Delete Job By ID
#--------------------------------

@router.delete('/jobs/{id}')
def delete_job_by_id(id : int, db: Session= Depends(get_db)):
    
    job = delete_job(db, id)

    if job is None:
        raise HTTPException(status_code=404, detail='Job not found')

    return {
        "message": "Job deleted successfully",
    }
    
#--------------------------------
#  Search Jobs By Skills
#--------------------------------

@router.get('/jobs/search/{skill}')
def search_job(skill):
    matched_jobs = []
    for job in jobs:
        for job_skill in job["skills"]:
            if job_skill.lower() == skill.lower():
                matched_jobs.append(job)
            
    return matched_jobs
    

#--------------------------------
#  API Endpoint Health Check
#--------------------------------
@router.get('/health')
def health_check():
    return {'status': 'ok'}