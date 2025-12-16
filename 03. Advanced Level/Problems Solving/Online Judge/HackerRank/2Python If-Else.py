# The code checks if a number is "Weird" or "Not Weird" based on the given conditions.
# It uses the modulo operator to determine if the number is odd or even and checks the specified ranges.
# The function prints the result directly based on the conditions.
# The code is structured to be run as a script, taking input from the user and calling the function to check the number.
"""
    
    
        def check_weird(n):
            ## Check if the number is odd or even and print the corresponding result
            # based on the specified conditions.
            
            if n % 2 == 1: 
                print("Weird")
            # already checked if n is odd, so we can check for even numbers now right now all even numbers here not odd numbers
            elif 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            else:
                print("Not Weird")
                
        if __name__ == '__main__':
            n = int(input())  # getting input from user
            check_weird(n)  # function calling
    
    """


    
def check_weird(n):
    if n % 2 != 0:  # if number is odd
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:  # if number is even and between 2 is smaller than n and n is smaller than 5
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:  # if number is even and between 6 is smaller than n and n is smaller than 20 
        print("Weird")
    else:
        print("Not Weird")  # if number is even and greater than 20
        
if __name__ == '__main__':
    n = int(input())  # getting input from user
    check_weird(n)  # function calling
    
    
    
    
    
    