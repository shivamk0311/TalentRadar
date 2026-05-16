from sqlalchemy import Column, Integer, String, ARRAY
from app.database import Base


class CandidateDB(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, nullable=False)

    education = Column(String, nullable=True)

    experience = Column(String, nullable=True)

    skills = Column(ARRAY(String), nullable=True)

    target_roles = Column(ARRAY(String), nullable=True)