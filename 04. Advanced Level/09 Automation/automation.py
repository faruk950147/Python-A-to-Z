import os
import shutil

"""
| Task                   | Library                     | Example                  |
| ---------------------- | --------------------------- | ------------------------ |
| File/Folder operations | `os`, `shutil`              | move, copy, delete       |
| Web Automation         | `selenium`                  | auto login, form fill    |
| Data process           | `pandas`                    | Excel, CSV process       |
| Web Scraping           | `requests`, `BeautifulSoup` | website data collect     |
| GUI Automation         | `pyautogui`                 | mouse & keyboard control |

Python Automation Libraries List
1. File & OS Automation
Library	Works
os	File/folder list, rename, delete, directory handle
shutil	High-level file/folder operations (copy, move, delete)
pathlib	File paths handle, modern way of os.path
2. Excel & Data Automation
Library	Works
pandas	Excel/CSV process, data manipulation
openpyxl	Excel file read/write (XLSX)
xlrd	Excel file read (XLS old format)
xlsxwriter	Excel file write with formatting
3. Web Automation
Library	Works
selenium	Browser open, auto login, form fill, scrape
requests	HTTP requests, API data fetch
BeautifulSoup	Website data parse, scraping
scrapy	Advanced web scraping, big projects
mechanize	Simple browser automation (form fill)
4. GUI Automation
Library	Works
pyautogui	Mouse/keyboard control, screen automation
keyboard	Keyboard events automation
mouse	Mouse click, move automation
pynput	Mouse & keyboard advanced control
5. Email & Messaging Automation
Library	Works
smtplib	Email send via SMTP
imaplib	Email read via IMAP
twilio	SMS send, WhatsApp messages
yagmail	Gmail automation (send email easily)
6. PDF & Document Automation
Library	Works
PyPDF2	PDF read/write, merge, split
pdfplumber	PDF data extract
docx (python-docx)	Word file automation
reportlab	PDF generate programmatically
7. Task Scheduling & Automation
Library	Works
schedule	Python script schedule (time-based)
time	Delay, sleep, time control
datetime	Date & time handling
8. Image & Screenshot Automation
Library	Works
Pillow	Image manipulation, resize, crop
pyautogui	Screen screenshot, locate image
opencv	Advanced image/video automation
9. Database Automation
Library	Works
sqlite3	SQLite database automation
mysql-connector-python	MySQL database automation
SQLAlchemy	ORM based database automation
10. Extra Useful Libraries
Library	Works
pywhatkit	WhatsApp, YouTube, Google automation
selenium-wire	Selenium + network requests capture
watchdog	File/folder change detection


"""
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
source = os.path.join(BASE_DIR, "source.txt")
destination = os.path.join(BASE_DIR, "destination.txt")

'''
# If destination file already exists, create a new name
if os.path.exists(destination):
    # base = "destination"
    # ext = ".txt"
    base, ext = os.path.splitext(destination)
    counter = 1
    while os.path.exists(f"{base}_{counter}{ext}"):
        counter += 1
    destination = f"{base}_{counter}{ext}"

shutil.copy(source, destination)
print(f"File copied to {destination}")


'''