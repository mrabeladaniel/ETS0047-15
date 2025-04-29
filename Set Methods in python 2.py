#1. difference()
#Returns a new set with elements from the first set that are not in the second set.
#Example:
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a.difference(b))
# Output: {1, 2}

#2.difference_update()
#Removes elements found in another set from the original set.
#Exqmple:
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.difference_update(b)
print(a)
# Output: {1, 2}

#3. discard()
#Removes an element from the set if it is present. No error if the element is missing.
#Example:
s = {1, 2, 3}
s.discard(2)
print(s)
# Output: {1, 3}

s.discard(5)  # No error even though 5 is not in the set
print(s)
# Output: {1, 3}