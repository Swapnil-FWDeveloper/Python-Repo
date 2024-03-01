# Loops are used for sequenctial traversal. For travesing list, string, tuples etc.

# for loops
# for el in list : 
    # some work

# for loop with else
# for el in list :
#     #some work
# else:
    # work when loops ends

list=[1,2,3,4,5]
for el in list :
    print(list)

# use in tuple
tup=(1,2,3,4,5,6,7,8,9)
for i in tup :
    print(i)

# range()
# Range funciton returns a sequence of numbers, starting from 0 by default and increments by 1 (by default), and stops before a specified number

# range(start?, stop , step?)

# The line `for i in list(5)` is attempting to iterate over the list variable, but it seems to have a
# syntax error. The correct syntax should be `for i in list:` to iterate over the elements in the
# list. The `(5)` after `list` is incorrect and should be removed.
for i in range(2,100,2) :
    print(i)
    # here loop is started from 2 till 100 with diffrence of 2


#Practice
# Run a loop form 1 to 100
for i in range(1, 100) :
    print(i)

for i in range(100, 0, -1) :
    print(i)

#  print the table 
n=int(input("enter the number : "))
for i in range(1,11) : 
    print(n*i)

# 
