# Lists in Python
# A built-in data type that stores a set of values 
# It can store elements of different types (integer, float, string, etc.)
# Lists are mutable, meaning their elements can be changed after creation
# Lists are similar to arrays in other programming languages

# Example: Accessing elements in a list
marks = [87, 64, 33, 95, 76]
print(marks[2])  # Accessing the third element, index starts from 0
# Output: 33

# Slicing in lists
print(marks[1:4])  # Slicing elements from index 1 to 3
# Output: [64, 33, 95]

# List Methods

# Append: Adds one element at the end of the list
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Sort: Sorts the elements of the list in ascending order by default
# To sort in descending order, use list.sort(reverse=True)
my_list1 = [5, 6, 1, 2, 3, 8, 9, 4, 7]
my_list1.sort()
print(my_list1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert: Inserts an element at the specified index
my_list2 = [1, 5, 9, 7, 5, 3]
my_list2.insert(1, 6)  # Inserts 6 at index 1
print(my_list2)  # Output: [1, 6, 5, 9, 7, 5, 3]


#Tuples in Python

# A build in data type that lets us create IMMUTABLE sequence of values.
# Syntax= var=() 
tup=(5,6,4,7,8,9)
tup[0]=1 #NOT allowed in python but we can access index value


# Tuple Method
tup=(1,2,3,4)
print(tup.ele)