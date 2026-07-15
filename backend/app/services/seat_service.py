from sqlalchemy.orm import Session
from app.repository.seat_repository import SeatRepository


class SeatService:
    def __init__(self):
        self.repository = SeatRepository()
    def get_all_seats(self,db:Session):
        return self.repository.get_all(db)
    