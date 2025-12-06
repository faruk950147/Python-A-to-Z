def rev_str(word):
    rev_string = ''
    for char in word: 
        # every time new char add in front
        rev_string = char + rev_string  
        # 1 y rev_string = 'y' + '' = y
        # 2 o rev_string = 'o' + 'y' = oy
        # 3 u rev_string = 'u' + 'oy' = uoy
        
        print(f"{char} is char add new rev string in {rev_string}")
    return rev_string

print(rev_str("you"))

def rev_str2(word):
    return word[::-1]

print(rev_str2("you"))