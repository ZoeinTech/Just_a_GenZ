import requests
def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()

BOT_TOKEN = "8242011946:AAFTficjD9TgbJFJNC-7rKkCu4501joy5vs"
CHAT_ID = "8663010197"

result = send_message(BOT_TOKEN, CHAT_ID, "Hello from your bot!")
print(result)