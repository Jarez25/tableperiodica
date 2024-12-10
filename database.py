from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(MONGO_URI)
db = client.periodic_table_db  # Asegúrate de que coincida con el nombre exacto
