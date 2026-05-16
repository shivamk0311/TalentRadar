from sqlalchemy.orm import Session
from app.models.candidate import CandidateDB
from app.schemas.candidate import CandidateCreate

def create_candidate(db: Session, candidate: CandidateDB):
    new_candidate = CandidateDB(
        name=candidate.name,
        email=candidate.email,
        education=candidate.education,
        experience=candidate.experience,
        skills=candidate.skills,
        target_roles=candidate.target_roles
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate

def get_all_candidates(db: Session):
    return db.query(CandidateDB).all()

def get_candidate_by_id(db: Session,  id: int):
    return db.query(CandidateDB).filter(CandidateDB.id == id).first()

def delete_candidate(db: Session, id: int):
    candidate = get_candidate_by_id(db,id)

    if candidate:
        db.delete(candidate)
        db.commit()

    return candidate

def update_candidate(db: Session, id:int, updated_candidate):
    candidate = get_candidate_by_id(db, id)

    if candidate is None:
        return None 
    
    candidate.name = updated_candidate.name
    candidate.email = updated_candidate.email
    candidate.education = updated_candidate.education
    candidate.experience = updated_candidate.experience
    candidate.skills = updated_candidate.skills
    candidate.target_roles = updated_candidate.target_roles

    db.commit()
    db.refresh(candidate)

    return candidate

    