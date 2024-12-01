from fastapi import FastAPI
from app.routes.chatbot import router as chatbot_router
from app.database.db import database

app = FastAPI(title="WhatsApp Chatbot", version="1.0.0")

# Include routes
app.include_router(chatbot_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Welcome to the WhatsApp Chatbot API!"}
