import re

with open(r"L:/Programming/Programming/All-Main-Problem-Solving/Python-A-to-Z/04. Advanced Level/06 Concurrency/Regex/email search/email.txt", "r") as file:
    data = file.read()

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", data)

gmail = []
yahoo = []

for email in emails:
    if "@gmail.com" in email:
        gmail.append(email)
    elif "@yahoo.com" in email:
        yahoo.append(email)

print("All Emails:", emails)
print("Gmail Emails:", gmail)
print("Yahoo Emails:", yahoo)