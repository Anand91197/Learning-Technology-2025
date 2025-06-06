#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
file =  open('update.txt', 'r')
content = file.read()

print(content)
file.close()

#Read Single Line
file =  open('update.txt', 'r')

line = file.readline()
print(line)
file.close()

#Read Multiple Lines
file = open('update.txt', 'r')

lines = file.readlines()
print(lines)
file.close()







