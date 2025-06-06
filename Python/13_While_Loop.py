#With the while loop we can execute a set of statements as long as a condition is true.

#Simple while Loop
count = 1

while count <= 5:
    print(count)
    count += 1


count = 0
while count < 5:
    print(count)
    count += 1 #count = count +1

i =1
while i < 5:
    print(i)
    i +=1 

#With the break statement we can stop the loop even if the while condition is true:
#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#With the continue statement, we can stop the current iteration, and continue with the next:
#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)  
