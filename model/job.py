from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel
class Job(declarative_base()):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    name = Column(String)