#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


#Print Star with Increasing format
for i in range(0,10):   Outer loop (controls the number of rows)
  for j in range(0,i+1): Inner loop (controls the number of stars in each row)
      print("*", end="") #The end parameter (end=' ') indicates that the end character has to be identified by whitespace
  print("\r")   #return, Python to move the cursor back to the beginning of the current line
    


#Print Number
a = 1
for i in range(0,5):    #Controls the number of rows
  for j in range(0,i+1): #Controls the number of items printed per row.
      print(a, end=" ")
      a+=1 # a = a+1
  print("\r")


## Initialize the list
weekdays = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursday","Friday", "Saturday"]
print("Seven Weekdays are:\n")
# Iterate the list using for loop
for day in range(len(weekdays)):        #range(len(weekdays)) creates a sequence of numbers from 0 to 6 
  print(weekdays[day])
  
