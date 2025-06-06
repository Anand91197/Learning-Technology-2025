
#"x" - Create - will create a file, returns an error if the file exists
file = open('Newfile.txt', 'x')


#Write a content in the file
file = open('Newfile.txt', 'w')
content = file.write("Hello World..!")
print(content)
file.close()


#"a" - Append - will append to the end of the file
file = open('Newfile.txt', 'a')
content = file.write("I'm Anand Saini")
file.close()

file = open("Newfile.txt", "r") #open and read the file after the appending
print(content)


#"w" - Write - will overwrite any existing content
file = open('Newfile.txt', 'w')
content = file.write('Woops! I have deleted the content!')
file.close()

file = open('Newfile.txt', 'r') #open and read the file after the overwriting
print(content)


#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
file =  open('Newfile.txt', 'r')
content = file.read()

print(content)
file.close()

#Read Single Line
file =  open('Newfile.txt', 'r')

line = file.readline()
print(line)
file.close()

#Read Multiple Lines
file = open('Newfile.txt', 'r')

lines = file.readlines()
print(lines)
file.close()

#Check File Availabilty
import os
import os.path

a= os.path.exists('Newfile.txt')
print('The file Newfile.txt is present: ', a)

#Delete File
import os
import os.path

os.remove('Newfile.txt')
a = os.listdir('.')
print(a)


print("******")

#Create a folder/Dirctory

import os

os.mkdir('Test_Folder')
a = os.listdir('.')
print(a)

#The os.path.join() function is used to combine directory and file paths in a way that works across different operating systems.
#Create a file in the existing folder
import os

folder_path = "Test_Folder"  # Replace with your actual folder name
file_name = "file_1.txt"  # Name of the file to create
file_content = "I'm learning a python programming..!!"

# Ensure the folder exists before creating the file
if os.path.exists(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Open the file in write mode and write content
    with open(file_path, "w") as file:
        file.write(file_content)
    
    print(f"File '{file_name}' has been created in '{folder_path}' and content has been written.")
else:
    print(f"Error: The folder '{folder_path}' does not exist. Please provide a valid folder.")


# Creating a File in a Specific Folder
import os

folder = "My_Folder"
file_name = "notes.txt"

# Ensure the folder exists
if not os.path.exists(folder):
    os.mkdir(folder)

# Create and write to the file
file_path = os.path.join(folder, file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.")

print(f"File created at: {file_path}")


#Delete Folder
#Delete the Empty Folder

import os
import os.path

os.rmdir('Folder1')

#Delete all the files with folder which contains in the folder

import os
import os.path
import shutil  

shutil.rmtree('TestingFolder')


#The shutil module in Python provides high-level file operations such as copying, moving, renaming, and deleting files and directories. It is built-in, so no installation is required.
import shutil

shutil.copy("source.txt", "destination.txt")

#Copies a file with metadata (timestamps, permissions, etc.).
shutil.copy2("source.txt", "destination.txt")

#Copies an entire folder (including subfolders and files).
shutil.copytree("source_folder", "destination_folder")


#Moves a file or folder to a new location (renaming if needed).
shutil.move("file.txt", "new_folder/file.txt")
