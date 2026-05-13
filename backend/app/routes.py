from fastapi import APIRouter, HTTPException
from app.models import Job


router = APIRouter()

jobs = []

@router.post('/jobs')
def create_job(job : Job):
    job_data = job.model_dump()
    job_data['id'] = len(jobs) + 1
    jobs.append(job_data)
    return {
        "message": "Job created successfully",
        "job" : job_data
    }

@router.get('/jobs')
def get_jobs():
    return jobs 

@router.get('/jobs/{id}')
def get_job_by_id(id : int):
    
    for job in jobs:
        if job['id'] == id:
            return job
        
    raise HTTPException(status_code=404, detail="Job not found.")

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