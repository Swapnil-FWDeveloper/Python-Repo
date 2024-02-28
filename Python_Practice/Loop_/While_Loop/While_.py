# Loops are used to repeat instructins.

# while Loop

# while condition :
    # some work

count=1
while count <=5 :
    print("Hello While Loop",count)
    # count=count+1
    count+=1

count=5
while count >=1 :
    print("Reverse While Loop",count)
    # count=count+1
    count-=1          

# Practice question

# 1 Print number form 1 to 100 and 100 to 1

i = 1
while i <= 100 :                          
    print(i)
    i+=1

############################################

# i = 100
while i >= 1 :
    print(i)
    i-=1
   

# 2 Print multiplication of table of number n

mul= int(input("Enter the number : "))
i=1
while (i <=10) :
    print(mul*i)
    i+=1

# 3 Print the element of the  following list using a loop
list_D = [1,2,4,9,16,25,36,49,61,81,100]
idx=0
while(idx <= len(list_D)-1) :
# while(idx < len(list_D)) :
    print(list_D[idx])
    idx+=1


# Search for a number x in this tuple using loop 
list_D = [1,2,4,9,16,25,36,49,61,81,100]
i=0
while i < len(list_D) :
    if list_D[i]==49 :
        print("Got the number",list_D[i])
    i+=1    

list_D = [1, 2, 4, 9, 16, 25, 36, 49, 61, 81, 100]
dynamic_data = int(input("Enter the number: "))

i = 0
found = False
while i < len(list_D):
    if list_D[i] == dynamic_data:
        print("Got the number", list_D[i])
        found = True
        break
    i += 1

if not found:
    print("Number", dynamic_data, "not found in the list.")
