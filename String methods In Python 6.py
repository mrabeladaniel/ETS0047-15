#13. str.lstrip([chars])
#Removes leading (left-side) whitespace or specified characters from the string.
#Example:
s = "  hello  "
print(s.lstrip())

  # Output: "hello  "
#14. str.rstrip([chars])
#Removes trailing (right-side) whitespace or specified characters from the string.
#Example:
s = "  hello  "
print(s.rstrip())  
# Output: "  hello"

#15.str.split([sep, maxsplit])
#Splits the string into a list of substrings based on the given separator (sep).
#If no separator is provided, it splits by whitespace.
#maxsplit specifies the maximum number of splits.
#Example:
s = "hello world python"
print(s.split()) 
 # Output: ['hello', 'world', 'python']
