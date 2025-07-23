# Author: Parentsgeeks
# Made by the community

from pathlib import Path
import shutil
import os
import time

version = "v1.0.0"

# Open window
os.system(f"title SC shader cache dumper - {version}")

# Star Citizen AppData path
base_path = Path.home() / 'AppData' / 'Local' / 'star citizen'

print(f"SC shader cache dumper - {version}\n")
time.sleep(1)
print("Made by the community\n")
time.sleep(1)

# Crashes folder to keep
exclude_folder = 'crashes'

response = input("Do you want to dump the shader cache? (yes [y] / no [n]):").lower()

if response in ['y', 'yes']:
    deleted = 0
    for item in base_path.iterdir():
        if item.name == exclude_folder:
            continue  # Don't delete 'crashes' folder
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()
                print(f"Deleted file: {item.name}")
                deleted += 1
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"Deleted folder: {item.name}")
                deleted += 1
        except Exception as e:
            print(f"Error while dumping {item}: {e}")

    if deleted == 0:
        print("Nothing to dump!")
    else:
        print(f"\nShader cache has been dumped successfully! ({deleted} item(s) deleted)")
        time.sleep(1)
        print("See you in the verse!")
else:
    print("\nOperation canceled.")

input("\nPress 'Enter' to exit the program...")