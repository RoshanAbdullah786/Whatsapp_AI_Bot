from databases import Database
from sqlalchemy import create_engine
from app.database.models import metadata

DATABASE_URL = "sqlite:///./whatsapp_chatbot.db"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

# Create tables
metadata.create_all(engine)

async def save_message(phone_number: str, role: str, content: str):
    query = """
    INSERT INTO messages (phone_number, role, content) 
    VALUES (:phone_number, :role, :content)
    """
    await database.execute(query, {"phone_number": phone_number, "role": role, "content": content})

async def get_message_history(phone_number: str):
    query = """
    SELECT role, content FROM messages 
    WHERE phone_number = :phone_number 
    ORDER BY timestamp
    """
    rows = await database.fetch_all(query, {"phone_number": phone_number})
    return [{"role": row["role"], "content": [{"type":"text","text":row["content"]}]} for row in rows]
