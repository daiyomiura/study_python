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

# String objects have a bunch of useful methods; for example:
s = "hello"
print(s.capitalize())   # Capitalize a string; prints "Hello"
print(s.upper())        # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))       # Right-justify a string, padding with spaces; prints "
print(s.center(7))      # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                                # prints(he(ell)(ell)o)
print('   world'.strip())       # Strip leading and trailing whitespace; prints "world"
# Containers
# Python includs several built-in container types: lists, dictionaries, sets, and tuples.

# Lists
#  A list is the Python equivalent of an array, but is resizeable and can contain elements of different types:

xs = [3, 1, 2]      # Create list
print(xs, xs[2])    # Prints "[3, 1, 2 ] 2"
print(xs[-1])       # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'       # Lists can contain elements of different types
print(xs)           # Prints "[3, 1, 'foo']"
xs.append('bar')    # Add a new element to the end of the list
print(xs)           # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()        # Remove and return the last element of the list
print(x, xs)        # Prints "bar [3, 1, 'foo']"
