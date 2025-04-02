#19. str.isalnum()
#Returns True if the string consists only of alphanumeric characters (letters and digits) and is not empty.
#Example:
print("Hello123".isalnum()) 
 # Outout: True
print("Hello 123".isalnum()) 
 # Outout: False (contains space)
print("Hello!".isalnum())  
# Outout: False (contains special character)
print("".isalnum()) 
 # Outout: False (empty string)
#20.str.isspace()
#Returns True if the string consists only of whitespace characters (space, tab, newline, etc.) and is not empty.
#Example:
print("   ".isspace())  
# Outout: True
print("\t\n".isspace())
  # Outout: True
print("Hello".isspace()) 
 # Outout: False
print(" Hello ".isspace())
  # Outout: False
#21.str.format(*args, **kwargs)
#Used for string formatting, allowing you to insert values into a string. 
#Example:
print("My name is {} and I am {} years old.".format("Alice", 25))
# Output: My name is Alice and I am 25 years old.
