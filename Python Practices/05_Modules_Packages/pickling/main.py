# ========================= Pickling =========================
# Pickling is a process of converting a Python object into a byte stream.
# Unpickling is a process of converting a byte stream into a Python object.

import pickle

# Pickling
# with open("data.pkl", "wb") as file:
#     pickle.dump([1, 2, 3, 4, 5], file)

# Unpickling
# with open("data.pkl", "rb") as file:
#     data = pickle.load(file)
#     print(data)

# ========================= Unpickling =========================
# # Unpickling is a process of converting a byte stream into a Python object.


# Pickling
# with open("data.pkl", "wb") as file:
#     pickle.dump([1, 2, 3, 4, 5], file)

# Unpickling
# with open("data.pkl", "rb") as file:
#     data = pickle.load(file)
#     print(data)


import students

student = students.Student("John", 20, "A")
student.display()