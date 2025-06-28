import os 
# This script renames all .txt files in the current directory to have a prefix "Archived_"
# and then lists all files that start with "Archived_" and end with ".txt".
files=os.listdir(".")

for file in files:
    if file.lower().endswith(".txt"):
        os.rename(file,f"Archived_{file}")
        
files=os.listdir(".")

for file in files:
    if file.lower().startswith("archived_") and file.lower().endswith(".txt"):
        print(file)
