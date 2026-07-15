from app.models.booking import Booking
from app.repository.base_repository import BaseRepository

class BookingRepository(BaseRepository[Booking]):
    def __init__(self):
        super().__init__(Booking)
