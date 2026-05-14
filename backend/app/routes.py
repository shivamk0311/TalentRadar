from fastapi import APIRouter, HTTPException, Depends
from app.models import Job
from app.database import get_db
from app.db_models import JobDB
from sqlalchemy.orm import Session




router = APIRouter()

jobs = []

@router.post('/jobs')
def create_job(job : Job, db : Session = Depends(get_db)):
    new_job = JobDB(
        title = job.title,
        company = job.company,
        location = job.location,
        description = job.description,
        salary = job.salary,
        source = job.source,
        employment_type = job.employment_type
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    
    return {
        "message": "Job created successfully",
        "job" : new_job
    }

@router.get('/jobs')
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(JobDB).all()
    return jobs 

@router.get('/jobs/{id}')
def get_job_by_id(id : int, db: Session=Depends(get_db)):

    job = db.query(JobDB).filter(JobDB.id == id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")

    return job
        

@router.put('/jobs/{id}')
def update_job(id: int, updated_job: Job):

    for index, job in enumerate(jobs):
        if job['id'] == id:
            updated_job_data = updated_job.model_dump()
            updated_job_data['id'] = id 
            jobs[index] = updated_job_data
            return {
                "message": "Job updated successfully",
                "deleted_job": updated_job_data
            }
    
    raise HTTPException(status_code=404, detail='Job not found')

@router.delete('/jobs/{id}')
def delete_job(id : int):
    
    for job in jobs:
        if job['id'] == id:
            jobs.remove(job)
            return {
                "message": "Job deleted successfully",
                "deleted_job": job
            }
    
    raise HTTPException(status_code=404, detail='Job not found')

@router.get('/jobs/search/{skill}')
def search_job(skill):
    matched_jobs = []
    for job in jobs:
        for job_skill in job["skills"]:
            if job_skill.lower() == skill.lower():
                matched_jobs.append(job)
            
    return matched_jobs
    

@router.get('/health')
def health_check():
    return {'status': 'ok'}