import requests


user_message = "create a task for me name as learn n8n basic for me"

request_message = {"message": user_message}

url = "url"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])