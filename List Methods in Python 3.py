#1. insert()
#Inserts an element at a specific position in the list.
#Example:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)
# Output: 
#['apple', 'orange', 'banana', 'cherry']

#2. pop()
#Removes and returns the element at the given index. 
#If no index is specified, it removes the last element.
#Example:
fruits = ['apple', 'banana', 'cherry']
removed = fruits.pop(1)
print(removed)    
  # Output: banana

print(fruits)     
  # Output: ['apple', 'cherry']
#3. remove()
#Removes the first occurrence of the specified value.
#Example:
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)
# Output: 
#['apple', 'cherry', 'banana']
