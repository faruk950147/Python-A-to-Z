import numpy as np

# -----------------------------------
# eye() function
# -----------------------------------
# তির্যক (Diagonal) কী?

# তির্যক মানে হলো কোণা থেকে কোণায় সোজা কাটা লাইন।

# ম্যাট্রিক্সে তির্যক দুই ধরনের হয়:

# Principal Diagonal (মূল তির্যক) → উপর-বাম থেকে নিচ-ডানে (↘️)

# Secondary Diagonal (অন্য তির্যক) → উপর-ডান থেকে নিচ-বামে (↙️)

# eye() একটি identity matrix তৈরি করে
# Identity matrix হলো এমন square matrix
# যেখানে প্রধান তির্যক (principal diagonal) এ 1 থাকে
# এবং বাকি সব জায়গায় 0 থাকে

# identity_matrix = np.eye(5)
# print("Identity Matrix:")
# print(identity_matrix)


# -----------------------------------
# diag() function (Matrix দিলে)
# -----------------------------------
# তির্যক (Diagonal) কী?

# তির্যক মানে হলো কোণা থেকে কোণায় সোজা কাটা লাইন।

# ম্যাট্রিক্সে তির্যক দুই ধরনের হয়:

# Principal Diagonal (মূল তির্যক) → উপর-বাম থেকে নিচ-ডানে (↘️)

# Secondary Diagonal (অন্য তির্যক) → উপর-ডান থেকে নিচ-বামে (↙️)

# যদি diag() এ একটি matrix দেই
# তাহলে এটি শুধু principal diagonal বের করে দেয়
# অর্থাৎ একটি 1D array রিটার্ন করে

# diagonal_from_matrix = np.diag(identity_matrix)
# print("\nDiagonal extracted from Identity Matrix:")
# print(diagonal_from_matrix)


# -----------------------------------
# diag() function (Array দিলে)
# -----------------------------------
# যদি diag() এ একটি 1D array দেই
# তাহলে এটি একটি diagonal matrix তৈরি করে

# array_values = [5, 6, 7, 8, 9]
# diagonal_matrix = np.diag(array_values)

# print("\nDiagonal Matrix from Array:")
# print(diagonal_matrix)

# এখানে প্রধান তির্যক (principal diagonal) এ 1 থাকে
# diagonal_matrix = np.diag(array_values, k=1)
# print("\nDiagonal Matrix from Array with k=1:")
# print(diagonal_matrix)

# vander() is a function that returns a Vandermonde matrix. 
# A Vandermonde matrix is a matrix with the terms of a set of polynomials as its elements. 
# It is named after the French mathematician Alexandre-Théodore Vandermonde. 
# power হলো কোন সংখ্যাটি কতবার পূর্ণ করা হবে
# কারণ Polynomial বানাতে power লাগে (x², x³, x⁴...)

vander_matrix = np.vander([4, 5])
print("\nVandermonde Matrix:")
print(vander_matrix)

vander_matrix = np.vander([1, 2])
print("\nVandermonde Matrix:")
print(vander_matrix)