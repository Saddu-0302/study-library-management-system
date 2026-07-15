from app.models.seat import Seat 
from app.repository.base_repository import BaseRepository

from sqlalchemy.orm import Session


class SeatRepository(BaseRepository[Seat]):
    def __init__(self):
        super().__init__(Seat)
    
    def get_by_seat_number(self,db:Session,seat_number:int):
        return (
            db.query(Seat)
            .filter(Seat.seat_number == seat_number)
            .first()
        )
