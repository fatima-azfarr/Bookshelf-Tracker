from enum import Enum

from pydantic import BaseModel, Field


class Genre(str,Enum):
    fiction = "fiction"
    non_fiction = "nonfiction"
    sci_fi = "scifi"
    biography = "biography"
    fantasy = "fantasy"
 
class BaseBook(BaseModel):
    title : str 
    author : str
    pages : int | None = None
    genre : Genre
    ratings : int | None = Field(default = None,ge=1,le=5)


class Status(str,Enum):
    to_read = "toread"
    reading = "reading"
    finished = "finished"

class ReadBook(BaseBook):
    id : int
    status : Status
    

class AddBook(BaseBook):
    pass

class EditBook(BaseBook):
    status : Status
    

class StatusUpdate(BaseModel):
    status : Status
    
    