import motor.motor_asyncio

# URL del mongo
MONGODB_URL = "mongodb://root:example@localhost:27017/"

# Creación del cliente
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# Conección a la base de datos "db"
database = client["books"]
