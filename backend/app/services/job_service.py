from app.schemas.job import JobCreate
from app.repositories.job_repository import create_job

def normalize_skills(skills: list[str]):
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
        "postgresql": "PostgreSQL"
    }
    cleaned_skills = []

    for skill in skills:
        updated_skill = skill.strip().lower()

        if updated_skill in acronym_map:
            updated_skill = acronym_map[updated_skill]
        else:
            updated_skill = updated_skill.title()
        cleaned_skills.append(updated_skill)
    
    return cleaned_skills

def create_job_service(db, job: JobCreate):
    job.skills = normalize_skills(job.skills)

    return create_job(db, job)