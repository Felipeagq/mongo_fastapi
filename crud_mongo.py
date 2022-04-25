from typing import Awaitable
from models import RequestBook, ResponseBook
from config import database
import uuid

class BookCRUD():
    
    @staticmethod
    async def read_all():
        _book = []
        collection = database['booka'].find()
        async for book in collection:
            _book.append(book)
        return _book
    
    @staticmethod
    async def create(book:RequestBook):
        id = str(uuid.uuid4())
        _book = {
            "_id":id,
            "title":book.title,
            "description": book.description
        }
        await database['booka'].insert_one(_book)



    @staticmethod
    async def update(id:str, book:RequestBook):
        _book = await database["booka"].find_one({"id":id})
        _book["title"] = book.get("title","-sin-titulo")
        _book["description"] = book.get("description","-sin-descripción-")
        await database.get_collection("book").update_one({"id":id},{"$set":_book})
    
    
    @staticmethod
    async def get_id(id:str):
        return await database.get_collection("book").find_one({"_id":id})
    
    
    @staticmethod
    async def delete(id:str):
        await database.get_collection("book").delete_one({"_id":id})