import re
'''
. matches any single character
^ matches the start of the string
$ matches the end of the string
* matches zero or more occurrences of the preceding character
+ matches one or more occurrences of the preceding character
? matches zero or one occurrence of the preceding character
| matches either the pattern before or the pattern after it
\w matches any word character (alphanumeric & underscore)
\d matches any digit (0-9)
\s matches any whitespace character
\S matches any non-whitespace character
\b matches a word boundary
\B matches a non-word boundary
\A matches the start of the string
\Z matches the end of the string
\n matches a newline character
\r matches a carriage return character
\t matches a tab character
\f matches a form feed character
\v matches a vertical tab character
\a matches a bell character
\e matches an escape character
\f matches a form feed character
\n matches a newline character
\r matches a carriage return character
\t matches a tab character
\f matches a form feed character
\v matches a vertical tab character
\a matches a bell character
\e matches an escape character
\f matches a form feed character
\n matches a newline character
\r matches a carriage return character
\t matches a tab character
\f matches a form feed character
\v matches a vertical tab character
\a matches a bell character

[a-z] this means any lowercase letter
[A-Z] this means any uppercase letter
[0-9] this means any number
[._%+-] this means any dot, underscore, percent, plus, or hyphen
[a-zA-Z] this means any letter
[a-zA-Z0-9] this means any letter or number
[a-zA-Z0-9._%+-] this means any letter, number, dot, underscore, percent, plus, or hyphen
[a-zA-Z0-9.-] this means any letter, number, dot, or hyphen
[a-zA-Z0-9.-.] this means any letter, number, dot, or hyphen

[a-zA-Z0-9._%+-]+: One or more characters that can be letters, numbers, dots, underscores, percent signs, plus signs, or hyphens.
@: The @ symbol.
[a-zA-Z0-9.-]+: One or more characters that can be letters, numbers, dots, or hyphens.
\.: The dot character (escaped with a backslash because it has a special meaning in regular expressions).
[a-zA-Z]{2,}: Two or more letters.
'''
import re

with open(r"L:/Programming/Programming/All-Main-Problem-Solving/Python-A-to-Z/04. Advanced Level/06 Concurrency/Regex/email search/email.txt", "r") as file:
    data = file.read()

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}", data)

gmail = []
yahoo = []
others = []

for email in emails:
    domain = email.split("@")[1]

    if domain == "gmail.com":
        gmail.append(email)
    elif domain == "yahoo.com":
        yahoo.append(email)
    else:
        others.append(email)

print("All Emails:", emails)
print("Gmail Emails:", gmail)
print("Yahoo Emails:", yahoo)
print("Others:", others)

'''
import re

with open(r"L:/Programming/Programming/All-Main-Problem-Solving/Python-A-to-Z/04. Advanced Level/06 Concurrency/Regex/email search/email.txt", "r") as file:
    data = file.read()

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}", data)

gmail = re.findall(r"[a-zA-Z0-9_.+-]+@gmail\.com", data)
yahoo = re.findall(r"[a-zA-Z0-9_.+-]+@yahoo\.com", data)

others = [e for e in emails if not re.search(r"@(gmail\.com|yahoo\.com)$", e)]

print("All Emails:", emails)
print("Gmail Emails:", gmail)
print("Yahoo Emails:", yahoo)
print("Others:", others)
'''