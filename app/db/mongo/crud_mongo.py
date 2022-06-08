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
        _book = await database["booka"].find_one({"_id":id})
        print(_book)
        print(book)
        _book["title"] = book.title
        _book["description"] = book.description
        await database["booka"].update_one({"_id":id},{"$set":_book})
        return _book
    
    
    @staticmethod
    async def get_id(id:str):
        return await database["booka"].find_one({"_id":id})
    
    
    @staticmethod
    async def delete(id:str):
        _book = await database["booka"].delete_one({"_id":id})
        print(str(_book))
        return _book