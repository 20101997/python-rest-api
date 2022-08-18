from fastapi import FastAPI
from pydantic import BaseModel


class Job(BaseModel):
    id: int
    name: str
