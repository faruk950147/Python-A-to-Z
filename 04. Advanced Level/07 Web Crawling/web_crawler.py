
import os
import requests

class Crawler:
    def __init__(self, url):
        self.url = url

    def create_directory(self):
        print(self.url)
        print(self.url.split("//"))
        folder_name = self.url.split("//")[-1].split("/")[0]
        print('folder name', folder_name)

        path = os.path.join("websites", folder_name)
        os.makedirs(path, exist_ok=True)
        return path

    def crawl_website(self):
        folder_path = self.create_directory()  

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print("Failed to download:", e)
            return None

        file_path = os.path.join(folder_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
            # print(response.text)

        print(f"Downloaded HTML to: {file_path}")
        return file_path

# usage
crawler = Crawler("https://www.python.org/")
crawler.crawl_website()

'''
class Crawler:
    def __init__(self, url, visited=None):
        self.url = url  # remove comma here!
        self.visited = set() if visited is None else set(visited)

    def create_directory(self):
        folder_name = self.url.split("//")[-1].split("/")[0]
        path = os.path.join("websites", folder_name)
        os.makedirs(path, exist_ok=True)
        return path

    def crawl_website(self):
        if self.url in self.visited:
            print(f"Already visited: {self.url}")
            return None

        self.visited.add(self.url)
        folder_path = self.create_directory()  

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print("Failed to download:", e)
            return None

        file_path = os.path.join(folder_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded HTML to: {file_path}")
        return file_path

# usage
crawler = Crawler("https://www.python.org/")
crawler.crawl_website()


import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Crawler:
    def __init__(self, url, visited=None):
        self.url = url
        self.visited = set() if visited is None else set(visited)

    def create_directory(self):
        folder_name = self.url.split("//")[-1].split("/")[0]
        path = os.path.join("websites", folder_name)
        os.makedirs(path, exist_ok=True)
        return path

    def crawl_website(self):
        if self.url in self.visited:
            print(f"Already visited: {self.url}")
            return None

        self.visited.add(self.url)
        folder_path = self.create_directory()  

        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
        except Exception as e:
            print("Failed to download:", e)
            return None

        file_path = os.path.join(folder_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Downloaded HTML to: {file_path}")

        # Extract all links
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(self.url, a_tag['href'])
            links.add(link)

        print(f"Found {len(links)} links on the page:")
        for link in links:
            print(link)

        return file_path, links

# usage
crawler = Crawler("https://www.python.org/")
crawler.crawl_website()




'''
