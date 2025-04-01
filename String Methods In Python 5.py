#16.str.join():
#This method is used to join elements of an iterable (like a list or tuple) into a single string. 
#The string that calls the method is used as a separator.
#Example:
words = ["Hello", "World"]
result = " ".join(words)
print(result)  
# Output: "Hello World"
#17. str.isalpha():
#This method checks if all the characters in the string are alphabetic (i.e., they are letters).
#It returns True if all characters are alphabetic and there is at least one character, otherwise it returns False.
#Example:
text = "Hello"
print(text.isalpha())
  # Output: True
text = "Hello123"
print(text.isalpha())
  # Output: False
#18. str.isdigit():
#This method checks if all the characters in the string are digits.
#It returns True if all characters are digits and there is at least one character, otherwise it returns False.
#Example:
text = "12345"
print(text.isdigit()) 
 # Output: True
text = "123a5"
print(text.isdigit()) 
 # Output: False
