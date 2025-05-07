from fastapi import APIRouter

"""FastAPI docs to unit test the endpoints"""

router = APIRouter()

@router.get("/upload")
def test_upload():
    return {"message": "Upload route works"}
