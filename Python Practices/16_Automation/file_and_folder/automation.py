"""
Professional File Automation - Modular Style
Features:
- Folder Watcher (Real-time)
- Duplicate Detection
- Daily Backup & Cleanup
- Auto Sync
- Screenshot Capture (Global Hotkey)
- GUI with Tkinter (Manual actions + Logs + Sync Pair)
- Thread-safe logging
"""

import os
import shutil
import hashlib
import threading
import time
from datetime import datetime, timedelta
from zipfile import ZipFile, ZIP_DEFLATED
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import ImageGrab
import keyboard

# ----------------- CONFIG -----------------
CONFIG = {
    "BASE_PATH": r"L:\Programming\Automation",
    "BACKUP_HOUR": 2,
    "BACKUP_MINUTE": 30,
    "ARCHIVE_AFTER_DAYS": 7,
    "OLD_BACKUP_DELETE_DAYS": 30,
    "SYNC_PAIRS": [],
    "HOTKEY": "ctrl+alt+s",
    "BUF_SIZE": 65536
}

# Paths
MAIN_FOLDER = os.path.join(CONFIG["BASE_PATH"], "MainFolder")
PROCESSED_FOLDER = os.path.join(CONFIG["BASE_PATH"], "ProcessedFiles")
ARCHIVE_FOLDER = os.path.join(CONFIG["BASE_PATH"], "Archive")
BACKUP_FOLDER = os.path.join(CONFIG["BASE_PATH"], "Backups")
DUPLICATE_FOLDER = os.path.join(CONFIG["BASE_PATH"], "Duplicates")
SCREENSHOT_FOLDER = os.path.join(CONFIG["BASE_PATH"], "Screenshots")
LOG_FILE = os.path.join(CONFIG["BASE_PATH"], "automation_log.txt")

CONFIG["SYNC_PAIRS"].append((MAIN_FOLDER, os.path.join(CONFIG["BASE_PATH"], "SyncedCopy")))

# ----------------- UTILITIES -----------------
def ensure_dirs():
    for p in [MAIN_FOLDER, PROCESSED_FOLDER, ARCHIVE_FOLDER, BACKUP_FOLDER, DUPLICATE_FOLDER, SCREENSHOT_FOLDER]:
        os.makedirs(p, exist_ok=True)

