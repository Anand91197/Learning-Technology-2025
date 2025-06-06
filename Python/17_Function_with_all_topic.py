#A function is a block of code which only runs when it is called.
#Functions are blocks of code that perform a specific task. They help organize code, make it reusable, and improve readability.
#In Python a function is defined using the def keyword
def my_function():
  print("Hello I'm from a India")

my_function()  


def greet(name):
  print(f"Hello,  {name}!!!")

greet("Anand")  

#Basic to Advanced
def greet():
    print("Hello! Welcome to Python Programming.")

greet() 


#Functions with Parameters (Inputs)
def greet(name):
    print(f"Hello, {name}! Welcome to Python Programming.")

greet("Anand")    

#Functions with Multiple Parameters
def add_numbers(a,b):
    result = a+b
    print(f"The sum of {a} and {b} is {result}.")

add_numbers(5, 3)    


#Functions with return Statement; If you want the function to return a value, use the return keyword.
def multiply(x, y):
    return x * y
product = multiply(4, 5)
print(f"Product: {product}")


#Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Uses the default value
greet("Charlie")  # Uses the provided argument    

#If we call the function without an argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Keyword Arguments (Named Arguments)
def display_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

display_info(age=25, name="Bob")


#*args (Multiple Arguments)
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)


#**kwargs (Keyword Arguments as Dictionary)
def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_details(name="Alice", age=30, country="USA")


#Local Variable: Defined inside a function and accessible only within that function.
#Global Variable: Defined outside of any function and accessible everywhere.
x = "I am global"

def test():
    x = "I am local"
    print(x)

test()
print(x)

#To modify a global variable inside a function.
count = 0

def increment():
    global count
    count += 1

increment()
print(count)

#Nested Functions
def outer():
    message = "Hello"

    def inner():
        print(message)
    
    inner()  # Calling the inner function

outer()

#Functions can be stored and called from lists or dictionaries.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = {
    "add": add,
    "subtract": subtract
}

result_1 = operations["add"](10, 5)
result_2 = operations["subtract"] (15, 5)
print(result_1)
print(result_2)


#Recursive Functions: A function can call itself. This is called recursion.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120



#To check number
def is_even(num):
  return num % 2 == 0

def is_odd(num):
  return num % 2 != 0

def square(num):
  return num ** 2    #num ** 2 means raising num to the power of 2

num = int(input("Enter a number: "))

if is_even(num):
  print(f"{num} is even")
else:
  print(f"{num} is odd")

print(f"The square of {num} is {square(num)}")

#Odd_Even
def odd_even(x):
  if x%2==0:
    print(x, "is even")
  else:
    print(x, "is odd")
odd_even(5)
