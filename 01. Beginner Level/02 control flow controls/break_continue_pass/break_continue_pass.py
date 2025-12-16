# break is used to exit the loop
# continue is used to skip the current iteration
# pass is used to do nothing
# ============= break =================== 
i = 0
while i < 10:
    print("I am a loop")
    i += 1
    break
# output:
# I am a loop

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
# output:
# 0
# 1
# 2
# 3
# 4

# ================ break =================== 
for i in range(10):
    if i == 5:
        break
    print(i)
# output:
# 0
# 1
# 2
# 3
# 4
# ================ continue =================== 
for i in range(10):
    if i == 5:
        continue
    print(i)
# output:
# 0
# 1
# 2
# 3
# 4
# ================ pass =================== 
for i in range(10):
    if i == 5:
        pass
    print(i)
# output:
# 0
# 1
# 2
# 3
# 4