#Call Function

import math_operations

a = math_operations.add(9,8)
print(a)

print(f"The subtraction result is: {math_operations.subtract(55,4)}")

x = int(input("Enter a numbber X: "))
y = int(input("Enter a number Y: "))
b = math_operations.multiply(x,y)
print(b)

#New Check
import math_operations

result_add = math_operations.add(5,9)
result_subtract = math_operations.subtract(70,5)
result_multiply = math_operations.multiply(9,8)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")