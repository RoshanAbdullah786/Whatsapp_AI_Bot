from fastapi import APIRouter,Request
from app.services.ai_service import get_ai_response
from app.services.whatsapp_service import send_whatsapp_message
from app.database.db import save_message, get_message_history

router = APIRouter()

@router.post("/webhook")
async def webhook(request: Request):
    data = await request.form()
    wa_phone_number = data.get("From")
    query = data.get("Body")
    phone_number = wa_phone_number.replace("whatsapp:+91","")
    
    # Step 1: Fetch message history
    history = await get_message_history(phone_number)
    if history == []:
        history = [{"role": "user", "content": [{"type":"text","text":"You are a helpful assistant,your reply should not exceed 10 words,your name is Parthieswaran"}]}]
        history.append({"role": "assistant", "content": [{"type":"text","text":"ok"}]})
    history.append({"role": "user", "content": [{"type":"text","text":query}]})
    # Step 2: Get AI response
    ai_response = await get_ai_response(history)

    # Step 3: Save messages in DB
    await save_message(phone_number, "user", query)
    await save_message(phone_number, "assistant", ai_response)

    # Step 4: Send response to WhatsApp
    await send_whatsapp_message(wa_phone_number, ai_response)
    

    return {"response": ai_response}
