#Basic
'''
import os

folders = input("Please provide list of the folders names: ").split()

for folder in folders:
    files = os.listdir(folder)

print("===Listing files for the folder:- ")  

for file in files:
    print(file)
    '''


#Advanced

import os

folders = input("Please provide list of the folders names: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Please provide a valid folder name, looks like this folder doesn't exist: {folder}")
        continue  # Continue to the next folder instead of breaking the loop
    except PermissionError:
        print(f"Permission denied. Cannot access the folder: {folder}")
        continue  # Continue to the next folder instead of breaking the loop

    print(f"=== Listing files for the folder: {folder} ===")
    for file in files:
        print(file)
    


## Advance level with Function:
import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
    
