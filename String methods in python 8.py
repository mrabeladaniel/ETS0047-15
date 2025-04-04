#22
s = "Hello"
encoded_s = s.encode()  # Default UTF-8 encoding
print(encoded_s)  # Output: b'Hello'

# Using a different encoding
print(s.encode("ascii"))  # Output: b'Hello'

# Handling errors
s = "你好"  # Chinese characters
print(s.encode("ascii", errors="ignore"))  # Output: b'' (ignored)
print(s.encode("ascii", errors="replace"))  # Output: b'??'
#23
print("hello".islower())  # True
print("Hello".islower())  # False (contains uppercase 'H')
print("123".islower())  # False (no letters)
print("hello!".islower())  # True (non-letter characters are ignored)
print("".islower())  # False (empty string)

#24
print("HELLO".isupper())  # True
print("Hello".isupper())  # False (contains lowercase 'e')
print("123".isupper())  # False (no letters)
print("HELLO!".isupper())  # True (non-letter characters are ignored)
print("".isupper())  # False (empty string)

 