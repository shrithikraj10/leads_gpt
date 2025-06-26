from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    industry: str

class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    industry: Optional[str] = None

class LeadResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    industry: str
    created_at: datetime  # ✅ Ensure this is included

    class Config:
        orm_mode = True
