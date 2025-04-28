#1. readable()
#Checks if the file can be read. Returns True or False.
#Example:
f = open('data.txt', 'r')
print(f.readable())
f.close()
#Output:
#True
#2. readline()
#Reads one line from the file.
#Example:
f = open('data.txt', 'r')
print(f.readline())
f.close()
#Output
#Hello

#3. readlines()
#Reads all lines and returns them as a list.
#Example:
f = open('data.txt', 'r')
print(f.readlines())
f.close()
#Output:
['Hello\n', 'World']
