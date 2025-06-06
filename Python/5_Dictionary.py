#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Print a single item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


#To determine how many items a dictionary has, use the len() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}
print(len(thisdict))


#You can change the value of a specific item by referring to its key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)


#The update() method will update the dictionary with the items from the given argument.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)


#Add New Item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)


#Removing Items
#The pop() method removes the item with the specified key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#The popitem() method removes the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


#Indexed by Keys (Accessed using keys, not indexes)
person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer",
    
}
print(person)

#Accessing Values
#The get() method is safer because it doesn't cause an error if the key doesn't exist. It returns None instead.
print(person["name"])  
print(person.get("age"))

# Adding a new key-value pair
person["city"] = "New York"
print(person)

# Updating an existing key
person["age"] = 26
print(person)

#Removes an item
person.pop("age")
print(person)

#Deletes an item or the entire dictionary.
del person["job"]
print(person)



#Looping Through a Dictionary
person = {"name": "Sunil", "age": 30, "job": "SRE Engineer"}

# Looping through keys
for key in person:
    print(key)

# Looping through values
for value in person.values():
    print(value)

# Looping through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")


#Nested Dictionary
students = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])



#Useful
print(person.keys())      # Returns all keys
print(person.values())     # Returns all values
print(person.items())      # Returns all key-value pairs


##Creating Dictionary Using dict() Constructor
person = dict(name="Alex", age=25, job="CA")
print(person)


