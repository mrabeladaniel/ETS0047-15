#1. flush()
#Forces the data in the buffer to be written to the file immediately.
#Example:
f = open('data.txt', 'w')
f.write('Hello')
f.flush()  # Ensures 'Hello' is actually written to the file
f.close()
#No output — it just does the job behind the scenes.

#2. isatty()
#eturns True if the file is connected to a terminal (like stdin or stdout), else False.
#Example:
f = open('data.txt', 'r')
print(f.isatty())
f.close()
#Output:
#False

#3. read()
#Reads the entire content of the file (or up to a certain number of bytes).
#Example:
f = open('data.txt', 'r')
print(f.read())  # Reads everything
f.close()