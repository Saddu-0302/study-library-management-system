from dateutil.relativedelta import relativedelta
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.constants import SeatStatus
from app.models.booking import Booking
from app.repository.booking_repository import BookingRepository
from app.repository.student_repository import StudentRepository
from app.repository.seat_repository import SeatRepository


class BookingService:
    def __init__(self):
        self.booking_repository = BookingRepository()
        self.student_repository = StudentRepository()
        self.seat_repository = SeatRepository()

    def create_booking(self, db: Session, booking_data):
        # -------------------------
        # Check Student
        # -------------------------
        student = self.student_repository.get_by_id(
            db,
            booking_data.student_id
        )

        if not student:
            raise ValueError("Student not found.")

        # -------------------------
        # Check Seat
        # -------------------------
        seat = self.seat_repository.get_by_seat_number(
            db,
            booking_data.seat_number
        )

        if not seat:
            raise ValueError("Seat not found.")

        # -------------------------
        # Check Seat Availability
        # -------------------------
        if seat.status != SeatStatus.AVAILABLE:
            raise ValueError("Seat is already booked.")

        # -------------------------
        # Calculate End Date
        # -------------------------
        end_date = booking_data.start_date + relativedelta(
            months=booking_data.months
        )

        # -------------------------
        # Calculate Amount
        # -------------------------
        amount = settings.MONTHLY_FEE * booking_data.months

        # -------------------------
        # Create Booking Object
        # -------------------------
        booking = Booking(
            student_id=booking_data.student_id,
            seat_id=seat.id,
            start_date=booking_data.start_date,
            end_date=end_date,
            amount=amount,
        )

        # -------------------------
        # Save Booking
        # -------------------------
        self.booking_repository.create(db, booking)

        # -------------------------
        # Update Seat Status
        # -------------------------
        seat.status = SeatStatus.BOOKED
        self.seat_repository.update(db, seat)

        # -------------------------
        # Commit Transaction
        # -------------------------
        try:
            db.commit()
            db.refresh(booking)
        except Exception:
            db.rollback()
            raise

        return booking