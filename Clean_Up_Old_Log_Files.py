import os
import shutil

files=os.listdir(".")

log_folder="Old Logs"

# This script moves all log files (.log) from the current directory to a folder named "Old Logs".
# If the folder does not exist, it creates the folder first.
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
    print(f"Created '{log_folder}' folder.")

try:
    for file in files:
        if file.lower().endswith(".log"):
            mtime=os.path.getmtime(file)
            from datetime import datetime,timedelta
            file_time=datetime.fromtimestamp(mtime)
            cutoff = datetime.now() -timedelta(days=7)
            if file_time<cutoff:
                shutil.move(file,os.path.join(log_folder,file))
                print(f"Moved {file} - older than 7 days.")
            else:
                print(f"Skipping {file} - not older than 7 days.")

    print(f"All log files older than 7 days have been moved to the '{log_folder}' folder.")
    
except Exception as e:
    print(f"Error: {e}")