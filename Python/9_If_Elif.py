#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >=80:
    print("Grade: B")
elif score >=70:  
    print("Grade: C")
else:
    print("Grade: Pass")




#Use elif (short for "else if") to check multiple conditions.
score = int(input("Please enter your score: "))
print(f"You've entered a score: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")




#Grading 
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")     
    
