import csv
# ===================== what is csv file =====================
# csv (Comma Separated Values) is a simple file format used for tabular data, 
# where values are separated by commas. It's often used for data exchange between 
# different applications and systems.

# ============================= CREATE & WRITE CSV FILE =============================
import os
# 'w' mode means create a new file (overwrite if it already exists)
if os.path.exists('data.csv'):
    os.remove('data.csv')
else:
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Header row
    writer.writerow(['Name', 'Age', 'City'])
    # Data rows
    writer.writerow(['John Doe', 30, 'New York'])
    writer.writerow(['Jane Smith', 25, 'Los Angeles'])

print("data.csv file created and written successfully!")


# ============================= APPEND TO CSV FILE =============================
# 'a' mode means append data at the end of the file
with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Alice Brown', 28, 'Chicago'])
    writer.writerow(['Michael Lee', 35, 'Houston'])

print("New data appended to CSV file!")


# ============================= READ CSV FILE =============================
# Now read the CSV file and display its contents
with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    print("\nContents of data.csv:")
    for row in reader:
        print(row)
