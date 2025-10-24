# 1. Question: Reverse a String
# input "Sky is blue"
# output "blue is sky"


def reverseString(str):
   #split return list ['Sky', 'is', 'blue']
   str = str.split(" ") 
   #reverse list ['blue', 'is', 'Sky']
   str = str[::-1]
   #join list 'blue is sky'
   return " ".join(str).lower()

print(reverseString("Sky is blue"))

# output: blue is sky

# 2. Question: Remove Duplicates from a List
# lst [1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# output [1, 4]

# remove duplicates from list
def removeDuplicates1(lst):
    result = []
    for i in lst:
        # check if element is already in result
        if lst.count(i) == 1: # Keep only the elements that appear once in the list
            result.append(i)
    return result
print(removeDuplicates1([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))

# output: [1, 4]

def removeDuplicates(lst):
    result = []
    for i in lst:
        if lst.count(i) >= 1 and i not in result:
            result.append(i)
    return result

print(removeDuplicates([1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))

# output: [1, 2, 3, 4, 5, 6]

# 3. Question: Count the Occurrences of Each Character in a String
# str1 = "a,a,a,b,b,c,c,c"
# output = a:3, b:2, c:3
def count_characters(s):
    # remove comma and space
    chars = s.replace(",", "")
    result = {}
    for ch in chars:
        result[ch] = result.get(ch, 0) + 1 # count the occurrences of each character

    # generate output
    output = ", ".join([f"{k}:{v}" for k, v in result.items()])
    return output

str1 = "a,a,a,b,b,c,c,c"
print(count_characters(str1))

# output: a:3, b:2, c:3

