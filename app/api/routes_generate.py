from fastapi import APIRouter, Request, HTTPException
from app.core.llm_provider import generate_with_fallback

router = APIRouter()

@router.post("/")
async def generate_message(request: Request):
    body = await request.json()
    name = body.get("name")
    industry = body.get("industry")
    email = body.get("email")

    if not (name and industry and email):
        raise HTTPException(status_code=400, detail="Missing required fields")

    prompt = (
        f"Generate a professional lead generation message for a person named {name} "
        f"in the {industry} industry. Contact email: {email}."
    )

    message = generate_with_fallback(prompt)
    return {"message": message}
