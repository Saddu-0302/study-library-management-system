from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.seat import SeatResponse
from app.services.seat_service import SeatService

router = APIRouter(
    prefix="/seats",
    tags=['Seats']
)
seat_service = SeatService()

@router.get("/",response_model=list[SeatResponse])
def get_all_seats(db:Session = Depends(get_db)):
    return seat_service.get_all_seats(db)