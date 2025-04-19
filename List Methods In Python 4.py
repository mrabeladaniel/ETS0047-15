#1. reverse()
#Reverses the elements of the list in place (modifies the original list).
#Example:
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
# Output:
# [5, 4, 3, 2, 1]
#2. sort()
#Sorts the list in ascending order by default. Can sort in descending order using reverse=True.
#Example:
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print(numbers)
# Output: 
#[1, 2, 3, 5, 9]
numbers.sort(reverse=True)
print(numbers)
# Output: 
#[9, 5, 3, 2, 1]
