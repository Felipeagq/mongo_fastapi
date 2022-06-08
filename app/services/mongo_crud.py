
from app.db.mongo.mg_core import database,conn

async def read_all():
    return conn.books.user.find()


async def create(user):
    conn.books.user.insert_one(dict(user))
    return user
