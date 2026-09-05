import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

# 2. Basic Data Extraction

# 2.1 tag select
# print(soup.title)
# print(soup.h1)
# print(soup.p)

# 2.2 text extract
# print(soup.title.text)
# print(soup.h1.text)
# print(soup.p.text)

# 2.3 attributes extract
# print(soup.title.attrs)
# print(soup.h1.attrs)
# print(soup.p.attrs)
print(f"soup.a['href'] = {soup.a['href']}")


'''
# all books select
books = soup.find_all("article", class_="product_pod")
# 3. Book Data Extract
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    stock = book.find("p", class_="instock availability").text.strip()

    print(title, price, stock)
    
# 4. Link & Image Extract
# Book link
link = book.h3.a["href"]
# Image
image = book.find("img")["src"]
image_url = "https://books.toscrape.com/" + image

# 5. Pagination (all pages scrape)
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1, 51):  # total 50 pages
    url = base_url.format(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        print(f"Page {page}:", title, price)
        
# 6. CSV File Save
import csv

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Stock"])

    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            stock = book.find("p", class_="instock availability").text.strip()

            writer.writerow([title, price, stock])
            
# 7. Image Download
import os

os.makedirs("images", exist_ok=True)

for book in books:
    img = book.find("img")["src"]
    img_url = "https://books.toscrape.com/" + img

    img_data = requests.get(img_url).content

    filename = img.split("/")[-1]

    with open(f"images/{filename}", "wb") as f:
        f.write(img_data)
        
# 8. Advanced (Production Tips)
# Headers use (block avoid)
headers = {
    "User-Agent": "Mozilla/5.0"
}
requests.get(url, headers=headers)
# Error Handling (simple way)
if res.status_code == 200:
    print("Success")
else:
    print("Failed")
    
# Delay (important)
import time
time.sleep(1)
# 9. CSS Selector (Pro Level)
books = soup.select(".product_pod")

for book in books:
    title = book.select_one("h3 a")["title"]
    price = book.select_one(".price_color").text
    
    
'''    
    
    
