# palindrome list in using for loop and string reverse
def palindromeList(list1):
    for i in range(len(list1)):
        if list1[i] == list1[i][::-1]:
            print(list1[i])

palindromeList(["madam", "racecar", "python", "level"])

# palindrome list in using copy (copy())
def palindromeList(list1):
    list2 = list1.copy()
    for i in range(len(list2)):
        if list2[i] == list2[i][::-1]:
            return list2[i]
        else:
            return 'No Palindrome Found'

palindromeList(["madam", "racecar", "python", "level"])


