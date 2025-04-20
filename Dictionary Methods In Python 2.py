 #1. items() 
#The items() method returns a view object that displays a list of dictionary’s key-value pairs as tuples.
#Useful for iterating over both keys and values.
#Example:
student = {"name": "Alice", "age": 20}

for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Alice
# age : 20

#2. keys()
#The keys() method returns a view object that displays all the keys in the dictionary.
    #Example:
    student = {"name": "Alice", "age": 20}

print(student.keys())
  # Output: dict_keys(['name', 'age'])

# Iterating over keys
for key in student.keys():
    print(key)
# Output:
# name
# age
    #3.  get() 
#The get() method is used to retrieve the value for a specified key in a dictionary.
#If the key is not found, it returns None (or a custom default value if specified) without raising an error.
#Example:
    student = {"name": "Alice", "age": 20}

print(student.get("name"))     
   # Output: Alice
print(student.get("grade"))  
     # Output: None
print(student.get("grade", "N/A"))
# Output: N/A (custom default)

