import os
import shutil

image_folder= "Images"
# This script moves all image files (.jpg, .png) from the current directory to a folder named "Images".
# If the folder does not exist, it creates the folder first.
# It also prints a message for each file moved or skipped.

files=os.listdir(".")
try:
    if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            print(f"Created '{image_folder}' folder.")

    for file in files:
        if file.lower().endswith((".jpg","png")):
            shutil.move(file,image_folder+"/"+file)
            print(f"Moved {file} to '{image_folder}' folder.")
        else:
            print(f"Skipping {file}, not an image file.")
    print(f"All image files have been moved to the '{image_folder}' folder.")

except Exception as e:
    print(f"Error: {e}")