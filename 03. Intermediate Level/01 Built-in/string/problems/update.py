'''ফাংশনটা যেটা করছে সেটা হলো string-এর নির্দিষ্ট index-এর character replace করা slicing দিয়ে।

কোডটা কীভাবে কাজ করে
def update_string(string, index, char):
    return string[:index] + char + string[index + 1:]

এখানে ৩টা অংশ আছে:

string[:index] → index এর আগ পর্যন্ত অংশ
char → যেটা বসাতে চাও
string[index + 1:] → index-এর পরের অংশ
তোমার ইনপুট:
update_string("hello", 1, "xl")

string = "hello"
index = 1 → এখানে আছে "e"
char = "xl"

ধাপে ধাপে:
"hello"[:1] → "h"
"xl" → নতুন character (এখানে ২টা অক্ষর)
"hello"[2:] → "llo"

এখন যোগ করলে:

"h" + "xl" + "llo" = "hxlllo"
'''
def update_string(string, index, char):
    return string[:index] + char + string[index + 1:]

print(update_string("hello", 1, "xl"))

# hello -> hxllo


