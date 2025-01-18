from datetime import date

from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()

class Course:
    id: int
    title: str
    instructor: str
    rating: int
    published_year: int

    def __init__(self, id: int, title: str, instructor: str, rating: int, published_year: int):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.published_year = published_year


courses_db = [
    Course(1, "Python", "Atil", 5, 2034),
    Course(2, "Java", "Ali", 4, 2029),
    Course(3, "R", "Beyza", 4, 2028),
    Course(4, "C#", "Ahmet", 5, 2045),
    Course(5, "JavaScript", "Atil", 1, 2036),
    Course(6, "Swift", "Zeynep", 2, 2025),

]
