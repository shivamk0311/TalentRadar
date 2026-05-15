from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    description: str
    salary: str | None = None
    skills: list[str] | None = None
    source: str | None = None
    employment_type: str | None = None

class JobResponse(BaseModel):
    id : int
    title: str
    company: str
    location: str
    description: str
    salary: str | None = None
    skills: list[str] | None = None 
    source: str | None = None
    employment_type: str | None = None

    class Config:
        from_attributes = True