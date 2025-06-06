#"x" - Create - will create a file, returns an error if the file exists
file = open('Newfile.txt', 'x')


#Write a content in the file
file = open('Newfile.txt', 'w')
content = file.write("Hello World..!")
print(content)
file.close()