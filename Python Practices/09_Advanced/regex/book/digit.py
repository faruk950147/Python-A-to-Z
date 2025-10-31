import re

phone = "phone number 08801712345678"
if re.search(r'\d+', phone):
    print(re.search(r'\d+', phone).group())
else:
    print("Not found")

