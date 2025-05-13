from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

router = APIRouter()

class Lead(BaseModel):
    name: str
    email: str
    company: str
    industry: str

# Simulated in-memory database
leads_db = {}

# Create a new lead
@router.post("/leads/create")
async def create_lead(lead: Lead):
    lead_id = str(uuid4())
    leads_db[lead_id] = lead.dict()
    return {"lead_id": lead_id, "lead": lead}

# Get a lead by ID
@router.get("/leads/{lead_id}")
async def get_lead(lead_id: str):
    lead = leads_db.get(lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return {"lead_id": lead_id, "lead": lead}

# Search leads
@router.get("/search")
async def search_leads(
    name: Optional[str] = Query(None),
    industry: Optional[str] = Query(None)
):
    results = []

    for lead_id, lead in leads_db.items():
        if name and name.lower() not in lead["name"].lower():
            continue
        if industry and industry.lower() not in lead["industry"].lower():
            continue
        results.append({"lead_id": lead_id, "lead": lead})

    if not results:
        raise HTTPException(status_code=404, detail="Lead not found")
    return results

# Bulk create leads
@router.post("/bulk-create")
async def bulk_create_leads(leads: List[Lead]):
    created = []
    for lead in leads:
        lead_id = str(uuid4())
        leads_db[lead_id] = lead.dict()
        created.append({"lead_id": lead_id, "lead": lead})
    return {"message": f"{len(created)} leads created", "leads": created}

# Partial update lead
@router.patch("/leads/{lead_id}")
async def partial_update_lead(lead_id: str, updates: dict):
    lead = leads_db.get(lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    lead.update(updates)
    leads_db[lead_id] = lead
    return {"message": "Lead partially updated", "lead": lead}
