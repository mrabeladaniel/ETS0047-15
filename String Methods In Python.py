10. str.strip()
This method is used to remove any leading and trailing whitespace characters (spaces, tabs, newlines, etc.) from a string.

Example:

text = "  Hello, World!  "
print(text.strip()) 

Output: 
"Hello, World!"

11. str.endswith()
This method checks if a string ends with a specified suffix. It returns True if the string ends with the given suffix, otherwise False.

Example:

filename = "example.txt"
print(filename.endswith(".txt")) 
 Output:
   True

print(filename.endswith(".pdf"))  
 Output: 
False

12. str.count()
This method returns the number of non-overlapping occurrences of a substring in the string.

Example:
text = "hello world, hello everyone"
print(text.count("hello"))  

Output:
2




