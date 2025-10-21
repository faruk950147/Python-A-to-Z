# zip() return a zip object and it is an iterator 
# that is why we need to convert it to a list
# accept arguments two or more iterable objects


student = ['Faruk', 'Rahat', 'Rifat']
marks = [80, 90, 100]
zip_object = zip(student, marks)
# for i in zip_object:
#     print(i)

# print(list(zip_object))
# print(tuple(zip_object))
# print(set(zip_object))
# print(dict(zip_object))
# print(str(zip_object))

# Unzipping
zip_object = zip(student, marks)
unzip1, unzip2 = zip(*zip_object)
print(unzip1)
print(unzip2)