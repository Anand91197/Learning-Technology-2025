#Taking User Input
user_input = int(input("Enter a number: "))

#Checking if the number is even or odd
if user_input % 2 == 0:
    print(f"{user_input} is an even number")
else:
    print(f"{user_input} is an odd number")    

#Using a For Loop print number from 1 to user_input 
print("Number from 1 to", user_input)
for i in range(1, user_input +1):
    print(i)    