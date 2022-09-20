from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int
    # age: int = Field(..., gt=15, lt=90, description="My description for data ff")

    # @validator('age')
    # def check_age(cls, v):
    #     if v < 15:
    #         raise ValueError("qwerrty")
    #     return v
