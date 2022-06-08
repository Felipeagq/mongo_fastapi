from pymongo.mongo_client import MongoClient
from app.config.settings import settings
from motor.motor_asyncio import AsyncIOMotorClient

# Create the connector
conn = MongoClient(settings.MONGO_DATABASE_URL)

client = AsyncIOMotorClient(settings.MONGO_DATABASE_URL)
database = client["books"]
