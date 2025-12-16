# ===================== what is csv file =====================
# csv (Comma Separated Values) is a simple file format used for tabular data, 
# where values are separated by commas. It's often used for data exchange between 
# different applications and systems.

# ============================= CREATE & WRITE CSV FILE =============================
import os
import csv

# 'w' mode means create a new file (overwrite if it already exists)
file_name = 'data.csv'

# if file already exists, delete it
if os.path.exists(file_name):
    os.remove(file_name)

# create and write to CSV file
with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow(['Name', 'Age', 'City'])

    # Data rows
    writer.writerow(['John Doe', 30, 'New York'])
    writer.writerow(['Jane Smith', 25, 'Los Angeles'])
    writer.writerow(['Alex Brown', 28, 'Chicago'])

print("data.csv file created and written successfully!")


# ============================= APPEND TO CSV FILE =============================
# 'a' mode means append data at the end of the file
with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Alice Brown', 28, 'Chicago'])
    writer.writerow(['Michael Lee', 35, 'Houston'])

print("New data appended to CSV file!")


# ============================= READ CSV FILE =============================
# Now read the CSV file and display its contents
with open(file_name, 'r', newline='') as file:
    reader = csv.reader(file)
    print("\nContents of data.csv:")
    for row in reader:
        print(row)
