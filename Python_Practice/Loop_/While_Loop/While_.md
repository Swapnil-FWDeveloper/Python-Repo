# Loops in Python

## Introduction

Loops are used to repeat instructions. Python provides several loop structures, such as `while` loop and `for` loop, to execute a block of code repeatedly.

## while Loop

````python
count = 1
while count <= 5:
    print("Hello While Loop", count)
    count += 1

count = 5
while count >= 1:
    print("Reverse While Loop", count)
    count -= 1

The while loop executes a block of code as long as the specified condition is true.


markdown
Copy code
# Loops in Python

## Introduction
Loops are used to repeat instructions. Python provides several loop structures, such as `while` loop and `for` loop, to execute a block of code repeatedly.

## while Loop
```python
count = 1
while count <= 5:
    print("Hello While Loop", count)
    count += 1

count = 5
while count >= 1:
    print("Reverse While Loop", count)
    count -= 1
The while loop executes a block of code as long as the specified condition is true.

Practice Questions
1. Print numbers from 1 to 100 and 100 to 1

i = 1
while i <= 100:
    print(i)
    i += 1

# Reverse order
i = 100
while i >= 1:
    print(i)
    i -= 1


2. Print the multiplication table of a number n

````

mul = int(input("Enter the number: "))
i = 1
while i <= 10:
print(mul \* i)
i += 1

3. Print the elements of a list using a loop

list_D = [1, 2, 4, 9, 16, 25, 36, 49, 61, 81, 100]
idx = 0
while idx <= len(list_D) - 1:
print(list_D[idx])
idx += 1

4. Search for a number x in a list using a loop

list_D = [1, 2, 4, 9, 16, 25, 36, 49, 61, 81, 100]
x = int(input("Enter the number to search: "))
i = 0
found = False
while i < len(list_D):
    if list_D[i] == x:
        print("Found", x, "at index", i)
        found = True
        break
    i += 1
if not found:
    print(x, "not found in the list.")
