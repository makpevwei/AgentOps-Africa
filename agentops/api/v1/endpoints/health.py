from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/")
def root():
    return {
        "application": "AgentOps Africa",
        "status": "running",
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
    }
