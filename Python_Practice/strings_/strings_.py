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

# Enter_Name = str(input("Enter your name : "))
# print(Enter_Name,"name length is ", len(Enter_Name))


# Conditional Statement
#if-elif-else (syntax)

# Example Result Day

Eng_Marks = int(input("Enter your English marks : "))
Maths_Marks = int(input("Enter your Maths marks : "))
Science_Marks = int(input("Enter your Science marks : "))
Hindi_Marks = int(input("Enter your Hindi marks : "))
Social_Science = int(input("Enter your Social Science marks : "))

Best_5 = Eng_Marks + Maths_Marks + Science_Marks + Hindi_Marks + Social_Science
Percentage = (Best_5 / 500) * 100
print(Percentage)

if (Percentage >= 92) :
    print("Congratulation you got A+")
elif (Percentage >= 80 < 91) :
    print("Congratulation you got A")
elif (Percentage >= 70 < 80) :
    print("Congratulation you got B+")
elif (Percentage >= 60 < 70) :
    print("Congratulation you got B")
elif (Percentage >= 50 < 60) :
    print("Congratulation you got C+")            
else : 
    print("No Worry work on your skills")






    