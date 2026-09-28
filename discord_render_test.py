import os
import requests

token = os.getenv("BOT_TOKEN")

response = requests.get(
    "https://discord.com/api/v10/users/@me",
    headers={"Authorization": f"Bot {token}"}
)

print("HTTP STATUS:", response.status_code)
print("RESPONSE:", response.text)
