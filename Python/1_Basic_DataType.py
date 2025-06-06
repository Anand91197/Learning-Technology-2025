print("Anand Saini")


#Data Type

x = 5
print (x)
print (type(x))

y = ["Anand", "Harish"]
print (y)
print(type(y))


value = 42

if type(value) == int:
    print("The variable is an integer.")

#Number

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#String Modify

a = "Hello Anand Saini"
print (a)
print(a.lower())

print(a.strip())

print(a.replace("H", "J"))


#String Concatenation
a = "Saini"
b = "Anand"
c = a+b
print(c)

#Format method
age = 27
txt = "This is Jhon, and my age is {}"
print(txt.format(age))

Roll =20
txt = "My roll number is {}"
print(txt.format(Roll))

name = "Alice"
age = 25

print("My name is {} and I am {} years old.".format(name, age))


print("My favorite fruit is {fruit}.".format(fruit="Mango"))


#Boolean
print(100>10)


=======
name = "Alice"
age = 25

# Using f-string
print(f"My name is {name} and I am {age} years old.") #My name is Alice and I am 25 years old.

#print(f"{key}: {value}")
#Here, key and value are variables. The f before the string tells Python to replace {key} and {value} with their actual values.






