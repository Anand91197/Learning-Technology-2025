#Lets say we have a list L1 = [1, 2, 2, 3, 2, 3, 4, 5], now identify the most repetitive element in the list? via dictionary 

L1 = [1, 2, 2, 3, 2, 3, 4, 5]

# Create an empty dictionary to store counts
count_dict = {}

# Count occurrences of each element
for num in L1:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Find the element with the maximum count
most_common_element = max(count_dict, key=count_dict.get)
max_count = count_dict[most_common_element]

print(f"The most repetitive element is {most_common_element} with {max_count} occurrences.")
