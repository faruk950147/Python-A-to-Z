import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()
start_url = "https://www.geeksforgeeks.org/"

depth = 2  # how many levels to crawl
queue = [(start_url, depth)]

while queue:
    url, current_depth = queue.pop(0)
    
    if current_depth == 0 or url in visited:
        continue
    
    print("Visiting:", url)
    visited.add(url)
    
    try:
        response = requests.get(url, timeout=5)
    except:
        continue
    
    if response.status_code != 200:
        continue
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # collect all the links and add them to the queue
    for link in soup.find_all("a", href=True):
        next_url = urljoin(url, link['href'])
        if next_url.startswith("http"):
            queue.append((next_url, current_depth - 1))