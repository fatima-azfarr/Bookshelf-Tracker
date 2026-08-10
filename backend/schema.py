from enum import Enum

from pydantic import BaseModel, Field


class Genre(str, Enum):
    fiction = "fiction"
    non_fiction = "nonfiction"
    sci_fi = "sci_fi"
    biography = "biography"
    fantasy = "fantasy"


class Status(str, Enum):
    to_read = "to_read"
    reading = "reading"
    finished = "finished"


class BaseBook(BaseModel):
    title: str
    author: str
    pages: int | None = None
    genre: Genre


class ReadBook(BaseBook):
    id: int
    status: Status
    rating: int | None = Field(default=None, ge=1, le=5)


class AddBook(BaseBook):
    pass


class EditBook(BaseBook):
    status: Status
    rating: int | None = Field(default=None, ge=1, le=5)


class StatusUpdate(BaseModel):
    status: Status
    rating: int | None = Field(default=None, ge=1, le=5)
