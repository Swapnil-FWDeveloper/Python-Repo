# # Function
# # Function is a group of statement that perform a specific task

# # Syntaax def function_name(parameter) : 
# # some work
# # return value or print value
# # function_name(argument1, argument2) function call
# # function_name(argument1, argument2) function call

def sum(a,b) :
    s=a+b
    return s
    # print (s)
sum(2,3)    

# # print(sum(5,2))
# # print(sum(50,2))
# # print(sum(5,20))
# # print(sum(50,20))


# def print_hello():
#     return "Hello"

# print_hello()
# output=print_hello()
# print(output)    


# Write a function that caluculate avg of three number

def avdcal (a,b,c):
    avg=(a+b+c)/3
    return avg
output=float(avdcal(2,3,4))
print(f"The avg is : {output}") 

########################################################################

# Types in Python
# Build-in Functions Used defined Fucntions

# Build-in Functions
# print()
# len()
# type()
# range(0, len())

# User Defined Functions

# The functon wich we define


herios=['herios','herios','herios','herios','herios','herios','herios']
def print_len(lst):
    print(len(lst))
def print_list(lst):
    for item in lst:
        print(item)

print_len(herios)
# print_list('herios')



