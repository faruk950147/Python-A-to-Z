import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
                
""" 
class ProductionCrawler:
    def __init__(self, start_url, max_depth=2, base_folder="websites"):
        self.start_url = start_url
        self.max_depth = max_depth
        self.base_folder = base_folder
        self.visited = set()
        self.queue = deque([(start_url, 0)])

    def create_directory(self, url):
        parsed_url = urlparse(url)
        domain_folder = parsed_url.netloc.replace(":", "_")
        path = os.path.join(self.base_folder, domain_folder)
        os.makedirs(path, exist_ok=True)
        return path

    def save_html(self, url, html):
        folder_path = self.create_directory(url)
        file_name = "index.html" if url.rstrip("/") == self.start_url.rstrip("/") else f"{hash(url)}.html"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        return file_path

    def crawl(self):
        while self.queue:
            url, depth = self.queue.popleft()
            if depth > self.max_depth or url in self.visited:
                continue

            self.visited.add(url)
            print(f"Crawling ({depth}/{self.max_depth}): {url}")

            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Failed to fetch {url}: {e}")
                continue

            file_path = self.save_html(url, response.text)
            print(f"Saved HTML: {file_path}")

            # Parse links and add to queue
            soup = BeautifulSoup(response.text, "html.parser")
            for a_tag in soup.find_all("a", href=True):
                next_url = urljoin(url, a_tag['href'])
                if next_url.startswith("http") and next_url not in self.visited:
                    self.queue.append((next_url, depth + 1))

if __name__ == "__main__":
    start_url = "https://www.python.org/"
    crawler = ProductionCrawler(start_url=start_url, max_depth=2)
    crawler.crawl()

"""
