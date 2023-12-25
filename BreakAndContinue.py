## Break and Continue keywords

students = [ "ram", "shyam" , "kishan", "radha", "radhika"]

for student in students:
    if student == "radha":
        break               ## break; semicolon is optional
    print(student)


for student in students:
    if student == "kishan":         #for kishan the loop will not print
        continue
    print(student)