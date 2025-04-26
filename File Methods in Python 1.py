#1. close()
#Closes an open file. After this, you can’t read or write from it unless you reopen it.
#Example:
f = open('example.txt', 'r')
f.close()
print(f.closed)  
# This checks if the file is closed
#Output : True

#2. detach()
#Used with buffered streams (like when you open files in binary mode). It detaches the underlying raw stream.
#Example:
f = open('example.txt', 'rb')
raw = f.detach()
print(type(raw))
#Output
#try to use f after detaching, you’ll get an error

#3. fileno()
#Returns the file’s file descriptor (an integer used by the OS to refer to the open file).
#Example:
f = open('example.txt', 'r')
print(f.fileno()) 
 # Output: some integer like 3 or 4
