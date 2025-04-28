#1. seek()
#Moves the file cursor to a specific position.
#Example:
f = open('data.txt', 'r')
f.seek(5)  # Moves cursor to 5th byte (character)
print(f.read())
# Output: (reads content starting from 6th character)
f.close()

#2. seekable()
# Checks if the file allows moving the cursor. Returns True or False.
#Example:
f = open('data.txt', 'r')
print(f.seekable())
# Output: True
f.close()

#3. tell()
# Tells the current position of the cursor.
#Example:
f = open('data.txt', 'r')
print(f.tell())
# Output: 0
f.read(5)
print(f.tell())
# Output: 5
f.close()
