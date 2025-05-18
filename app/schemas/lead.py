from pydantic import BaseModel, EmailStr
from typing import Optional


class LeadBase(BaseModel):
    name: str
    email: EmailStr
    company: str
    industry: str


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    company: Optional[str] = None
    industry: Optional[str] = None


class LeadOut(LeadBase):
    lead_id: str
