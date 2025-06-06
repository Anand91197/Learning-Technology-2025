x = 20
y = 5

if x > y:
    print("x is greater than y")
    if x > 15:
        print("x is also greater than 15")
    else:
        print("x is not greater than 15")
else:
    print("x is not greater than y")





#Nested if Statements: if statement inside another if statement.
age = int(input("Enter your age: "))
print(f"Your age is: {age}")

is_registered = input("Have you register or not (Yes/No): ").strip().lower()  #Making input case-insensitive: .strip().lower() ensures that YES, Yes, yes are all accepted.

if age >= 18:
    if is_registered == "yes":
        print("You are eligible to vote.")
    else:
        print("You need to register to vote.")
else:
    print("You are not eligible to vote.")    
