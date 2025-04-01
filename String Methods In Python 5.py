#13. str.lstrip()
#This method removes leading whitespace (spaces, tabs, newlines) from the string. 
#And also helps to pass a string argument to specify the characters to be removed from the start of the string.
#Example:
text = "   Hello World!"
print(text.lstrip()) 
# Output:
#"Hello World!"

# Removing specific characters:
text = "xxxyyyHello World!"
print(text.lstrip("xy"))  
 #Output:
#"Hello World!"

#14.str.rstrip()
#This method removes trailing whitespace (spaces, tabs, newlines) from the string. 
#Like lstrip(), this method also helps to pass a string argument to specify the characters to be removed from the end of the string.

#Example:

text = "Hello World!   "
print(text.rstrip()) 
# Output: "Hello World!"

#Removing specific characters:
text = "Hello World!xxx"
print(text.rstrip("x")) 
 #Output: "Hello World!"
#15.str.split()
#this method splits a string into a list of substrings based on a specified delimiter (default is whitespace).
#EXample:
text = "apple orange banana"
result = text.split()
print(result)

#Output:
#['apple', 'orange', 'banana']
