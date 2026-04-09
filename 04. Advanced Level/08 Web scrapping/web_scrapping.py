""" 
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wscubetech.com/')

# HTML content
print(response.text)

# Save to file
with open('text.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

"""
    
    
    
import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.youtube.com/watch?v=VIksvMzIS0g')

print("Without beautyful soup" + res.content)

# soup = BeautifulSoup(res.content, 'html.parser')

# create a file
# with open('text.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

