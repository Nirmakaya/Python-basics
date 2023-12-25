## It is a complex datatype or a collection of items
## And not primitive datatype like bool,int,string
## List

marks = [95, 98, 97]
print(marks[-3])

# Index can be negative in python, -1 being the last index and so on

marks = [95, 98, 97]
print(marks[0:2])
# It will not include the index 2, so 0th and 1st index will be printed

# This takes variables in score and then print it by loop
for score in marks:
    print(score)

## Append
marks.append(100)

## Insert: it is used with index on which you want to isert
marks.insert(0, 99)

print(marks)

## in keyword
print(99 in marks)

## Length : elements in the list
print(len(marks))

# Iteration with while loop
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

## Clear : removes every element of the list
marks.clear()

print(len(marks)) # 0