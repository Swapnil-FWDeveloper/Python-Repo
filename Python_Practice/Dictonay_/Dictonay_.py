


# # Dictionary
# # Methods to manipulate dictionaries

# student = {
#     "marks": {
#         "Science": 99,
#         "Maths": 99,
#         "English": 99,
#         "Hindi": 99,
#         "EVS": 99,
#     }
# }

# # Return all keys in the dictionary
# student_keys = student.keys()
# print(student_keys)  # Output: dict_keys(['marks'])

# # Return all values in the dictionary
# student_values = student.values()
# print(student_values)  # Output: dict_values([{'Science': 99, 'Maths': 99, 'English': 99, 'Hindi': 99, 'EVS': 99}])

# # Return all (key, value) pairs as tuples
# student_items = student.items()
# print(student_items)  # Output: dict_items([('marks', {'Science': 99, 'Maths': 99, 'English': 99, 'Hindi': 99, 'EVS': 99})])

# # Return the value for the specified key
# marks_value = student.get("marks")
# print(marks_value)  # Output: {'Science': 99, 'Maths': 99, 'English': 99, 'Hindi': 99, 'EVS': 99}

# # Update the dictionary with specified items
# student.update({"EVS": 100})
# print(student)  # Output: {'marks': {'Science': 99, 'Maths': 99, 'English': 99, 'Hindi': 99, 'EVS': 100}}


# # Set in Python

# # Set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from them. 
# # Sets are defined using curly braces {} and can contain elements of any immutable data type such as integers, floats, strings, and tuples. 
# # However, sets themselves are mutable and cannot be elements of other sets.
# my_set = {1, 2, 3, 4, 5}
# print(my_set)


# # Methods to manipulate sets

# set_eg = {1, 2, 3}
# set_eg.add(5)  # Adds an element
# print(set_eg)  # Output: {1, 2, 3, 5}

# set_eg.remove(2)  # Removes the element
# print(set_eg)  # Output: {1, 3, 5}

# set_eg.clear()  # Empties the set
# print(set_eg)  # Output: set()

# set_Eg = {4, 5, 6}
# print_data = set_eg.union(set_Eg)  # Combines both sets and returns a new set
# print(print_data)  # Output: {4, 5, 6}

# set_Eg = {4, 5, 6}
# print_data = set_eg.intersection(set_Eg)  # Returns the common elements between both sets
# print(print_data)  # Output: {4, 5, 6}


# # Practice Proble
# # Store the value in Dectionary
# Str_val = {
#     "cat" : "A Small animal",
#     "table" : ["A piece of furniture" , "list of facts & figures"]
# }

# print(Str_val)
# getKeys=Str_val.keys()
# print(Str_val["cat"])
# print(getKeys)

# # assume the class for subjects and find classrooms are needed

# cls_room={'Python','Java',"C++","Python", "Java", "JavaScript","Python","C"}
# # find_leng=len(cls_room)
# print(len(cls_room))


# # Use Subject name as a key and name as a value

# marks={}
# x = int(input("enter phy : "))
# marks.update({"Physics" : x})

# x = int(input("enter phy : "))
# marks.update({"Maths" : x})

# x = int(input("enter phy : "))
# marks.update({"Eng" : x})

# print(marks)


# Problem
# Count the vovels
vol=["A","E","I","O","U"]
# ptvol=str(input("Enter the word :"))
# count=0
# dic={}
# for i in vol:
#     if(i==ptvol):
#         count+=1

