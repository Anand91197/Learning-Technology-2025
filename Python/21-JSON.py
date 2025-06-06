#Convert from JSON to Python:
import json

# some JSON:
json_data =  '{ "name":"John", "age":30, "city":"New York"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data)

# the result is a Python dictionary:
print(python_dict["age"])
print(python_dict["name"])
print(python_dict)


#Converting Python Dictionary to JSON
import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(data)  # Convert to JSON
print(json_string)

print("==========")
#Reading JSON from a File: The json.load() function reads JSON data from a file. (Reading data.json file)
import json

with open("data.json", "r") as file:
    data = json.load(file)  # Read JSON file and convert to Python dictionary

print(data)
print(data["city"])  # Output: Chicago

#Writing JSON to a File: The json.dump() function writes a Python dictionary into a JSON file.
import json

data = {
    "name": "David",
    "age": 28,
    "city": "Houston"
}

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)  # Save with indentation for readability  #indent=4 : Pretty-print JSON output

print("JSON file created successfully!")
