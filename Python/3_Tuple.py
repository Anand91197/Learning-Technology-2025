#A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Data type of a tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

single_item = ("apple",)  
print(type(single_item))  

not_a_tuple = ("apple")  
print(type(not_a_tuple))


#Accessing Tuple Elements using Indexing
print(thistuple[2])

#Once a tuple is created, you cannot modify its elements. 
#thistuple[1] = "orange"  # ❌ This will cause an error

#Packing: Assign multiple values to a tuple
#Unpacking: Extract values from a tuple
person = ("Alice", 25, "Engineer")  # Packing
(name, age, job) = person  # Unpacking

print(name)  
print(age)   
print(job)

#Since tuples are immutable, you can convert them to a list to modify elements.
fruits = ("apple", "banana", "cherry")
fruits_list = list(fruits)  # Convert tuple to list
fruits_list.append("orange")  # Modify the list
fruits = tuple(fruits_list)  # Convert back to tuple
print(fruits)


#Tuples have two built-in methods:

#count() → Returns the number of times a value appears in the tuple
#index() → Returns the index of the first occurrence of a value
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))  # Output: 3 (since 2 appears 3 times)
print(numbers.index(3))  # Output: 2 (index of first occurrence of 3)
