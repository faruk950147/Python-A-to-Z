# ============================ what is nested if-else ============================
# nested if-else is a if-else statement inside another if-else statement
# it is used when we have to check multiple conditions

# ============================ rules ============================
# 1. first check the outer if condition
# 2. if the outer if condition is true, then check the inner if condition
# 3. if the inner if condition is true, then execute the inner if block
# 4. if the inner if condition is false, then execute the inner else block
# 5. if the outer if condition is false, then execute the outer else block

# ============================ how to use nested if-else ============================
# if condition:
#     if condition:
#         pass
#     else:
#        pass
# else:
#     pass

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")


a = 10
b = 20

if a < b:
    if a == b:
        print("a is equal to b")
    else:
        print("a is not equal to b")
else:
    print("a is not less than b")
    
    
# if condition:
#     if condition:
#         pass
#     else:
#         pass
# else:
#     if condition:
#         pass
#     else:
#         pass

    