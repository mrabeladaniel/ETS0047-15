#1. clear()
#The clear() method removes all the items from the dictionary, leaving it empty.
#Example:
my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)
  # Output: {}
#2. copy()
#The copy() method returns a shallow copy of the dictionary. 
#This means the copy is a new dictionary with the same key-value pairs, but changes to it won't affect the original.
#Example:
original = {'a': 1, 'b': 2}
duplicate = original.copy()
duplicate['a'] = 100
print(original)  
 # Output: {'a': 1, 'b': 2}
print(duplicate)
  # Output: {'a': 100, 'b': 2}
#3. fromkeys()
#The fromkeys() method creates a new dictionary from a given sequence of keys and sets all values to a specified value (default is None if not given).
#Example:
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys)
print(new_dict) 
 # Output: {'a': None, 'b': None, 'c': None}
#Example 2:
keys = ['x', 'y']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'x': 0, 'y': 0}
