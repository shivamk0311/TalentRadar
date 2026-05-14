from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    description: str
    salary: str | None = None
    skills: list[str]
    source: str | None = None
    employment_type: str | None = None