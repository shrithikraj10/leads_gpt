from pydantic import BaseModel
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    email: str
    industry: str

class LeadUpdate(BaseModel):
    name: str
    email: str
    industry: str

class LeadResponse(BaseModel):
    id: int
    name: str
    email: str
    industry: str
    created_at: datetime

    class Config:
        orm_mode = True
