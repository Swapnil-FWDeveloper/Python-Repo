```markdown
# Python Basics

## Variables

Variables are named memory locations in a program.

Example:
```python
name = "Swapnil"
```
`name` is a variable holding the value "Swapnil".

## Rules for Identifiers / Variables

- Start with a letter (a-z, A-Z) or underscore (_).
- Subsequent characters can be letters, digits (0-9), or underscores.
- Special characters like !, @, #, $, %, ^, &, * are not allowed at the start.
- Python keywords cannot be used as identifiers.

## Data Types

- **Integer**: Represents whole numbers.
- **String**: Represents text data.
- **Float**: Represents decimal numbers.
- **Boolean**: Represents True or False values.
- **None**: Represents the absence of a value.

Example:
```python
age = 25
name = "John"
height = 5.11
is_student = True
no_value = None
```

## Expression Execution

### Rule 1
```python
A, B = 2, 3
expExe = "@"
print(A * expExe * B)
print(2 * expExe * 3)
```
The code assigns `2` to `A`, `3` to `B`, `"@"` to `expExe`, then prints `"@@@"`.

### Rule 2
```python
a, b = "2", 3
expExe1 = "@"
print((a + expExe1) * b)
```
The code assigns the string `"2"` to `a`, `3` to `b`, `"@"` to `expExe1`, then prints `"@@@"`.

### Rule 3
```python
c, d = 2, 3
e = 4
print(c + d * e)
```
Numeric values can operate with all operators.

### Rule 4
```python
c, d = 2.5, 3
e = c * d
print(e)
```
Arithmetic expression with Integer and float results in float.

### Rule 5
```python
A, B = 1, 2
C = A / B
print(C)

```
Division operator with two integers results in float.

### Rule 6
```python

num1, num2 = 1.5, 3
num3 = num1 // num2
print(num3, num1 / num2)

```
Integer division with float and int results in int displayed as float.
```

These notes provide a concise overview of Python basics, covering variables, rules for identifiers, data types, and expression execution.


Alpha Bita Gammma