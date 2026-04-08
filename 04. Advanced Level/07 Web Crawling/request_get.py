import requests
url = "http://books.toscrape.com/index.html"

response = requests.get(url)

# print(response.status_code)
# print(response.status_code == requests.codes.ok)
# print(response.text)
# print(response.headers)
# print(response.content)
# print(response.json())
# print(response.url)
# print(response.history)
# print(response.elapsed)
# print(response.request)
# print(response.cookies)
print(response.raw)