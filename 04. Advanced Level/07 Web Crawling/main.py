import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()
start_url = "https://www.geeksforgeeks.org/"

depth = 2  # how many levels to crawl
queue = [(start_url, depth)]

