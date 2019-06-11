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

# 7.1.3. Manual String Formatting
for x in range(1, 11):
    print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

'12'.zfill(5)
'-3.14'.zfill(7)
'-003.14'
'3.14159265359'.zfill(5)

# 7.1.4.Old string Formatting
import math
print('The value of pi is approximately %5.3f.' % math.pi)

# 7.2. Reading and Writning FIles
f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()
f.closed

f.close()
f.read()

# 7.2.1.Methods of File objects
f = open('workfile', 'r')
# f.read()
# f.read()
f.readline()
f.readline()

f = open('workfile', 'r')
for line in f:
    print(line, end = ' ')

f = open('workfile', 'r+')
f.write('This is a test\n')

value = ('the answer', 42)
s = str(value) # convert the tuple to string
f.write(s)

f = open('workfile','rb+')
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)

# 7.2.2. Saving structed data sith json
import json
json.dumps([1, 'simple', 'list'])

dict = [1, 'simple', 'list']
f = open('test.json', 'w')
json.dump(dict, f, indent=1)

# 8.Errors and Exceptions
# 8.1.Syntax Errors
while True print('Hello world')

# 8.2. Exceptions
10 / (1/0)
4 + spam*3
'2' + 2

# 8.3.Handling Exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# 8.4. Raise Exceptions
raise NameError('HiThere')

raise ValueError # shorthand for 'raise ValueError()'

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

# 8.5. User-defined Exceptions
class Error(Exception):
    """Base class for exceptions  in the modules"""
    pass

class InputError(Error):
    """Exception raised for errors in the input

    Attributes:
        expression -- input expression in which the error occured
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when operation attempts a state transition that's not
    allowed

    Attributes:
        previous -- state a beginning of transition
        next -- attempted new statement
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

    8.9. Defining Clean-up Actions
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye world!')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("devision by zero!")
    else:
        print("result is", result)
    finally:
        print("executing final clause")

divide(2,1)
divide(2,0)
divide("2","1")

# 8.7. Predifined Clean-up Actions
for line in open("myfile.txt"):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

# 9.Classes
# 9.1. A Word About Names and objects
# 9.2. Python Scopes and Namespaces
# 9.2.1. Scopes and Namespaces Example
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

# 9.3. A First Look at Classes
# 9.3.1. Class Difinition Syntax
# 9.3.2. Class objects
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return "hello world"

x =  MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

# 9.3.3. Instance Objects

x = MyClass()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# 9.3.4. Methos Objects
x.f()
xf = x.f
while True:
    print(xf())

# 9.3.5. Class and Instance Variables
class Dog:

    kind = 'canine'         # class variable shared by all instance

    def __init__(self, name):
        self.name = name

d = Dog("Fibo")
e = Dog("Buddy")
d.kind      # shared by all dogs
e.kind      # shared by all dogs
d.name      # unique to d
e.name      # unique to e

class Dog:
    tricks = []             # mistaken use of a class variable

    def __init__(self, trick):
        self.trick = trick

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fibo")
e = Dog("Buddy")
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                   # unexpetedly shared by all dogs

class Dog:
    def __init__(self, trick):
        self.trick = trick
        self.tricks = []         # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fibo")
e = Dog("Buddy")
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
e.tricks

# 9.4. Random Remarks
# Fuction defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# 9.5. Inheritance
# 9.5.1. Multiple Inheritance

# 9.6. Private Variables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update       # private copy of original update() method

class MappingSubClass(Mapping):

    def update(self, key, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(key, values):
            self.items_list.append(item)

# 9.7. Odds and Ends
class Employee:
    pass

john = Employee()   # Create an empty employee record

# Fill the fields of the record
john.name = 'john Doe'
john.dept = 'computer lab'
john.salary = 1000

# 9.8. Iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')


s = 'abc'
it = iter(s)
it
next(it)
next(it)
next(it)
next(it)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

# 9.9. Generators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# 9.10. Generator Expressions
sum(i*i for i in range(10))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))

unique_words = set(word for line in page    for word in line.split())

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

# 10. Brief Tour of the Standard Library
# 10.1 Operating System Interface
import os
os.getcwd()
os.chdir('/server/accesslog')
os.system('mkdir today')

import os
dir(os)

help(os)
import shutil
shutil.copyfile('data.db', 'archive.db')

# 10.2. File Wildcards
import glob
glob.glob("*.py")

# 10.3. Command Line Arguments
import sys
print(sys.argv)
# 10.4. Error Output Redirection and Program Termination
sys.stderr.write('Warning, log file not found starting a new one\n')
# 10.5. String Pattern Matching
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')

# 10.6. Mathematics
import math
math.cos(math.pi / 4)
math.log(1024, 2)

import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()
random.randrange(6) # random integer chosen from range(6)


import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# 10.7. Internet Access
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8') # Decoding the binary data to text
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

import smtplib
server = smtplib.SMTP('localhost')


# 10.8. Dates and Times
# dates are easily constructed and formatted
from datetime import date
now = date.today()
now

now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.')
# dates support calendar arithmetic
birthday = date(1973, 12, 5)
age = now - birthday
age.days

# 10.9. Data Compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# 10.10. Performance Measurement
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

Timer('a,b = b,a', 'a=1; b=2').timeit()

# 10.11 Quality Control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

import unittest

class TestStatisticalFUnctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() # Calling from the comand line invokes all tests

# 10.12 Batteries included

# 11. Brief Tour of the Standard Library ---Part ifmain II
# 11.1. Output Formatting
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
import pprint
t = [[[['black','cian'], 'white', ['green','red']],[['magenta','yellow'],'blue']]]
pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that returns a list of strings instead of one big string with newlines to separate the wrapped lines."""
print(textwrap.fill(doc,width=40))

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()   # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)
locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)

# 11.2. Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

11.3.Working with Binary Data Record Layouts
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()
start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header

# 11.4. Multi-threading
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished backgroud zip of:', self.infile)

background = AsyncZip('fibo.py', 'fiboarchive.zip')
background.start()
print('the main program continues to run in foreground')

background.join()
print('Main program waited until background was done.')

# 11.5. Logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shtting down')

# 11.6. Weak References
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)               # create reference
d = weakref.WeakValueDictionary()
d['primary'] = a        # dose not create a reference
d['primary']            # fetch the object if it is still alive

del a                   # remove the one reference
gc.collect()            # run garbage collection right away

d['primary']            # entry was automatically removed
