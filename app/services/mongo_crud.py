
from bson import ObjectId
from app.db.mongo.mg_core import database,conn

async def read_all():
    return conn.books.user.find()


async def create(user):
    conn.books.user.insert_one(dict(user))
    return user


async def update(id,user):
    conn.books.user.find_one_and_update(
        {"_id":ObjectId(id)},
        {"$set":dict(user)}
    )
    return user


async def delete(id):
    r = conn.books.user.find_one_and_delete(
        {"_id":ObjectId(id)}
    )
    return r