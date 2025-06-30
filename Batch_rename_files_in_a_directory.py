import os

# List all files in the current directory
files = os.listdir(".")
counter = 1

print("Renaming files....")
print("Current directory:", os.getcwd())

for file in files:
    if file.endswith(".txt"):
        new_name = f"archived_{counter}.txt"
        os.rename(file, new_name)
        print(f"File {file} has been renamed to {new_name}")
        counter += 1
