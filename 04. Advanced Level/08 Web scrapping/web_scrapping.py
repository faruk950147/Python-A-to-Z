import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.youtube.com/watch?v=VIksvMzIS0g')



soup = BeautifulSoup(res.text, 'lxml')
print(soup)

# create a file
# with open('text.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

