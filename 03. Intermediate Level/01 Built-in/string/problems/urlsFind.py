def urlsFind(url):
    # Extract the domain name from the URL
    if "www." in url:
        domain = url.split("www.")[1].split("/")[0]
    else:
        domain = url.split("/")[2]
    return domain

print(urlsFind("https://www.example.com/"))

from urllib.parse import urlparse

def urlsFind(url):
    parsed = urlparse(url)
    return parsed.netloc

print(urlsFind("https://www.example.com/"))


print(urlsFind("http://example.com/path"))
# Output: example.com