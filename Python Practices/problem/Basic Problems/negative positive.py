def positive_negative(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
    
print(positive_negative(10))

def positive_negative(n):
    if n >= 0:
        if n == 0:
            return "Zero"
        else:
            return "Positive"
    else:
        return "Negative"
    
print(positive_negative(0))

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_odd(10))