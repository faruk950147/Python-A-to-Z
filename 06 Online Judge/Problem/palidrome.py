class Palindrome:
    """
    A class for checking whether strings and numbers are palindromes.

    A palindrome is a word or number that remains the same
    when reversed.
    """

    def str_palindrome(self, text):
        """
        Check if a string is a palindrome.

        Logic:
        - Reverse the string using slicing.
        - Compare the original string with the reversed string.

        Args:
            text (str): The string to check.

        Returns:
            bool: True if the string is a palindrome,
                  False otherwise.
        """
        return text == text[::-1]

    def num_palindrome(self, num):
        """
        Check if a number is a palindrome.

        Logic:
        - Store the original number.
        - Reverse the number digit by digit.
        - Compare the original number with the reversed number.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is a palindrome,
                    False otherwise.
        reverse = reverse * 10 + digit
        Example:
        n = 1234
        
        Extract LSM 4 then 3 then 2 then 1
        Initial:
        reverse = 0

        Get 4:
        0 * 10 + 4 = 4

        Get 3:
        4 * 10 + 3 = 43

        Get 2:
        43 * 10 + 2 = 432

        Get 1:
        432 * 10 + 1 = 4321
        
        """
        original = num
        reverse_num = 0

        while num > 0:
            # Get the last digit
            digit = num % 10

            # Add the digit to the reversed number
            reverse_num = reverse_num * 10 + digit

            # Remove the last digit from the number
            num //= 10

        # Compare original number with reversed number
        return original == reverse_num


p = Palindrome()

print(p.str_palindrome("madam"))   # True
print(p.str_palindrome("hello"))   # False

print(p.num_palindrome(121))       # True
print(p.num_palindrome(123))       # False
print(p.num_palindrome(1221))      # True