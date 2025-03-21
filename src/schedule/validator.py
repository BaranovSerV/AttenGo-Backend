from collections import defaultdict
from pydantic import TypeAdapter
from src.schedule.shemas import LessonsDay, LessonShema, ScheduleShema


PAIR_TIMES = [
    "09:20", "11:10", "13:45", "15:35", "17:20"
]

def get_pair_number(start_time: str) -> int | None:
    for i, time in enumerate(PAIR_TIMES, start=1):
        if start_time == time:
            return i
    return None 


def adjust_teacher(lesson: LessonShema) -> None:
    if lesson.teacher and lesson.teacher.startswith("!"):
        lesson.teacher = None


def assign_pair_number(lesson: LessonShema) -> None:
    pair_number = get_pair_number(lesson.start_lesson)
    if pair_number:
        lesson.pair_number = f"{pair_number} пара"


def group_lessons_by_date(lessons: list[LessonShema]) -> defaultdict:
    grouped_lessons = defaultdict(list)
    for lesson in lessons:
        grouped_lessons[lesson.date].append(lesson)
    return grouped_lessons


def create_schedule(grouped_lessons: defaultdict) -> list[LessonsDay]:
    return [
        LessonsDay(date=date, lessons=lessons) for date, lessons in grouped_lessons.items()
    ]


def validate_schedule(data) -> ScheduleShema:
    lesson_type_adapter = TypeAdapter(list[LessonShema])
    lessons = lesson_type_adapter.validate_python(data)

    for lesson in lessons:
        adjust_teacher(lesson)
        assign_pair_number(lesson)

    grouped_lessons = group_lessons_by_date(lessons)
    
    schedule = create_schedule(grouped_lessons)

    return ScheduleShema(schedule=schedule)

