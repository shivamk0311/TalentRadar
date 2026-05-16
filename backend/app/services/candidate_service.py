from app.repositories.candidate_repository import create_candidate, update_candidate
from app.schemas.candidate import CandidateCreate

def normalize_list(values):
    if values is None:
        return None

    acronym_map = {
        "sql": "SQL",
        "aws": "AWS",
        "api": "API",
        "ai": "AI",
        "ml": "ML",
        "llm": "LLM",
        "rag": "RAG",
        "fastapi": "FastAPI",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "postgresql": "PostgreSQL",
        "react": "React",
        "python": "Python",
        ".net": ".NET",
        "ai engineer": "AI Engineer"
    }

    cleaned_values = []

    for value in values:
        cleaned_value = value.strip().lower()

        if cleaned_value in acronym_map:
            cleaned_values.append(acronym_map[cleaned_value])
        else:
            cleaned_values.append(cleaned_value.title())

    return cleaned_values


def normalize_candidate(candidate: CandidateCreate) -> CandidateCreate:
    candidate.skills = normalize_list(candidate.skills)
    candidate.target_roles = normalize_list(candidate.target_roles)

    return candidate


def create_candidate_service(db, candidate: CandidateCreate):
    candidate = normalize_candidate(candidate)
    return create_candidate(db, candidate)


def update_candidate_service(db, candidate_id: int, updated_candidate: CandidateCreate):
    updated_candidate = normalize_candidate(updated_candidate)
    return update_candidate(db, candidate_id, updated_candidate)