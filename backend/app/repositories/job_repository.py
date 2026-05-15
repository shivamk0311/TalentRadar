from sqlalchemy.orm import Session
from app.models.job import JobDB
from app.schemas.job import JobCreate


def create_job(db: Session, job: JobCreate):
    new_job = JobDB(
        title=job.title,
        company=job.company,
        location=job.location,
        description=job.description,
        salary=job.salary,
        skills=job.skills,
        source=job.source,
        employment_type=job.employment_type
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


def get_all_jobs(db: Session):
    return db.query(JobDB).all()


def get_job_by_id(db: Session, job_id: int):
    return db.query(JobDB).filter(JobDB.id == job_id).first()


def delete_job(db: Session, job_id: int):
    job = get_job_by_id(db, job_id)

    if job:
        db.delete(job)
        db.commit()

    return job

def update_job(db: Session, job_id: int, updated_job: JobCreate):
    job = get_job_by_id(db, job_id)

    if job is None:
        return None

    job.title = updated_job.title
    job.company = updated_job.company
    job.location = updated_job.location
    job.description = updated_job.description
    job.salary = updated_job.salary
    job.skills = updated_job.skills
    job.source = updated_job.source
    job.employment_type = updated_job.employment_type

    db.commit()
    db.refresh(job)

    return job

def search_job_by_skill(db: Session, skill: str):
    return db.query(JobDB).filter(JobDB.skills.any(skill)).all()