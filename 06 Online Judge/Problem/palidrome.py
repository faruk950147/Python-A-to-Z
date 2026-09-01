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


"""
    This program checks if a given string is a palindrome using recursion. A palindrome is a word, 
    phrase, number, or other sequence of characters that reads the same forward and backward 
    (ignoring spaces, punctuation, and capitalization). efficiently.
    Logic:
    1. Define a recursive function that takes a string and two pointers (left and right).
    2. If the left pointer is greater than or equal to the right pointer, return True (base case).
    3. If the characters at the left and right pointers are not equal, return False.
    4. Move the left pointer one step to the right and the right pointer one step to the left,
    and call the function recursively.
    5. Before comparing characters, convert them to lowercase and ignore non-alphanumeric characters.
    O(n) time complexity and O(n) space complexity due to recursion stack.
"""
def is_palindrome(s, left=0, right=None):
    # Preprocess the string: remove non-alphanumeric characters and convert to lowercase.
    s = ''.join(filter(str.isalnum, s)).lower()

    # Set right pointer to the last index if not provided.
    if right is None:
        right = len(s) - 1

    # Base case: stop when pointers meet or cross.
    if left >= right:
        return True

    # Check if characters at left and right pointers are equal.
    if s[left] != s[right]:
        return False

    # Recursive call: move both pointers inward.
    return is_palindrome(s, left + 1, right - 1)

if __name__ == "__main__":
    if is_palindrome("Madam, I'm Adam"):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
        
"""
This program checks if a given string is a palindrome using recursion. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward 
(ignoring spaces, punctuation, and capitalization). less efficiently.
Logic:
1. Preprocess the string to remove non-alphanumeric characters and convert it to lowercase.
2. If the string is empty or has one character, return True (base case).
3. If the first and last characters of the string are not equal, return False.
4. Recursively check the substring that excludes the first and last characters.
O(n^2) time complexity and O(n^2) space complexity due to string slicing and recursion stack.

"""
def is_palindrome(s):
    # Preprocess the string: remove non-alphanumeric characters and convert to lowercase.
    s = ''.join(filter(str.isalnum, s)).lower()

    # Base case: stop recursion when the string is empty or has one character.
    if len(s) <= 1:
        return True

    # Check if the first and last characters are equal.
    if s[0] != s[-1]:
        return False

    # Recursive case: check the substring excluding the first and last characters.
    return is_palindrome(s[1:-1])