marks = (99, 98, 97, 97, 97)

## Tuple : are immutable, and cannot be changed

print(marks.count(97))
# it keeps a count of times the number is there in tuple
print(marks.index(97))
# the first index of 97 int will be printed

# In tuple the parentheses is not important
person = "Twisha", "Sam", "Hoyaho"
# Above datatype is a tuple



## Set : only unique elements are present
## and there is no index, variable are not marked, no idea
## you can loop through every element though
## Sets are Unordered sequence

marks = {98, 90, 78, 90, 90}
print(marks)
#Only the unique element will be printed

for score in marks:
    print(score)

