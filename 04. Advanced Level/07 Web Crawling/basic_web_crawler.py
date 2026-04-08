import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()
start_url = "https://books.toscrape.com/"

depth = 2  # how many levels to crawl
queue = [(start_url, depth)] 

print(queue[0])