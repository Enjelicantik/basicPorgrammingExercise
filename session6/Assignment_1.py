#Grade Calculator: Create a program that takes a student's score as input and then outputs 
#their corresponding letter grade based on the following criteria

value = int (input(" Enter your score:"))

if value >100:
    print(" Invalid score")
elif value >= 90:
    print ("your grade is A")
elif value >= 80:
    print ("your grade is B")
elif value >= 70:
    print ("your grade is C")
elif value >= 60:
    print ("your grade is D")
elif value >= 0:
    print ("your grade is E")
else:
    print( "Invalid score")

