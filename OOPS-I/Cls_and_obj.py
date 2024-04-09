# Class and object in python

# creating clss
class student:
    name="karan kumar"

# creating objrct 
obj1 = student()
print(obj1.name)    

class Fruits:
    fruit1 = "Mango"
    fruit2 = "Apple"
    fruit3 = "Banana"

Fruit_store=Fruits()
print(Fruit_store.fruit1)



# print(Fruit_store.fruit2)
# print(Fruit_store.fruit3)


# Constructor 
#  Constructor is init function which always executed when the class is being initiated 
#  it basscally like .this in JS
# creating class constructor
class Student_info:
    def __init__(self,fullname) :
        self.name=fullname
s1=Student_info("Swapnil")
print(s1.name)
# It takes one parameter i.e Self 
# This self parameter is a referance to the current instance of the classand it used to access variables that belongs to the class.
# Self is like .this keyword in Js which was refering to the parent function. 
            
class Student1:
    def __init__(self) :
        print("Adding new addmission to Student1..")
        self.name="Swapnil-Shende"
        self.age=20
        self.marks=90
        print(self.name)
S2=Student1() # it will print name as it is calling it self
print(S2.name)        
print(S2.age) 
print(S2.marks)  
        
class Student1:
    def __init__(self,fullname) :
        print("Adding new addmission to Student1..")
        self.name=fullname
        self.age=20
        self.marks=90
        print(self.name)
S2=Student1("Swapnil-Shende") # it will print name as it is calling it self
print(S2.name)        
print(S2.age) 
print(S2.marks)

class Student1:
    def __init__(self,fullname,age) :
        print("Adding new addmission to Student1..")
        self.name=fullname
        self.age=age
        self.marks=90
        print(self.name)
S2=Student1("Swapnil-Shende",21) # it will print name as it is calling it self
# print(S2.name,97)        
print(S2.marks)