def log(msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} - {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def file_hash(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                b = f.read(CONFIG["BUF_SIZE"])
                if not b: break
                h.update(b)
    except Exception:
        return None
    return h.hexdigest()

def move_with_unique(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    base = os.path.basename(src)
    name, ext = os.path.splitext(base)
    dest = os.path.join(dest_dir, base)
    counter = 1
    while os.path.exists(dest):
        dest = os.path.join(dest_dir, f"{name}_{counter}{ext}")
        counter += 1
    shutil.move(src, dest)
    return dest

# ----------------- FILE HANDLING -----------------
def is_duplicate(path):
    h = file_hash(path)
    if not h: return False, None
    for folder in [PROCESSED_FOLDER, DUPLICATE_FOLDER]:
        for root, _, files in os.walk(folder):
            for f in files:
                fp = os.path.join(root, f)
                if file_hash(fp) == h:
                    return True, fp
    return False, None

def organize_file(path):
    if not os.path.isfile(path): return
    ext = os.path.splitext(path)[1].lower().strip(".") or "no_extension"
    dest_dir = os.path.join(PROCESSED_FOLDER, ext)
    newpath = move_with_unique(path, dest_dir)
    log(f"Organized {os.path.basename(path)} -> {dest_dir}")
    return newpath

def handle_duplicate(path):
    os.makedirs(DUPLICATE_FOLDER, exist_ok=True)
    newpath = move_with_unique(path, DUPLICATE_FOLDER)
    log(f"Duplicate detected. Moved {os.path.basename(path)} -> {newpath}")

def archive_old_files():
    cutoff = time.time() - CONFIG["ARCHIVE_AFTER_DAYS"] * 86400
    for root, _, files in os.walk(PROCESSED_FOLDER):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.getmtime(fp) < cutoff:
                newpath = move_with_unique(fp, ARCHIVE_FOLDER)
                log(f"Archived old file {f} -> {newpath}")

# ----------------- BACKUP -----------------
def make_daily_backup():
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    zipname = os.path.join(BACKUP_FOLDER, f"processed_backup_{stamp}.zip")
    with ZipFile(zipname, "w", ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(PROCESSED_FOLDER):
            for f in files:
                fp = os.path.join(root, f)
                arcname = os.path.relpath(fp, PROCESSED_FOLDER)
                try: zf.write(fp, arcname)
                except Exception as e: log(f"Backup error {fp}: {e}")
    log(f"Backup created: {zipname}")
    cleanup_old_backups()

def cleanup_old_backups():
    cutoff = time.time() - CONFIG["OLD_BACKUP_DELETE_DAYS"] * 86400
    for f in os.listdir(BACKUP_FOLDER):
        fp = os.path.join(BACKUP_FOLDER, f)
        if os.path.isfile(fp) and os.path.getmtime(fp) < cutoff:
            try: os.remove(fp); log(f"Deleted old backup: {fp}")
            except Exception as e: log(f"Failed to delete backup {fp}: {e}")

def backup_scheduler(stop_event):
    log("Backup scheduler started")
    while not stop_event.is_set():
        now = datetime.now()
        target = now.replace(hour=CONFIG["BACKUP_HOUR"], minute=CONFIG["BACKUP_MINUTE"], second=0, microsecond=0)
        if now > target: target += timedelta(days=1)
        if stop_event.wait(timeout=(target - now).total_seconds()): break
        make_daily_backup()

# ----------------- SYNC -----------------
def sync_once(src, dst):
    os.makedirs(dst, exist_ok=True)
    for root, _, files in os.walk(src):
        rel = os.path.relpath(root, src)
        for f in files:
            srcfp = os.path.join(root, f)
            dst_dir = os.path.join(dst, rel) if rel != "." else dst
            os.makedirs(dst_dir, exist_ok=True)
            dstfp = os.path.join(dst_dir, f)
            try:
                if not os.path.exists(dstfp) or os.path.getmtime(srcfp) > os.path.getmtime(dstfp):
                    shutil.copy2(srcfp, dstfp)
                    log(f"Synced {srcfp} -> {dstfp}")
            except Exception as e: log(f"Sync error {srcfp} -> {dstfp}: {e}")

def sync_scheduler(stop_event, interval=60):
    log("Sync scheduler started")
    while not stop_event.is_set():
        for s,d in CONFIG["SYNC_PAIRS"]:
            try: sync_once(s,d)
            except Exception as e: log(f"Sync pair error {s}->{d}: {e}")
        if stop_event.wait(timeout=interval): break

# ----------------- WATCHER -----------------
class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory: return
        path = event.src_path
        log(f"Detected new file: {path}")
        time.sleep(0.5)
        try:
            dup,_ = is_duplicate(path)
            if dup: handle_duplicate(path)
            else: organize_file(path)
            archive_old_files()
        except Exception as e: log(f"Watcher error {path}: {e}")
    def on_moved(self, event): self.on_created(event)

# ----------------- SCREENSHOT -----------------
def take_screenshot():
    try:
        img = ImageGrab.grab()
        stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        filename = f"screenshot_{stamp}.png"
        dest = os.path.join(SCREENSHOT_FOLDER, filename)
        img.save(dest)
        log(f"Screenshot saved: {dest}")
    except Exception as e: log(f"Screenshot error: {e}")

def hotkey_listener(stop_event):
    keyboard.add_hotkey(CONFIG["HOTKEY"], take_screenshot)
    stop_event.wait()
    keyboard.unhook_all_hotkeys()

# ----------------- GUI -----------------
class AutomationApp:
    def __init__(self, root):
        self.root = root
        root.title("File Automation")
        root.geometry("800x500")
        self.observer = None
        self.stop_event = threading.Event()
        self.threads = []

        # Buttons
        frm = tk.Frame(root); frm.pack(fill=tk.X, padx=5,pady=5)
        tk.Button(frm,text="Start Watcher",command=self.start_watcher).pack(side=tk.LEFT,padx=3)
        tk.Button(frm,text="Stop Watcher",command=self.stop_watcher).pack(side=tk.LEFT,padx=3)
        tk.Button(frm,text="Manual Organize",command=self.manual_organize).pack(side=tk.LEFT,padx=3)
        tk.Button(frm,text="Archive Old Files",command=self.manual_archive).pack(side=tk.LEFT,padx=3)
        tk.Button(frm,text="Take Screenshot",command=take_screenshot).pack(side=tk.LEFT,padx=3)
        tk.Button(frm,text="Manual Backup",command=lambda: threading.Thread(target=make_daily_backup).start()).pack(side=tk.LEFT,padx=3)

        # Log viewer
        self.logbox = scrolledtext.ScrolledText(root,state='disabled'); self.logbox.pack(fill=tk.BOTH,expand=True,padx=5,pady=5)
        self.periodic_refresh()

    def periodic_refresh(self):
        try:
            if os.path.exists(LOG_FILE):
                with open(LOG_FILE,'r',encoding='utf-8') as f:
                    data=f.read()
                    self.logbox.config(state='normal')
                    self.logbox.delete('1.0',tk.END)
                    self.logbox.insert(tk.END,data[-20000:])
                    self.logbox.config(state='disabled')
        except: pass
        self.root.after(2000,self.periodic_refresh)

    def start_watcher(self):
        if self.observer and self.observer.is_alive(): messagebox.showinfo("Info","Watcher already running"); return
        ensure_dirs()
        event_handler = WatcherHandler()
        observer = Observer()
        observer.schedule(event_handler,MAIN_FOLDER,recursive=True)
        observer.daemon=True; observer.start()
        self.observer=observer
        log("Watcher started")

        self.stop_event.clear()
        t1=threading.Thread(target=backup_scheduler,args=(self.stop_event,),daemon=True)
        t2=threading.Thread(target=sync_scheduler,args=(self.stop_event,),daemon=True)
        t3=threading.Thread(target=hotkey_listener,args=(self.stop_event,),daemon=True)
        t1.start(); t2.start(); t3.start()
        self.threads.extend([t1,t2,t3])
        messagebox.showinfo("Info","Watcher & background services started")

    def stop_watcher(self):
        if self.observer: self.observer.stop(); self.observer.join(timeout=3); self.observer=None
        self.stop_event.set()
        time.sleep(0.5)
        log("Watcher stopped and background threads signaled to stop")
        messagebox.showinfo("Info","Stopped watcher & background services")

    def manual_organize(self):
        for root,_,files in os.walk(MAIN_FOLDER):
            for f in files:
                fp=os.path.join(root,f)
                try:
                    dup,_ = is_duplicate(fp)
                    if dup: handle_duplicate(fp)
                    else: organize_file(fp)
                except Exception as e: log(f"Manual organize error {fp}: {e}")
        messagebox.showinfo("Info","Manual organize completed")

    def manual_archive(self):
        archive_old_files(); messagebox.showinfo("Info","Archived old files (if any)")

# ----------------- MAIN -----------------
def main():
    ensure_dirs()
    # sample file
    sample=os.path.join(MAIN_FOLDER,"example.txt")
    if not os.path.exists(sample):
        with open(sample,"w",encoding="utf-8") as f: f.write("Auto-created example file\n")
        log(f"Sample file created: {sample}")

    root=tk.Tk()
    app=AutomationApp(root)
    root.protocol("WM_DELETE_WINDOW",lambda: [app.stop_watcher(), root.destroy()])
    root.mainloop()

if __name__=="__main__":
    main()
