from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from sqlalchemy.orm import relationship

from src.infrastructure.postgres import Base


class Attendance(Base):
    __tablename__ = "attendance"


    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    date = Column(String, nullable=False)  
    attendance = Column(JSON, nullable=False)  

    student = relationship("User", back_populates="attendance")

