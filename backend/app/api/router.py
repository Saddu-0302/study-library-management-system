from fastapi import APIRouter
from app.api.v1.endpoints import students,seats,bookings

api_router = APIRouter()
api_router.include_router(students.router)
api_router.include_router(seats.router)
api_router.include_router(bookings.router)