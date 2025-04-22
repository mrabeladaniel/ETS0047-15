#1. pop()
#Removes the specified key and returns the corresponding value. 
#If the key is not found, it raises a KeyError (unless a default value is provided).
#Exmaple:
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
age = my_dict.pop('age') 
 # Removes 'age' and returns its value
print(age)
      # Output: 25
print(my_dict)            
# Output: {'name': 'Alice', 'city': 'Paris'}

#2. popitem()
#Removes and returns the last inserted key-value pair as a tuple (in Python 3.7+).
#Raises KeyError if the dictionary is empty.
#Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
last_item = my_dict.popitem()
print(last_item)     
     # Output: ('c', 3)
print(my_dict)
     # Output: {'a': 1, 'b': 2}
#3. setdefault()
#Returns the value of the specified key.
#If the key does not exist, it inserts the key with a specified default value and returns that value.
#Example:
my_dict = {'fruit': 'apple', 'vegetable': 'carrot'}
value = my_dict.setdefault('fruit', 'banana')  # Key exists
print(value)     
          # Output: apple

value2 = my_dict.setdefault('drink', 'water')  # Key doesn't exist
print(value2)       
       # Output: water
print(my_dict)
# Output: {'fruit': 'apple', 'vegetable': 'carrot', 'drink': 'water'}
