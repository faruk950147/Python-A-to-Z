'''
এটা কী করছে?

এই কোডটা দেখাচ্ছে:

1. Integer (immutable) কিভাবে কাজ করে
a = 10
a = a + 20

এখানে প্রতিবার:

নতুন value তৈরি হয়
পুরানোটা change হয় না

তাই id() বদলে যায়

2. আরেকটা integer
b = 10
b += 20

এটাও একই:

নতুন object তৈরি হয়
id change হয়
3. List (mutable) কিভাবে কাজ করে
a = [1, 2, 3]
Case 1:
a = a + [4, 5, 6]

নতুন list তৈরি হয় → id change

Case 2:
a += [4, 5, 6]

আগের list-এর ভিতরেই update হয় → id same থাকে

এক লাইনে উত্তর:

এটা একটা Python practice code যা দেখায়:
কখন নতুন object তৈরি হয় আর কখন same object modify হয়

'''

# =================== memory address deference ===================
# always create new object and assign to a
a = 10
print('Value of a first line:', a)
print('ID of a first line:', id(a))

# create new object and assign to a
a = a + 20  
print('Value of a second line:', a)
print('ID of a second line:', id(a))

# create new object and assign to b
# immutable object
b = 10  
print('Value of b third line:', b)
print('ID of b third line:', id(b))

# create new object and assign to b
# immutable object
b += 20  
print('Value of b fourth line:', b)
print('ID of b fourth line:', id(b))

# =================== list (mutable vs immutable behavior) ===================
a = [1, 2, 3]
print('Value of a list:', a)
print('ID of a list:', id(a))

# always create new object and assign to a
a = a + [4, 5, 6]  
print('Value of a list:', a)
print('ID of a list:', id(a))

# modify same object (mutable behavior)
a += [4, 5, 6]
print('Value of a list:', a)
print('ID of a list:', id(a))