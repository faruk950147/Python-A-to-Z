import os
from datetime import datetime
import requests

response = requests.get("https://www.geeksforgeeks.org/")

print("Status Code:", response.status_code)

print("\nResponse Content:")
print(response.text)


'''
class Crawler:
    def __init__(self, url):
        self.url = url
        
    def create_folder(self):
    
        # url: https://www.geeksforgeeks.org/
        print(self.url)
        # url: ['https:', '', 'www.geeksforgeeks.org', '']
        print(self.url.split("//"))
        # url: ['https:', '', 'www.geeksforgeeks.org', '']
        print(self.url.split("//")[-1])
        # url: ['www.geeksforgeeks.org', '']
        print(self.url.split("//")[-1].split("/"))
        # url: ['www', 'geeksforgeeks', 'org']
        print(self.url.split("//")[-1].split("/")[0])
        # url: www.geeksforgeeks.org
        # folder_name: www.geeksforgeeks.org

        folder_name = self.url.split("//")[-1].split("/")[0]
        
        path = os.path.join(
            "L:\\Programming\\Programming\\All-Main-Problem-Solving\\Python-A-to-Z\\04. Advanced Level",
            "07 Web Crawling\\websites",
            folder_name
        )
        
        os.makedirs(path, exist_ok=True)  # already handles exists
        
        return path

    def crawl(self):
        folder_path = self.create_folder()
        response = requests.get(self.url)
        with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(response.text)
        return response.text

crawler = Crawler("https://www.python.org/")
print(crawler.crawl())
'''