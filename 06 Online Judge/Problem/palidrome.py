class Palindrome:
    def str_palindrome(self, text):
        return text == text[::-1]

    def num_palindrome(self, num):
        original = num
        reverse_num = 0

        while num > 0:
            digit = num % 10
            reverse_num = reverse_num * 10 + digit
            num = num // 10

        return original == reverse_num
    
p = Palindrome()

print(p.str_palindrome("madam"))   # True
print(p.str_palindrome("hello"))   # False

print(p.num_palindrome(121))       # True
print(p.num_palindrome(123))       # False
print(p.num_palindrome(1221))      # True