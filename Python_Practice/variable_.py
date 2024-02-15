print("Hello world")
'''
if want to add in one line so use
print("Hello" , "my name is Swpanil")
'''
name="Swapnil"
print (name)    

# Reassign 

name='Raja'
name='Swapnil' # Reasigned
print(name)


# Data Type
age = 25       # Interger 
name = "John"  # String
height = 5.11  # Float
is_student = True # Boolean
no_value = None # None

print(age)
print(name)
print(height)
print(is_student)
print(no_value)

#Print Sum
a=2
b=5
sum=a+b
print(sum) 


#Expression Execution 

#Rule 1
A,B=2,3
expExe="@"
print(A*expExe*B)
print(2*expExe*3)
#The code assigns `2` to `A`, `3` to `B`, `"@"` to `expExe`, then prints `"@@@"  as Python is Expression Execution language.

#Rule 2
# String & Sting can operate with +
a,b="2",3
expExe1="@"
print((a+expExe1)*b)
# The code assigns the string `"2"` to `a`, `3` to `b`, `"@"` to `expExe1`, then prints `"@@@".

# Rule 3
# Numeric value can operate with all the operator
c,d=2,3
e=4
print(c+d*e)

# Rule 4

# Arithmetic expression with Integer and float will result in float

c,d=2.5,3
e=c*d
print(e)



# Rule 5
# Result o fdivision operator with two integers will be float
A,B=1,2
C=A/B
print(C)

# Rule 6
# Integer division with float and int will give int displayed as float
num1,num2=1.5,3
num3=num1//num2
print(num3,num1/num2)