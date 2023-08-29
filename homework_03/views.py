from fastapi import APIRouter, status
from schemas import PongOut
router = APIRouter(tags=["Ping"])


@router.get("/", response_model=PongOut, status_code=status.HTTP_200_OK)
def get_pong():
    return PongOut()
