"""
Opportunity API Endpoints
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"],
)


@router.get("/")
async def list_opportunities():
    """
    List opportunities.
    """
    return {
        "message": "Opportunity endpoint working.",
        "items": [],
    }
