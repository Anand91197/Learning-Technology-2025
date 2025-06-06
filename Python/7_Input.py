#Input String and Number
a = input("Enter your Name: ")
print("My name is: ", a)

b = int(input("What is your age: "))
print("My agae is: ", b)


###
name = input("Enter your name: ")
print(f"Hello, {name}!")


color = input("What's your favorite color? ")
print(f"Wow! {color} is a beautiful color.")

name = input("Enter your name: ")
age = input(f"Hello {name}, how old are you? ")
print(f"{name} is {age} years old.")

#If you want to get more than one value in a single line, you can use the split() method.
x, y = input("Enter two numbers separated by a space: ").split()
x = int(x)
y = int(y)
print(f"You entered: {x} and {y}")
print(f"Sum = {x + y}")


a, b = input("Suggest two number: ").split()
a = int(a)  # Convert to integer
b = int(b)  # Convert to integer
print(f"Well, you've enter numbers are {a} and {b}")
print(f"Its Sum = {a + b}")


name = input("What is your name: ")
age = input(f"Hello {name}, what about you? ")
print(f" {age} Thank for you asking..!")

car = input("Which kind of vehicle you are looking for ? ")
brand = input(f"wow!! {car}, which {car} brand your looking for: ")
print(f"Yes {brand} is too good and I think you should go for it.")
