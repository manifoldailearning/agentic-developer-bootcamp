import requests

response = requests.get("http://localhost:8000/")
print(response.text)
print(response.status_code)
# print(response.json())