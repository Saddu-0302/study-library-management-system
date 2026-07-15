from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.booking import BookingCreate,BookingResponse
from app.services.booking_service import BookingService

router = APIRouter(
    prefix="/bookings",
    tags=['Bookings']
)
booking_service = BookingService()

@router.post("/",response_model=BookingResponse)
def create_booking(booking: BookingCreate,db:Session=Depends(get_db)):
    try:
        return booking_service.create_booking(db,booking)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )