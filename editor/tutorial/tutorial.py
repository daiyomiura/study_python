# 4.7.2. Keyword Argument
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if yo put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "I")

parrot(1000)                                            # 1 positional argument
parrot(voltage=1000)                                    # 1 keyword Argument
parrot(voltage=1000000, action='VOOOOOOM')              # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')           # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword

# invalid
parrot()                      # required argument missing
parrot(voltage=5.0, 'dead')   # non-keyword argument after a keyword argument
parrot(110, voltage=220)        # duplicate value for the same Argument
parrot(actor='John Cleese')     # unknown keyword argument

def function(a):
    pass

function(0, a=0)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop(
    "Limburger", "It's very runny, sir.",
    "It's reay very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch"
)

# 4.7.3. Arbitrary Argument Lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

# 4.7.4. Unpacking Argument Lists
list(range(3, 6))           # normal call with separate arguments
args = [3, 6]
list(range(*args))

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if yo put", voltage, "volts through it.", end=' ')
    print("-- E's", state, "I")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# 4.7.5. Lambda Expressions
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)

pairs = [(1, 'one'),(2, 'two'),(3, 'three'),(4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

# 4.7.6. Documentation Strings
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
# 4.7.7. FUnction Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

# 4.8. Intermezzo: Coding style

# 5. Data Structures
# 5.1. More on Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)   # Find next banana starting position 4.
fruits.reverse()
fruits
fruits.append('grape')
fruits
fruits.sort()
fruits
fruits.pop()
fruits

# 5.1.1. Using LIsts as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
stack.pop()
stack
stack.pop()
stack

# 5.1.2. Using Lists as Queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")                               # Terry arrives
queue.append("Graham")                              # Graham arrives
queue.popleft()                                     # The first to arrive now leaves
queue.popleft()                                     # The second to arrive now leaves
queue

# 5.1.3. List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

squares

squares = list(map(lambda x: x**2, range(10)))
squares

squares = [x**2 for x in range(10)]
squares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x**2 for x in vec]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# call a method on each element
freshfruit = ['  banana', '  loganberry', 'passion fruit   ']
[weapon.strip() for weapon in freshfruit]
# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

from math import pi
[str(round(pi, i)) for i in range(1, 6)]

# 5.1.4. Nested List Complehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
[[row[i] for row in matrix] for i in range(4)]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append[row[i]]
    transposed.append(transposed_row)

transposed

list(zip(*matrix))

# 5.2. The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a
del a[2:4]
a
del a[:]
a
del a # delete entire variables

# 5.3. Tuples and Sequences
t = 12345, 54321, 'hello!'
t[0]
t
# Tuples may be nestd:
u = t, (1,2,3,4,5)
u
# Tuples are immutable:
t[0] = 88888;
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

empty = ()
singleton = 'hello', # <-- note trailing comma
len(empty)
len(singleton)
singleton
x, y, z = t

# 5.4. Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed
'orange' in basket  # fast membership testing
'crabgrass' in basket

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a   # unique letters in a
a - b   # letters in a but not in b
a | b   # letters in a or b or both
a & b   # letters in both a and b
a ^ b   # letters in a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'}
a

# 5.5. Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['quido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127
tel
list(tel)
sorted(tel)
'quido' in tel
'jack' not in tel

dict([('sage', 4139), ('quido', 4127), ('jack', 4098)])

{x: x**2 for x in (2, 4, 6)}
dict(sape=4139, quido=4127, jack=4098)

# 5.6. Looping Techniques
knights = {'gallahad' : 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data

# 5.7. More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null

# 5.8. Comparing Sequences and Other Types
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 3]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'bb')) < (1, 2, ('aa', 'bb'), 4)

# 6.Modeles
# ライブラリのパスを追加する
import sys
# カレントディレクトリからのインポートは以下の様に書く
from . import fibo
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

fib = fibo.fib
fib(500)

# 6.1.More on Modules
from fibo import fib, fib2
fib(500)
from fibo import *
fib(500)

import fibo as fib
fib.fib(500)

from fibo import fib as fibonacci
fibonacci(500)

# 6.1.1.Executing modules as scripts

# 6.2.Standard Modules
import sys
sys.ps1
sys.ps2
sys.ps1 = 'C> '
print('Yuck!')

# 6.3. The dir() Function
import fibo, sys
dir(fibo)
dir(sys)
a = [1,2,3,4,5]
import fibo
fib = fibo.fib
dir()

import builtins
dir(builtins)

# 6.4. Packages

# 6.4.1. Importing * From Package

# 6.4.2. Intra-package References

# 6.4.3. Packages in Multiple Directories

# 7.Input and Output
# 7.1. Fancier output Formatting
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)

s = 'Hello, World'
str(s)
repr(s)
str(1/7)
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + "..."
print(s)
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# The argument to repr() may any Python object:
repr((x, y, ('spam', 'eggs')))

# 7.1.1. FOrmatted String Literals
import math
print(f'The value of pi is approximatery {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

7.1.2. The String format() method
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}'.format(
    food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
