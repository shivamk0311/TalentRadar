from sqlalchemy import Column, Integer, String, ARRAY
from app.database import Base

class JobDB(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    salary = Column(String, nullable=True)
    skills = Column(ARRAY(String), nullable=True)
    source = Column(String, nullable=True)
    employment_type = Column(String, nullable=True)
