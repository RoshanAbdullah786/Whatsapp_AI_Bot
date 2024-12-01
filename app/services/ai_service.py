import httpx

async def get_ai_response(message_history: list):
    url = "https://openrouter.ai/api/v1/chat/completions"
    key = "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"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "google/learnlm-1.5-pro-experimental:free",
        "messages": message_history,
        "max_tokens":200
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url=url,
            headers=headers,
            json=payload)  # Automatically serializes the dictionary to JSON
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
