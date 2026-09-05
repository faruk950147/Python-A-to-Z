import re

text = "2025-10-21 the conference will be held on 2025-10-21"
match = re.findall(r"\d{4}-\d{2}-\d{2}", text)
if match:
    print(f"1. Found {match}")
else:
    print(f"1. Not found {text}")
    
# output: ['2025-10-21', '2025-10-21']