def print_list(lst):
    if len(lst) == 0: # Base case
        return
    print(lst[0]) # Recursive case
    print_list(lst[1:]) # Recursive call

print_list([1, 2, 3, 4, 5])

def print_list(lst, idx):
    if idx == len(lst): # Base case
        return
    print_list(lst, idx + 1) # Recursive call
    print(lst[idx]) # Recursive case