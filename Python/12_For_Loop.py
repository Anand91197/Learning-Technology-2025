#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["Apple", "Banana", "Cherry"]
for i in fruits:
    print(i)



number = [1,2,3,4,5,6,7]
for i in number:
    print(i)



#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

#The range() function generates a sequence of numbers.
for i in range(5):
    print(i)

for x in range(2, 6):
  print(x)  

#range() with Start, Stop, Step
for i in range(1, 10, 2):  # From 1 to 9, stepping by 2
    print(i)


#Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")



#break: Stops the loop entirely.
#continue: Skips the current iteration and jumps to the next one.

#With the break statement we can stop the loop before it has looped through all the items:


for i in range(10):
    if i == 5:
        break  # Stop the loop if i is 5
    print(i)

        
#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break 
  

for y in range(4):
   print(y)
   if y == 2:
      break   
  

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
for i in range(10):
    if i == 5:
        continue  
    print(i)
    
#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#The else block executes after the loop finishes normally  
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#If the loop breaks, the else block is not executed.
