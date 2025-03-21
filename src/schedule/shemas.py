from pydantic import BaseModel, Field


class LessonShema(BaseModel):
    pair_number: str | None = None
    subject: str = Field(alias="discipline") 
    teacher: str | None = Field(alias="lecturer") 
    type_lesson: str = Field(alias="kindOfWork")  
    start_lesson: str = Field(alias="beginLesson") 
    end_lesson: str = Field(alias="endLesson")      
    auditorium: str = Field(alias="auditorium")     
    date: str = Field(alias="date")                
    building: str = Field(alias="building")         


    class Config:
        populate_by_name = True


class LessonsDay(BaseModel):
    date: str
    lessons: list[LessonShema]


class ScheduleShema(BaseModel):
    schedule: list[LessonsDay]
