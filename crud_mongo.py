from models import RequestBook, ResponseBook
from config import database
import uuid

class BookCRUD():
    
    @staticmethod
    async def read_all():
        _book = []
        collection = database.get_collection('book').find()
        async for book in collection:
            _book.append(book)
        return _book
    
    @staticmethod
    async def create(book:RequestBook):
        id = str(uuid.uuid4())
        _book = {
            "_id":id,
            "title":book.get("title","-sin-titulo-"),
            "description": book.get("description","-sin-descripción-")
        }
        await database.get_colletion('book').insert_on(book)