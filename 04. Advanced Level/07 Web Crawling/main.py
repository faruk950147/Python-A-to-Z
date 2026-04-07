import os
from datetime import datetime
import requests

response = requests.get("https://www.geeksforgeeks.org/")

# check the status code
print("Status Code:", response.ok)


