# Basic data Types
# Numbers
x = 3
print(type(x))  # Prints "<class 'int'>"
print(x)        # Prints "3"
print(x + 1)    # Addition: prints "2"
print(x - 1)    # Subtraction: prints "2"
print(x * 2)    # Multiplication: prints "6"
print(x ** 2)   # Exponentiation: prints "9"
x += 1
print(x)    # Prints "4"
y = 2.5
print(type(y))  # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"

# Booleans
t = True
f = False
print(type(t))  # Prints "<class 'bool'>"
print(t and f)  # Logical AND; prints "False"
print(t or f)   # Logical AND; prints "True"
print(not t)    # Logical NOT; prints "False"
print(x != f)   # Logical XOR; prints "True"

# Strings
hello = 'hello'     # String literals can use single quotes
world = "world"     # or double quotes; it does not matter.
print(hello)        # Prints "hello"
print(len(hello))   # String length; Prints "5"
hw = hello + ' ' + world    # String concatenation
print(hw)   # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formating.
print(hw12) # prints "hello world 12"
