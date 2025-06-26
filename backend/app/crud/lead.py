from sqlalchemy import insert, select
from app.db.models import Lead
from app.db.database import database

# Create lead
async def create_lead(name: str, email: str, industry: str):
    query = insert(Lead).values(name=name, email=email, industry=industry)
    lead_id = await database.execute(query)
    return await get_lead(lead_id)

# Get Lead by ID
async def get_lead(lead_id: int):
    query = select(Lead).where(Lead.id == lead_id)
    lead = await database.fetch_one(query)
    return dict(lead) if lead else None

# Get All Leads
async def get_all_leads():
    query = select(Lead)
    leads = await database.fetch_all(query)
    return [dict(l) for l in leads]

# Update Lead
async def update_lead(lead_id: int, name: str, email: str, industry: str):
    query = (
        Lead.__table__.update()
        .where(Lead.id == lead_id)
        .values(name=name, email=email, industry=industry)
    )
    await database.execute(query)
    return await get_lead(lead_id)

# Delete Lead
async def delete_lead(lead_id: int):
    query = Lead.__table__.delete().where(Lead.id == lead_id)
    await database.execute(query)
    return {"message": f"Lead with id {lead_id} deleted"}
