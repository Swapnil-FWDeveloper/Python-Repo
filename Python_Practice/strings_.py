# Strings 
# String is data type that stores a sequence of characters

# Slicing

# str="Apna Collage"
# print(str[1:3])

# String Function

# replace()
# When ever we want to replace string character with another character then we use String replace funciton


# Replace_Char = "Hello my Name is Swapnil";
# print(Replace_Char.replace("H", "B"))
# print(Replace_Char.replace("Hello", "Volla"))

# We can replace entire Sentence also

# find()
# Used in finding character in a string with its index

# Find_Char = "Hello my Name is Swapnil";
# print(Find_Char.find("Name"))

# count()
# Count funciton counts the occurances of character

# Count_Char = "Hello my Name is Swapnil and I am Data Scientist";
# print(Count_Char.count("a"))
# print(Count_Char.count("Hello", "Volla"))

# Practice
# WAP to input user's first name and print its length

Enter_Name=str(input("Enter your name : "))
print(Enter_Name,"name length is ", len(Enter_Name))