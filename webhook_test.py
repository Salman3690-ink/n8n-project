import requests


user_message = "create a task for me name as learn n8n basic for me"

request_message = {"message": user_message}

url = "https://mimag.app.n8n.cloud/webhook/c2724128-3e3e-4b2e-a5e6-4b0f84386bf0"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])