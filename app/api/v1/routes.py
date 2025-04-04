from fastapi import APIRouter
from app.services.cve_service import fetch_cve

router = APIRouter()

@router.get("/cve/{cve_id}")
async def get_cve(cve_id: str):
    return await fetch_cve(cve_id)
