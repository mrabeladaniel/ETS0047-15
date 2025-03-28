1. upper()
The upper() method converts all characters in a string to uppercase.

Example:

text = "hello world"
result = text.upper()
print(result)
Output:


HELLO WORLD
2. lower()
The lower() method converts all characters in a string to lowercase.

Example:


text = "HELLO WORLD"
result = text.lower()
print(result)
Output:
hello world

3. replace()
The replace() method replaces a specified substring with another substring in the string.

Example:

text = "I like cats"
result = text.replace("cats", "dogs")
print(result)

Output:
I like dogs

4. title()
The title() method returns a copy of the string where the first letter of each word is capitalized and all other letters are in lowercase.

text = "hello world"
result = text.title()
print(result)

Output:
Hello World
5. capitalize()
The capitalize() method returns a copy of the string where only the first character is capitalized, and all other characters are converted to lowercase.

Example:
text = "hello world"
result = text.capitalize()
print(result)

Output:
Hello world

6. swapcase()
The swapcase() method returns a copy of the string where all uppercase letters are converted to lowercase and all lowercase letters are converted to uppercase.

Example:
text = "Hello World"
result = text.swapcase()
print(result)

Output:

hELLO wORLD
7. str.find()
str.find() method searches for a specified substring within the string and returns the lowest index where the substring is found. If the substring is not found, it returns -1.

Example:

text = "Hello, welcome to Python!"
result = text.find("welcome")
print(result)  

Output:
 7  
 because "welcome" starts at index 7

8. str.index()
str.index() method is similar to find(), but it raises a ValueError if the substring is not found, instead of returning -1.
Example:

text = "Hello, welcome to Python!"
result = text.index("welcome")
print(result)  
Output: 
7, because "welcome" starts at index 7

9. str.startswith()
 str.startswith() method checks whether the string starts with the specified prefix (substring) and returns True if it does, and False otherwise. It can also take optional start and end parameters to check a specific portion of the string.
 Example:
 text = "Hello, welcome to Python!"
result = text.startswith("Hello")
print(result)  
 Output:
  True, because the string starts with "Hello"

