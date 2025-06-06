#math module
import math

print(math.sqrt(16))        # Output: 4.0 (Square root)
print(math.pi)              # Output: 3.141592653589793
print(math.factorial(5))



#datetime - Working with dates and times
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))  #%A Weekday, full version
print(x.strftime("%B"))   #%B Month name
