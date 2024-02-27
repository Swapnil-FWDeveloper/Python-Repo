
# Dictionary => Are used to store data values in the form of key : value pairs
# They are unordered, mutable(changable) & they dont't allow duplicate keys

# syntax {}

# dict ={
#     "name" : "Swapnil",
#     "roll" : "47",
#     'marks' : [10,20,30,40,50]
# }
# print(dict)
# print(dict["name"])

# Nested Dictionary

student={
    "marks" : {
        "Science" : 99,
        "Maths" : 99,
        "English" : 99,
        "Hindi" : 99,
        "EVS" : 99,
    }
}
# print(student["marks"]["Science"])

# for key in student["marks"] :
#     print(key["marks"][key])