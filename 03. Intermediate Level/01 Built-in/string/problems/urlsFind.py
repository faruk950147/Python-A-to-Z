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


'''
Step-by-step breakdown

ধরো:

url = "https://www.google.com/search"
Step 1: "www." দিয়ে split
url.split("www.")

Result:

['https://', 'google.com/search']
Step 2: index [1]
'google.com/search'
Step 3: / দিয়ে split
['google.com', 'search']
Step 4: [0]
google.com
Final:
google.com
Problem (IMPORTANT)

এই method সব URL এ কাজ করে না 

Case 1:
url = "https://example.com/page"

`"www
." নাই → crash

Case 2:
url = "example.com/page"

structure ভিন্ন → ভুল result

Case 3:
url = "ftp://www.site.com"

unpredictable

Method 2: Smart Manual Fix
def urlsFind(url):
    if "://" in url:
        url = url.split("://")[1]

    domain = url.split("/")[0]

    if domain.startswith("www."):
        domain = domain[4:]

    return domain
Example:
print(urlsFind("https://www.google.com/search"))
# google.com

print(urlsFind("http://example.com/page"))
# example.com

print(urlsFind("example.com/test"))
# example.com
Method 3: Best (Professional Way)

Python built-in library ব্যবহার করো

from urllib.parse import urlparse

def urlsFind(url):
    return urlparse(url).netloc
Example:
print(urlsFind("https://www.google.com/search"))
# www.google.com

print(urlsFind("http://example.com/page"))
# example.com
# যদি www. বাদ দিতে চাও
from urllib.parse import urlparse

def urlsFind(url):
    domain = urlparse(url).netloc
    return domain.replace("www.", "")
Comparison
Method	Easy	Safe	Recommended
তোমার কোড	✅	❌	❌
Manual Fix	✅	⚠️	⚠️
urlparse	✅	✅  BEST
Real World Tip

Scraping, Django project, API — সব জায়গায়
always use urlparse 

Bonus (Interview Question)

Difference:

split() → string ভাঙে
urlparse() → URL বুঝে parse করে (smart)
'''