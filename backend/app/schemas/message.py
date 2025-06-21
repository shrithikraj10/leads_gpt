# app/schemas/message.py

from pydantic import BaseModel, EmailStr

class Lead(BaseModel):
    name: str
    industry: str
    email: EmailStr

class MessageResponse(BaseModel):
    message: str
