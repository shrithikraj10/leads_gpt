from pydantic import BaseModel

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

    class Config:
        orm_mode = True
