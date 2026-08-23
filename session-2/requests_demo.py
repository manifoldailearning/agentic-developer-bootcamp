# pip install requests
import requests

response = requests.get("https://www.google.com")
print(response.text)
print(response.status_code)
# print(response.json())