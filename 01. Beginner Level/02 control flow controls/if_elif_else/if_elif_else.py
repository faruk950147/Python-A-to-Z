# ================ if else Simple decision making =================== 
"""
             ┌───────────────┐
             │   Start        │
             └───────┬───────┘
                     │
              ┌──────▼───────┐
              │  x == 20 ?   │
              └───┬─────┬────┘
                  │Yes  │No
       ┌──────────┘     │
       │                ▼
  "x is exactly     ┌──────────────┐
        20"         │  x > 20 ?    │
                    └───┬─────┬────┘
                        │Yes  │No
          ┌─────────────┘     ▼
          │              ┌──────────────┐
    "x is greater        │  x < 20 ?    │
        than 20"         └───┬─────┬────┘
                             │Yes  │No
                 ┌───────────┘     ▼
                 │             "x is not 20"
           "x is less than 20"


"""
print("================ Simple decision making ===================")
x = 15

if x == 20:
    print("x is exactly 20")
else:
    print("x is not 20")
    
print("================ elif decision making ===================")
# ================ if elif else Simple decision making =================== 
x = 15

if x == 20:
    print("x is exactly 20")
elif x > 20:
    print("x is greater than 20")
else:
    print("x is not 20")
    
print("================ elif advanced decision making ===================")
# ================ if elif else advanced decision making =================== 
x = 15

if x == 20:
    print("x is exactly 20")
elif x > 20:
    print("x is greater than 20")
elif x < 20:
    print("x is less than 20")
else:
    print("x is not 20")
    
print("================ elif nested decision making ===================")
    
#  ================ if elif else nested decision making =================== 

"""
             ┌───────────────┐
             │     Start      │
             └───────┬───────┘
                     │
              ┌──────▼────────┐
              │  x > 10 ?     │
              └───┬─────┬─────┘
                  │Yes  │No
       ┌──────────┘     │
       │                │
 "x is greater          │
   than 10"             │
       │                │
       ▼                ▼
 ┌───────────────┐   "x is 10 or less"
 │   y > 0 ?     │
 └───┬─────┬─────┘
     │Yes  │No
     │     │
 "y is    "y is zero
positive"  or negative"


"""
x = 15
y = 5
print("================ nested decision making ===================")
# first condition is True so it will check second condition
if x > 10:
    print("x is greater than 10")
    if y > 0:
        print("y is positive")
    else:
        print("y is zero or negative")
else:
    print("x is 10 or less")
# first condition is False so it will not check second condition just skip it and go to else
if x == 10:
    print("x is greater than 10")
    if y > 0:
        print("y is positive")
    else:
        print("y is zero or negative")
else:
    print("x is 10 or less")

