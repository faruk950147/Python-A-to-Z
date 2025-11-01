
import re

# \d+ means one or more digits
# \D+ means one or more non-digits
# \s+ means one or more whitespace
# \S+ means one or more non-whitespace
# \w+ means one or more word characters
# \W+ means one or more non-word characters
# \. special character
text = "Hello World .1235"
pattern = r"\."
match = re.findall(pattern, text)
print(match)