import os
import requests

class Crawler:
    def __init__(self, url):
        self.url = url
        
    def create_directory(self):
        # url: https://www.geeksforgeeks.org/ 
        print(self.url) 
        # url: ['https:', '', 'www.geeksforgeeks.org', ''] 
        
        # split the url by // 
        print(self.url.split("//")) 
        # url: ['https:', '', 'www.geeksforgeeks.org', ''] 
        
        # directory name from URL
        folder_name = self.url.split("//")[-1].split("/")[0]
        
        path = os.path.join(
            "L:\\Programming\\Programming\\All-Main-Problem-Solving\\Python-A-to-Z\\04. Advanced Level",
            "07 Web Crawling\\websites",
            folder_name
        )
        
        os.makedirs(path, exist_ok=True)
        return path

    def crawl_website(self):
        folder_path = self.create_directory()  
        
        try:
            response = requests.get(self.url, timeout=10)
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