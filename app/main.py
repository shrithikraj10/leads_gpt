from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from app.db.database import engine, database, Base  # ⬅️ Import Base here
from app.db.models import Lead  # ⬅️ Import Lead model so it's registered
from app.api import routes_upload, routes_generate, routes_test, routes_leads, routes_auth

load_dotenv()

# This will now correctly create tables from ORM models
Base.metadata.create_all(bind=engine)  # ⬅️ FIXED

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(
    title="LeadsGPT",
    description="AI-powered outreach message generator for SMMA owners and high-ticket coaches.",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(routes_upload.router, prefix="/upload", tags=["Upload"])
app.include_router(routes_generate.router, prefix="/generate-message", tags=["Generate"])
app.include_router(routes_test.router)
app.include_router(routes_leads.router, prefix="/leads", tags=["Leads"])
app.include_router(routes_auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to LeadsGPT 🚀"}
