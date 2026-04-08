import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wscubetech.com/')

# HTML content
print(response.text)

# Save to file
with open('text.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
    
    
    
    
'''
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wscubetech.com/')

soup = BeautifulSoup(response.text, 'html.parser')

# just text find out (HTML tag)
print(soup.get_text())

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write(soup.get_text())

'''