from fastapi import FastAPI
from app.api import routes_upload, routes_generate
from app.core.config import settings

"""Base of operations: The main.py to fulfill all the routing of different API endpoints/ Pages"""

app = FastAPI(
    title="LeadsGPT",
    description="AI-powered outreach message generator for SMMA owners and high-ticket coaches.",
    version="1.0.0"
)

# Include routes
app.include_router(routes_upload.router, prefix="/upload", tags=["Upload"])
app.include_router(routes_generate.router, prefix="/generate", tags=["Generate"])

@app.get("/")
def read_root():
    return {"message": "Welcome to LeadsGPT 🚀"}
