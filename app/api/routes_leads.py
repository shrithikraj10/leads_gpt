from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.schemas import LeadCreate, LeadUpdate, LeadResponse
from app.crud.lead import create_lead, get_lead, get_all_leads, update_lead, delete_lead

router = APIRouter()

@router.post("/", response_model=LeadResponse)
async def create_new_lead(lead: LeadCreate):
    created = await create_lead(lead.name, lead.email, lead.industry)
    return created

@router.get("/{lead_id}", response_model=LeadResponse)
async def read_lead(lead_id: int):
    lead = await get_lead(lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.get("/", response_model=List[LeadResponse])
async def read_all_leads():
    leads = await get_all_leads()
    return leads

@router.put("/{lead_id}", response_model=LeadResponse)
async def update_existing_lead(lead_id: int, lead: LeadUpdate):
    updated = await update_lead(lead_id, lead.name, lead.email, lead.industry)
    if not updated:
        raise HTTPException(status_code=404, detail="Lead not found")
    return updated

@router.delete("/{lead_id}")
async def delete_existing_lead(lead_id: int):
    result = await delete_lead(lead_id)
    return result
