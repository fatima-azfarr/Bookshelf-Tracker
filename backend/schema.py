from enum import Enum

from pydantic import BaseModel, Field


class BaseBook(BaseModel):
    title : str 
    author : str
    pages : int | None = None

class Genre(str,Enum):
    fiction = "fiction"
    non_fiction = "nonfiction"
    Sci_fi = "scifi"
    biography = "biography"
    fantasy = "fantasy"

class Status(str,Enum):
    to_read = "toread"
    reading = "reading"
    finised = "finished"

class ReadBook(BaseBook):
    id : int
    genre : Genre
    ratings : int | None = Field(default = None,ge=1,le=5)

class AddBook(BaseBook):
    pass

class EditBook(BaseBook):
    status : Status
    ratings : int | None = Field(default = None,ge=1,le=5)

class StatusUpdate(BaseBook):
    status : Status
    ratings : int | None = Field(default = None,ge=1,le=5)
    