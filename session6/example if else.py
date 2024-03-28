#if_else grade calculator
value = int (input(" Enter your score:"))

if value >100:
    print(" Invalid score")
elif 90 <= value <= 100:
    print ("your grade is A")
elif 80 <= value <= 89:
    print ("your grade is B")
elif 70 <= value <= 79:
    print ("your grade is C")
elif 60 <= value <= 69:
    print ("your grade is D")
elif 89 <= value <= 99:   
    print ("your grade is E")
else:
    print ("invalid score")

