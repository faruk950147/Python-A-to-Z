# ===============================
# Full File & Folder Automation
# (Ready for Production)
# ===============================

import os
import shutil
from datetime import datetime

# ===============================
# Base Paths
# ===============================
BASE_PATH = r"L:\Programming\Programming\All-Main-Problem-Solving\Python-A-to-Z\Python Practices\16_Automation\file_and_folder"

base_folder = os.path.join(BASE_PATH, "MainFolder")
destination_folder = os.path.join(BASE_PATH, "ProcessedFiles")
archive_folder = os.path.join(BASE_PATH, "Archive")
log_file = os.path.join(BASE_PATH, "log.txt")

# ===============================
# Logger
# ===============================
def log(msg):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")
    print(msg)

# ===============================
# Create folders if not exist
# ===============================
for folder in [base_folder, destination_folder, archive_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        log(f"Created folder: {folder}")

# ===============================
# Create new file with duplicate handling
# ===============================
file_name = "example.txt"
file_path = os.path.join(base_folder, file_name)

counter = 1
while os.path.exists(file_path):
    name, ext = os.path.splitext(file_name)
    file_path = os.path.join(base_folder, f"{name}_{counter}{ext}")
    counter += 1

with open(file_path, "w") as f:
    f.write("Hello! This file was created automatically.\n")
log(f"File created: {file_path}")

# ===============================
# Move file to destination folder
# ===============================
shutil.move(file_path, destination_folder)
log(f"File moved to destination: {destination_folder}")

# ===============================
# Organize files by extension
# ===============================
for file in os.listdir(destination_folder):
    full_path = os.path.join(destination_folder, file)

    if os.path.isfile(full_path):
        ext = os.path.splitext(file)[1][1:]
        if ext == "":
            ext = "no_extension"

        ext_folder = os.path.join(destination_folder, ext)

        if not os.path.exists(ext_folder):
            os.makedirs(ext_folder)

        shutil.move(full_path, ext_folder)
        log(f"Organized {file} into folder: {ext_folder}")

# ===============================
# Archive old files (older than 7 days)
# ===============================
for root, dirs, files in os.walk(destination_folder):
    for file in files:
        file_path = os.path.join(root, file)
        modified_time = os.path.getmtime(file_path)
        file_age_days = (datetime.now().timestamp() - modified_time) / (3600 * 24)

        if file_age_days > 7:
            shutil.move(file_path, archive_folder)
            log(f"Archived old file: {file}")

log("Automation completed successfully.")
