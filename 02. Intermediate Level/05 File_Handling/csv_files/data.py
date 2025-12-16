import csv
import os
import shutil

# ==============================
# ১. Data-level operations
# ==============================

# Sample CSV file
csv_file = "sample.csv"

# --- Write ---
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age"])
    writer.writerow([1, "Faruk", 25])
    writer.writerow([2, "Rahim", 30])

# --- Read ---
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("Read:", row)

# --- Append ---
with open(csv_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3, "Karim", 28])

# --- Update (read → modify → write) ---
rows = []
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    rows = list(reader)

# Update Age of ID 2
for row in rows:
    if row[0] == "2":
        row[2] = "31"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# --- Delete (read → remove → write) ---
rows = []
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    rows = list(reader)

# Remove row with ID 1
rows = [row for row in rows if row[0] != "1"]

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# ==============================
# ২. File-level operations
# ==============================

# --- Move ---
shutil.move("sample.csv", "moved_sample.csv")

# --- Copy ---
shutil.copy("moved_sample.csv", "copied_sample.csv")

# --- Rename ---
os.rename("copied_sample.csv", "renamed_sample.csv")

# --- Delete ---
os.remove("moved_sample.csv")
os.remove("renamed_sample.csv")
