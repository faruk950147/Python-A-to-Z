# 1. Question: Reverse a String
# input "Sky is blue"
# output "blue is sky"

def reverseString(str):
    #split return list 
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

# 4. Question: Find the Longest Common Prefix
# strs = ["flower", "flow", "flight"]
# output = "fl"
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # sort the list to make comparison easier
    strs.sort()
    
    # compare first and last strings
    first = strs[0]
    last = strs[-1]
    
    # find the common prefix
    for i in range(len(first)):
        if i >= len(last) or first[i] != last[i]:
            return first[:i]
    
    return first

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

# output: fl
