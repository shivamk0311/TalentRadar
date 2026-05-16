from fastapi import APIRouter, HTTPException, Depends
from app.schemas.candidate import CandidateCreate, CandidateResponse
from sqlalchemy.orm import Session
from app.database import get_db

from app.services.candidate_service import create_candidate_service, update_candidate_service

from app.repositories.candidate_repository import (
    get_all_candidates,
    get_candidate_by_id,
    update_candidate,
    delete_candidate
)

router = APIRouter()

@router.post('/candidates', response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session=Depends(get_db)):
    return create_candidate_service(db, candidate)


@router.get('/candidates', response_model = list[CandidateResponse])
def get_candidates(db : Session=Depends(get_db)):
    return get_all_candidates(db)


@router.get('/candidates/{id}', response_model=CandidateResponse)
def get_single_candidate(id: int, db: Session=Depends(get_db)):
    candidate = get_candidate_by_id(db, id)

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate

@router.put("/candidates/{candidate_id}", response_model=CandidateResponse)
def update_existing_candidate(
    candidate_id: int,
    updated_candidate: CandidateCreate,
    db: Session = Depends(get_db)
):
    candidate = update_candidate_service(db, candidate_id, updated_candidate)

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate

@router.delete("/candidates/{candidate_id}")
def remove_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    candidate = delete_candidate(db, candidate_id)

    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return {
        "message": "Candidate deleted successfully"
    }