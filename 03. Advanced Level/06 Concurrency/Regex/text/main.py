import re

with open("email.txt", "r") as file:
    text = file.read()

# All emails
all_emails_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
all_emails = re.findall(all_emails_pattern, text, re.IGNORECASE)

# Gmail
gmail_pattern = r"\b[A-Za-z0-9._%+-]+@gmail\.com\b"
gmail_emails = re.findall(gmail_pattern, text, re.IGNORECASE)

# Yahoo
yahoo_pattern = r"\b[A-Za-z0-9._%+-]+@yahoo\.com\b"
yahoo_emails = re.findall(yahoo_pattern, text, re.IGNORECASE)

print("All Emails:", all_emails)
print("Gmail Emails:", gmail_emails)
print("Yahoo Emails:", yahoo_emails)


# ====================== Specific email ======================
with open("email.txt", "r") as file:
    text = file.read()

specific_email = "example@gmail.com"

# Search Specific email
if re.search(re.escape(specific_email), text):
    print(f"{specific_email} found")
else:
    print(f"{specific_email} not found")
