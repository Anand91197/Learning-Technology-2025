import mymodule  # Import the entire module

# Calling functions from the module using dot notation
message = mymodule.greet("Alice")
result = mymodule.add(5, 3)

print(message)  
print(result)   

#You can import specific functions or variables from a module.
from mymodule import greet, add  # Importing specific functions

print(greet("Bob"))      
print(add(10, 20)) 


#You can rename the module or functions for convenience.
import mymodule as mm  # Renaming the module

print(mm.greet("Charlie"))


#persion
a = mymodule.person1["age"]
print(a)