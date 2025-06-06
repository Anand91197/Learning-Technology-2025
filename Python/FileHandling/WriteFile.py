#"a" - Append - will append to the end of the file
file = open('update.txt', 'a')
content = file.write("I've five years of experience")
file.close()

file = open("update.txt", "r") #open and read the file after the appending
print(content)


#"w" - Write - will overwrite any existing content
file = open('update.txt', 'w')
content = file.write('Woops! I have deleted the content!')
file.close()

file = open('update.txt', 'r') #open and read the file after the overwriting
print(content)