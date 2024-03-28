#Age Group Classifier: Develop a program that takes a person's age as input and then outputs 
# their age group

age = int(input("Please enter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")