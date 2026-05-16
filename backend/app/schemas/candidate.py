from pydantic import BaseModel, EmailStr


class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    education: str | None = None
    experience: str | None = None
    skills: list[str]
    target_roles: list[str] | None = None


class CandidateResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    education: str | None = None
    experience: str | None = None
    skills: list[str] | None = None
    target_roles: list[str] | None = None

    class Config:
        from_attributes = True