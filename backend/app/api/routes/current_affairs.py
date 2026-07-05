from fastapi import APIRouter, Depends

from app.dependencies import get_current_user
from app.services.current_affairs_service import list_affairs, today_iso


router = APIRouter(prefix="/current-affairs", tags=["current-affairs"])


@router.get("")
def get_affairs(selected_date: str | None = None, category: str | None = None, current_user=Depends(get_current_user)):
    return {"selected_date": selected_date or today_iso(), "items": list_affairs(selected_date, category)}
