count = 0 
for num in range(1000, 0, -2):  # 1000 to 2 (odd numbers)
    print(num, end="\t")  # print number with tab
    count += 1
    
    if count % 5 == 0:  # print new line after 5 numbers
        print()
   
   
        
N = int(input("Enter a number (N): "))  # user input
count = 0  # count for 5 numbers per line
# N to 2 (odd numbers)
for num in range(N if N % 2 == 0 else N - 1, 1, -2):  
    print(num, end="\t")  # print number with tab
    count += 1
    
    if count % 5 == 0:  # print new line after 5 numbers
        print()
