# Lists and Tuples in Python

# Lists:
# - A built-in data type that stores a set of values.
# - Mutable, meaning elements can be changed after creation.
# - Can store elements of different types (integer, float, string, etc.).

# Tuples:
# - A built-in data type that creates immutable sequences of values.
# - Defined using parentheses ().
# - Elements cannot be changed after creation.

# Tuple Method Example:

tup = (1, 2, 3, 4)
print(tup.index(2))  # Output: 1
print(tup.count(3))  # Output: 1

# Practice: Asking User for Favorite Movies
Ent_Mov1 = input("Enter the favorite movie name 1: ")
Ent_Mov2 = input("Enter the favorite movie name 2: ")
Ent_Mov3 = input("Enter the favorite movie name 3: ")
movies = [Ent_Mov1, Ent_Mov2, Ent_Mov3]
print(movies)

# Check if a List Contains a Palindrome

# Type-1

check_Palin = input("Check Palindrome: ")
rev_Palin = check_Palin[::-1]
if check_Palin == rev_Palin:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

# Type2
check_Palin1=[1,2,3,4,5]
check_Palin1.reverse()
print(check_Palin) 
# Count the Number of Students with Grade "A"    
cls_std = ['A', 'B', 'A', 'B', 'D', 'D', 'A', 'A']
count_A = cls_std.count('A')
print("Number of students with grade 'A':", count_A)

# Sorting and Printing the List
cls_std.sort()
print(cls_std)
