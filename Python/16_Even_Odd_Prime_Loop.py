#Check Even and Odd Number
a = int(input("Enter a number: "))

if a % 2 == 0:
    print("Its Even Number")
else:
    print("Odd Number")    


#Check Postive and Negative Number
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#Check Prime Number
#Prime numbers are those natural numbers divisible by only 1 and the number itself.
num = int(input("Enter the desired number: "))
for i in range (2, num):
    if (num% i) == 0:                            #If num is perfectly divisible by i (meaning the remainder is 0), then num is not a prime number.
       print("The number is not a prime number")
       break
else:
 print("The number is a prime number")  




#Check if year is a leap year or not: Year divided by 4 is a leap year
year = 2024
## year = int(input("Enter a year: "))
if (year % 4 ==0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))    


   

