from fastapi import APIRouter, HTTPException, Depends
from app.models import Job
from app.database import get_db
from app.db_models import JobDB
from sqlalchemy.orm import Session




router = APIRouter()

jobs = []


#--------------------------------
#  Create Job
#--------------------------------
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



#--------------------------------
#  Get all jobs
#--------------------------------

@router.get('/jobs')
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(JobDB).all()
    return jobs 



#--------------------------------
#  Get Job By ID
#--------------------------------

@router.get('/jobs/{id}')
def get_job_by_id(id : int, db: Session=Depends(get_db)):

    job = db.query(JobDB).filter(JobDB.id == id).first()

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")

    return job
        

#--------------------------------
#  Update Job By ID
#--------------------------------

@router.put('/jobs/{id}')
def update_job(id: int, updated_job: Job, db: Session = Depends(get_db)):

    job = db.query(JobDB).filter(JobDB.id == id).first()

    if job is None:
        raise HTTPException(status_code=404, detail='Job not found')


    job.title = updated_job.title
    job.company = updated_job.company
    job.location = updated_job.location
    job.description = updated_job.description
    job.salary = updated_job.salary
    job.source = updated_job.source
    job.employment_type = updated_job.employment_type

    db.commit()
    db.refresh(job)

    
    return {
        "message": "Job updated successfully",
        "job": job
    }


#--------------------------------
#  Delete Job By ID
#--------------------------------

@router.delete('/jobs/{id}')
def delete_job(id : int, db: Session= Depends(get_db)):
    
    job = db.query(JobDB).filter(JobDB.id == id).first()

    if job is None:
        raise HTTPException(status_code=404, detail='Job not found')

    db.delete(job)
    db.commit()

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