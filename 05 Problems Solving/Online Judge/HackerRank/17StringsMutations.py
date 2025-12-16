def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    string = input()
    position, character = input().split()
    s_new = mutate_string(string, int(position), character)
    print(s_new)
    
# str1 = "Hello World"
# print(str1[:5]) # index 0 to 4
# print(str1[6:]) # index 6 to end
# print(str1[6:10]) # index 6 to 9
# print(str1[6:10:2]) # index 6 to 9 step 2
# print(str1[::-1]) # reverse string
# print(str1[::2]) # step 2

# print(str1[:5] + "Python" + str1[6:]) # index 0 to 4 + "Python" + index 6 to end










