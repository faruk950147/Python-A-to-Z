import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()
start_url = "https://books.toscrape.com/"

depth = 2
queue = [(start_url, depth)] 
print(queue[0][0])
print(queue[0][1])
while queue:
    url, current_depth = queue.pop(0)
    # print(url)
    # print(current_depth)