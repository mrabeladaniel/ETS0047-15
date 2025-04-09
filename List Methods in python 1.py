#1. append()
#Definition:
#Adds a single element to the end of a list.
#Example:
fruits = ['apple', 'banana']
fruits.append('cherry')
print(fruits)
#Output
['apple', 'banana', 'cherry']

#2. clear()
#Definition:
#Removes all items from the list, making it an empty list.
#Example:
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)
#Output:
[]

#3. copy()
#Definition:
#Returns a shallow copy of the list (a new list with the same elements).
#Example:
fruits = ['apple', 'banana']
fruits_copy = fruits.copy()
print(fruits_copy)
#Output
['apple', 'banana']
