from pydantic import BaseModel

class Job(BaseModel):
    title: str 
    company: str 
    location: str 
    description: str 
    salary: str 
    skills: list[str]
    source: str 
    employment_type: str