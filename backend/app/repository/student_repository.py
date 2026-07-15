from app.models.student import Student
from app.repository.base_repository import BaseRepository
from sqlalchemy.orm import Session
from uuid import UUID

class StudentRepository(BaseRepository[Student]):
    def __init__(self):
        super().__init__(Student)
    def get_student_by_id(self,db:Session,student_id:UUID):
        return db.query(Student).filter(Student.id == student_id).first()
    