from fastapi import APIRouter

"""FastAPI docs to unit test the endpoints"""

router = APIRouter()

@router.get("/generate")
def test_upload():
    return {"message": "Generate route works"}