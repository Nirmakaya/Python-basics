# Simple Function
def login(username, password):
    print(username, password)

login('Sam', 'Kia@124')
login(username='kia', password='ola')


# Arg Function : *args, by this parameters numbers can be any value.
def getMarks(*arg):
    for x in arg:
        print(x)

getMarks(10, 20, 30, 40, 50)
getMarks("A", "A+", "B", "B+")



# Keyword args Function : **args, parameters
def getStudentMarks(**args):
    for key, value in args.items():
        print("%s==%s" %(key,value))

getStudentMarks(naveen=10, tom=20, peter=30)
getStudentMarks(key="apple", sellerName="Xeon")


## Lambda Function : It's an anonymous function, Function without a name
cube = lambda x: x*x*x
total = lambda marks: marks+30

print(cube(4))
print(total(100))