import requests

response = requests.get("https://www.geeksforgeeks.org/")

print("Status Code:", response.status_code)

print("\nResponse Content:")
print(response.text)