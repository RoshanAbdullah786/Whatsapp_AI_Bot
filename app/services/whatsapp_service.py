import httpx
import base64
from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.rest import Client
# Twilio API credentials
account_sid = "ACa1fb373491d820cc59ee5feaa1991f2b"
auth_token = "e3d61a1d50c6b890a7892980b8d28b18"

# Twilio API endpoint for sending messages
#http_client = AsyncTwilioHttpClient()
client = Client(account_sid, auth_token)

async def send_whatsapp_message(phone_number, message):
    reply = client.messages.create(
    from_='whatsapp:+14155238886',
    to=phone_number,
    body=message
    )
    return reply

async def get_message_status(message_sid: str):
    TWILIO_API_URL = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message_sid}.json"

    async with httpx.AsyncClient() as client:
        auth = base64.b64encode(f"{account_sid}:{auth_token}".encode()).decode()
        headers = {"Authorization": f"Basic {auth}"}

        response = await client.get(TWILIO_API_URL, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve status: {response.status_code}")
            response.raise_for_status()
