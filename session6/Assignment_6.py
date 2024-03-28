#if_else grade calculator
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

