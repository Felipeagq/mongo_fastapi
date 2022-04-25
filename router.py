from unittest import result
from fastapi import APIRouter
from crud_mongo import BookCRUD
from models import RequestBook,ResponseBook

router = APIRouter()

@router.get("/book")
async def get_book():
    _bookList = await BookCRUD.read_all()
    return ResponseBook(code=200,
    status="ok",
    message="Success search",
    result=_bookList).dict(exclude_none=True)


@router.get("/book/{id}")
async def get_book_id(id:str):
    _book = await BookCRUD.get_id(id)
    return ResponseBook(code=200,
    status="ok",
    message="Success search by id",
    result=_book).dict(exclude_none=True)


@router.post("/book/create")
async def create_book(book: RequestBook):
    await BookCRUD.create(book)
    return ResponseBook(code=200,
    status="ok",
    message="Post Created",
    result=book).dict(exclude_none=True)


@router.put("/book/update/{id}")
async def update_book(id:str, book: RequestBook):
    _book = await BookCRUD.update(id,book)
    return ResponseBook(code=200,
    status="ok",
    message="Success update",
    result=_book).dict(exclude_none=True)


@router.delete("/book/{id}")
async def delete_book(id:str):
    _book = await BookCRUD.delete(id)
    return ResponseBook(code=200,
    status="ok",
    message="Success deleted",
    result=str(_book)).dict(exclude_none=True)
