from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from .schema import AddBook, EditBook, Genre, ReadBook, Status, StatusUpdate

app = FastAPI()

books: dict[int, ReadBook] = {
    1: ReadBook(
        id=1,
        title="Project Hail Mary",
        author="Andy Weir",
        pages=496,
        genre=Genre.sci_fi,
        status=Status.finished,
        ratings=5,
    ),
    2: ReadBook(
        id=2,
        title="Educated",
        author="Tara Westover",
        pages=334,
        genre=Genre.biography,
        status=Status.finished,
        ratings=4,
    ),
    3: ReadBook(
        id=3,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        pages=310,
        genre=Genre.fantasy,
        status=Status.reading,
        ratings=None,
    ),
    4: ReadBook(
        id=4,
        title="Sapiens",
        author="Yuval Noah Harari",
        pages=443,
        genre=Genre.non_fiction,
        status=Status.reading,
        ratings=None,
    ),
    5: ReadBook(
        id=5,
        title="Dune",
        author="Frank Herbert",
        pages=412,
        genre=Genre.sci_fi,
        status=Status.to_read,
        ratings=None,
    ),
    6: ReadBook(
        id=6,
        title="Normal People",
        author="Sally Rooney",
        pages=273,
        genre=Genre.fiction,
        status=Status.to_read,
        ratings=None,
    ),
    7: ReadBook(
        id=7,
        title="Steve Jobs",
        author="Walter Isaacson",
        pages=656,
        genre=Genre.biography,
        status=Status.to_read,
        ratings=None,
    ),
}


@app.get("/book/{id}", response_model=ReadBook)
def book_read(id: int) -> ReadBook:

    # check the id
    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid request,the given id doesn't exits!",
        )
    return books[id]


@app.post("/book", response_model=ReadBook)
def submit_book(body: AddBook) -> ReadBook:

    # create and assign the books a new id
    new_id = max(books.keys()) + 1

    # add content to the new id
    new_book = ReadBook(
        id=new_id,
        title=body.title,
        author=body.author,
        pages=body.pages,
        genre=body.genre,
        status=Status.to_read,
        ratings=None,
    )
    books[new_id] = new_book
    return new_book


@app.patch("/book/{id}", response_model=ReadBook)
def patch_book(id: int, body: StatusUpdate) -> ReadBook:
    # check the id
    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid request,the given id doesn't exits!",
        )
    book = books[id]
    book.status = body.status
    books[id] = book
    return book


@app.put("/book/{id}", response_model=ReadBook)
def update_book(id: int, body: EditBook) -> ReadBook:
    # check the id
    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid request,the given id doesn't exits!",
        )
    books[id] = ReadBook(id=id, **body.model_dump())
    return books[id]


@app.delete("/book/{id}")
def delete_book(id: int) -> dict[str, str]:
    if id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid request, the given id doesn't exist!",
        )
    books.pop(id)
    return {"detail": f"The book #{id} is deleted"}

#for scalar documentation
@app.get("/scalar", include_in_schema=False)
def scalar_documentation():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="scalar" )
