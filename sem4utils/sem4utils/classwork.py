# =============================================================================
# PYTHON SEM 4 — REFERENCE FILE
# =============================================================================


# =============================================================================
# PART 1: DATA TYPES & TYPE CONVERSION
# =============================================================================

# a. Functions: type(), int(), float(), str(), bool()
# b. Examples:

print(type(1.56))       # float
print(type(2.0))        # float
print(type(2))          # int
print(type(3-2*1j))     # complex
print(type(2e2))        # float

print(int(5.78))        # float → int
print(float(2))         # int → float
print(str(2))           # int → str
print(bool(3))          # int → bool (non-zero = True)
print(int("3"))         # str → int
print(str(4.2))         # float → str


# =============================================================================
# PART 2: OPERATORS & EXPRESSIONS
# =============================================================================

# a. Functions/Operators: +, -, *, /, //, %, **, =, ==, <, >, and, or, not, in, is
# b. Examples:

print(2*5*(6+9+3))          # arithmetic
print(120-(8/5+(28.4))+(5+7))
print(2**5)                 # exponent
print((3-5j)*(3+5j))        # complex multiplication
print(12345%10)             # modulo (remainder)
print(17//3)                # floor division (quotient)
print(12.50/100*500)        # percentage

print(3.14*5**2)            # area of circle

roll_no, name, height = 400, "Unknown Man", 170.6   # multiple assignment
print(roll_no, name, height)

x, y = 5, 6
print(x == y)               # equality check

x, b = 11, 11
a = 8
print(x < b and x > a)     # logical and

word = "student"
x = "f"
print(x in word)            # membership test

word = "PYTHON"
print("P" in word and "p" not in word)

# identity operators
x = [1, 2, 3, 567, 892, 71]
y = [1, 2, 3, 567, 892, 71]
z = x
print(x is z)              # True — same object
print(x is y)              # False — different objects
print(x is not y)          # True


# =============================================================================
# PART 3: STRINGS
# =============================================================================

# a. Functions: indexing, slicing, startswith(), endswith(), isupper(), islower(),
#    isspace(), isdigit(), isalpha(), isalnum(), upper(), lower(), title(),
#    len(), count(), find(), replace(), format(), in, +, *, raw strings, \t, \n

# b. Examples:

word = "PYTHON"
print(word[0])              # first character
print(word[1])              # second character
print(word[4])              # 5th character
print(word[-1])             # last character
print(word[-2])             # second to last
print(word[0:2])            # start to before 2nd position
print(word[3:])             # 4th position to end
print(word[1:-1])           # 2nd to before last
print(word[-2:])            # last two characters
print(word[0::2])           # every 2nd character from start
print(word[2:]+word[:2])    # rotation
print(word[4:]+word[4:])    # repeated slice

# String methods
str1 = "Introduction to python"
print(str1.startswith("Intro"))     # True
print(str1.startswith("intro"))     # False
print(str1.endswith("Intro"))       # False

print("NAME".isupper())             # True
print("Name".islower())             # False
print(" ".isspace())                # True

print(r"Some\new")                  # raw string — \ not treated as escape
print("My\nname\nis")              # newline
print("This \tis \nPython")        # tab and newline

s1, s2, s3 = "My", "name", "is"
print(s1 + " " + s2 + " " + s3)   # concatenation

print("Name".upper())
print("NAME".lower())
print("Introduction to python".title())     # camel/title case
print(len("python"))                        # length

print("name" in "my name is")              # membership in string

# format string
m = "This is {} and I am {} years old"
print(m.format("Python", "50"))

# More string methods
a = "INTRO TO PYTHON"
b = "intro to python"
c = "50"
d = "abc"
e = "abc50"
g = "python"
l = "This is a goat"

print(len(a))
print(a.count("O"))
print(a.find("O"))          # first index of substring; -1 if not found
print(a.find("o"))
print(l.replace(" is", " was"))
print(g in b)
print(b.startswith(g))
print(b.isdigit())
print(c.isdigit())
print(c.isalpha())
print(e.isalpha())
print(d.isalnum())
print("  ".isspace())

print("50" + "abc")        # concatenation
print("50" * 3)            # repetition

# Formatted certificate string
str16 = "This is to certify that Ms S belongs to Semester 1 of the Statistics department."
print(str16)


# =============================================================================
# PART 4: LISTS
# =============================================================================

# a. Functions: indexing, slicing, append(), insert(), extend(), remove(),
#    pop(), del, clear(), sort(), reverse(), index(), count(), len(), in

# b. Examples:

# --- Creating lists ---
empty = []
squares = [1, 4, 9, 16, 25]
heights = [5.8, 4.9, 6.2, 5.5, 2.3]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
colors = ['red', 'blue', 'green']
Crop = [20.25, 'onion', 50]

# --- Indexing & slicing ---
sq = [4, 9, 16, 25]
print(sq[0])        # first element
print(sq[-1])       # last element
print(sq[1:3])      # second and third elements
print(sq[1:])       # second to last
print(sq[:])        # all elements
sq[0] = 1           # update first element

# --- Nested list ---
student = [['A', 'F', 80], ['B', 'F', 70], ['C', 'M', 79]]
print(student[2])           # third student
print(student[2][1])        # second element of third student

# --- Modifying elements ---
letters[2:5] = ['x', 'y', 'z']
print(letters)

# --- Concatenation ---
numbers = [1, 2, 3]
LN = letters + numbers
print(LN)

# --- append, insert, extend ---
colors1 = ['blue', 'pink']
colors1.append('black')     # add to end
print(colors1)

numbers = [2, 4, 7, 10]
numbers.insert(2, 5)        # insert BEFORE index
print(numbers)

sq1 = [4, 9, 16, 25]
sq2 = [36, 49]
sq1.extend(sq2)             # extend with another list
print(sq1)

empty.append(1)
empty.insert(-1, "wow")     # insert before last index
empty.insert(len(empty), 1) # insert at end
colors.extend(empty)

# --- remove, pop, del, clear ---
x = [1, 5, 6, 9]
x.remove(1)         # remove by value
print(x)

x.pop(0)            # remove by index; default = last
print(x)

empty.remove("wow")
empty.pop()

# del empty[0]      # delete by index (uncomment to use)
# del x             # delete entire list

empty.clear()       # empty the list
print(empty)

# --- sort, reverse ---
colors2 = ['green', 'black', 'pink', 'green']
colors2.sort()
print(colors2)

colors2.reverse()
print(colors2)

heights.sort()
print(heights)

squares.reverse()
print(squares)

# --- index, count ---
print(colors2.index('black'))
print(colors2.count('green'))
print(heights.count(4.9))
print(squares.index(4))

# --- membership ---
print('blue' in colors)
if "green" in colors:
    print("green is in the list")

# create list from string
python_list = list('python')
print(python_list)
print(len(python_list))
print("".join(python_list))     # join back to string


# =============================================================================
# PART 5: DICTIONARIES
# =============================================================================

# a. Functions: accessing keys/values, update(), pop(), popitem(), del, clear(),
#    keys(), values(), items(), get(), len(), in

# b. Examples:

# --- Creating dictionaries ---
my_dict = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
Empty = {}

print(my_dict['a'])
print(type(Empty))

# --- Adding / updating ---
Empty['new'] = 'element'
print(Empty)

Empty['land'] = 'mark'
print(Empty)

d1 = {'A': 'Geeks', 'B': 'For'}
d2 = {'B': 'Geeks', 'C': 'Python'}
d1.update(d2)               # merge d2 into d1 (overwrites shared keys)
d1.update(A='Hello')        # update by keyword argument

# --- Student dictionary ---
student = {'name': 'Unknown Man', 'subject': 'Statistics', 'semester': '4'}
print(student['subject'])

student['subject'] = 'Python'   # update value
student['marks'] = 70           # add new key
student.update(nature='Okay')   # update via method

print('subject' in student)     # check key membership (not value)
print(len(student))             # number of key-value pairs

print(student['marks'])
print(student.get('marks'))     # safer access (returns None if key absent)

print(student.keys())
print(student.values())
print(student.items())

student.pop('nature')           # remove specific key
# del student['nature']         # alternate way

student.popitem()               # remove last inserted key-value pair
student.clear()                 # clear entire dictionary

# --- Monthly crop production dictionary ---
dictionary_crop_prod_per_month = {
    'Jan': 56.7, 'Feb': 78.9, 'Mar': 78.2, 'Apr': 89.0,
    'May': 90.1, 'Jun': 91.2, 'Jul': 92.5, 'Aug': 92.1
}
dictionary_crop_prod_per_month.update(Jun=57.5)     # update existing key
dictionary_crop_prod_per_month.update(Sep=85.2)     # add new key

dictionary_crop_prod2 = {'Oct': 82.2, 'Nov': 67.4, 'Dec': 87.0}

# Transfer all keys from dict2 to dict1
keys_to_transfer = list(dictionary_crop_prod2.keys())
for key in keys_to_transfer:
    value = dictionary_crop_prod2.pop(key)
    dictionary_crop_prod_per_month.update({key: value})

print(dictionary_crop_prod_per_month)


# =============================================================================
# PART 6: SETS
# =============================================================================

# a. Functions: union(), intersection(), difference(), issubset(),
#    issuperset(), isdisjoint(), len()

# b. Examples:

crops_farm1 = {'potato', 'tomato', 'okra', 'sweetpotato'}
crops_farm2 = {'barley', 'wheat', 'jowar', 'bajra', 'potato'}

print(crops_farm1.union(crops_farm2))               # all unique crops
crop_inter = crops_farm1.intersection(crops_farm2)
print(len(crop_inter))                              # common crops count

crop_diff = crops_farm1.difference(crops_farm2)
print(len(crop_diff))                               # crops only in farm1

print(crops_farm1.issubset(crops_farm2))
print(crops_farm1.issuperset(crops_farm2))
print(crops_farm1.isdisjoint(crops_farm2))

# For loop over a set
items = {1, 2, 3, 4}
for item in items:
    print(item)


# =============================================================================
# PART 7: CONDITIONAL STATEMENTS
# =============================================================================

# a. Keywords: if, elif, else
# b. Examples:

a, b = 200, 100

if b > a:
    print("b is greater than a")

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, apple is in the list")
else:
    print("No")

d = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "brand" in d:
    print("Yes, the key is in the dictionary")

# Roots of quadratic — discriminant check
a = int(input("Enter coefficient of second order polynomial = "))
b = int(input("Enter coefficient of first order polynomial = "))
c = int(input("Enter value of constant = "))

if b**2 > 4*a*c:
    print("Roots are real")
elif b**2 < 4*a*c:
    print("Roots are imaginary")
else:
    print("Roots are equal")

# Positive/Negative Even/Odd
a = int(input("Enter a number"))
while True:
    if a > 0:
        if a % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    elif a < 0:
        if a % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")
    else:
        print("Zero")
    break

# Leap year check
Y = int(input("Enter year"))
if Y % 4 == 0 and Y % 100 != 0:
    print("Leap Year")
elif Y % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# Triangle type check
a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or a == c or b == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")


# =============================================================================
# PART 8: WHILE LOOP
# =============================================================================

# a. Keywords: while, break, continue, else
# b. Examples:

count = 1
while count <= 5:
    print(count)
    count += 1

# while-else
n = 1
while n <= 3:
    print(n)
    n += 1
else:
    print("Loop finished normally")

# break
num = 1
while num <= 10:
    if num == 6:
        break
    print(num)
    num += 1

# continue
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)

# while with input
qty = int(input("Enter crop quantity"))
while qty > 0:
    if qty > 100:
        print("Quantity is too large")
        break
    print(qty)
    qty = int(input("Enter crop quantity"))

# factorial using while
n = int(input("Enter a number"))
if n == 0:
    print("1")
else:
    f = 1
    while n > 0:
        f *= n
        n -= 1
    print(f)

# countdown by halving
num = 10
while num > 1:
    print(num)
    num = num / 2

# print list using while
fruits = ["apple", "banana", "cherry"]
a = 0
while a < len(fruits):
    print(fruits[a])
    a += 1


# =============================================================================
# PART 9: FOR LOOP
# =============================================================================

# a. Keywords: for, in, range(), break, continue, else
# b. Examples:

numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

colors = ("red", "green", "blue")
for color in colors:
    print(color)

word = "Python"
for letter in word:
    print(letter)

for i in range(1, 6):
    print(i)

# for over dict
student = {'name': 'Tarun', 'age': '21', 'grade': 'A'}
for key in student:
    print(key)
for value in student.values():
    print(value)
for key, value in student.items():
    print(key, value)

# break — stop at 7
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# continue — skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# search in list using for
c = 0
numbers = [2, 4, 6, 8, 10]
num = int(input("Enter the number = "))
for i in numbers:
    if num == i:
        print("FOUND")
        break
    else:
        c += 1
if c == len(numbers):
    print("NOT FOUND")

# skip vowels
word = "education"
for i in word:
    if i in {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}:
        continue
    else:
        print(i)

# prime check using for-else
n = int(input())
for i in range(2, n // 2, 1):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")


# =============================================================================
# PART 10: FUNCTIONS
# =============================================================================

# a. Keywords: def, return, default arguments, nested functions
# b. Examples:

# Basic function with no parameters
def add():
    a, b = 2, 3
    return a + b
add()

# Function with parameters
def add(a, b):
    c = a + b
    print(c)
add(2, 3)

# Function with return
def sum(a, b):
    c = a + b
    return c
sum(5, 5)

# Default argument
def sum1(a=1, b=2):
    d = a + b
    print(d)
sum1(0, 3)

# Positional arguments
def NameLoc(Name, Location):
    print('Hi, I am ' + Name + ' and I am from ' + Location + '.')
NameLoc('Ayub', 'Bangladesh')
NameLoc('Bangladesh', 'Ayub')

# Optional middle name
def my_name(first_name, last_name, middle_name=""):
    if middle_name:
        print("My name is " + first_name + " " + middle_name + " " + last_name)
    else:
        print("My name is " + first_name + " " + last_name)
my_name("Ayub", "Bacchu")

# Returns only last value from loop
def variable(x):
    for i in x:
        s = i * i
    return s
k = variable([1, 2, 3])
print(k)

# Mean of a list
def mean(x):
    s = 0
    for i in x:
        s = s + i
    m = s / len(x)
    return m
mean([1, 2, 3])

# Function that modifies and returns
def test():
    x = 10
    x += 5
    return x
print(test() + 2)

# Nested function (closure)
def mystery(a):
    def inner(b):
        return a + b
    return inner
result = mystery(10)
print(result(5))

# GCD using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a
print(gcd(48, 18))

# Fibonacci sequence
def fibon(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
fibon(7)

# Count occurrences of x in list
def count_occurences(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count
count_occurences([2, 3, 4, 4, 5, 6, 9, 1], 3)

# Multiplication table
def multiplication_table(n, up_to):
    for i in range(1, up_to):
        print(n * i)
multiplication_table(5, 11)


# =============================================================================
# PART 11: MODULES
# =============================================================================

# a. Modules: math, random
# b. Examples:

import math
import random

# math module
dir(math)
print(help(math.asinh))

x = math.asinh(1)
print(math.degrees(x))

# random module
random.normalvariate(0, 1)
random.gammavariate(5, 1)

# generate 10 normal random values
x = []
for _ in range(10):
    value = random.normalvariate(0, 1)
    x.append(value)
    print(value)

# set seed for reproducibility
random.seed(123)
x = []
for _ in range(10):
    value = random.normalvariate(0, 1)
    x.append(value)
    print(value)


# =============================================================================
# PART 12: NUMPY
# =============================================================================

# a. Functions: np.array(), np.matrix(), np.shape(), np.reshape(),
#    np.zeros(), .ndim, .shape, .T, indexing, slicing

# b. Examples:

import numpy as np

# 1. 1D array from list
x = [1, 2, 3, 4, 9, 4, 0]
print(np.array(x))

# 2. Matrix and shape
y = [[1, 2, 3], [4, 5, 6]]
y = np.matrix(y)
print(np.shape(y))

# 3. 3D reshape
z = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
z = np.reshape(z, (2, 2, 4))
print(np.shape(z))
print(z)

# 4. zeros array
k = np.zeros(24)
print(k.reshape(2, 3, 4))

# alternate: create zeros in desired shape directly
k = np.zeros((2, 3, 4))
print(k)

# 5. reshape and ndmin
c = np.reshape(np.array([1, 2, 3, 4]), (2, 2))
d = np.array([1, 2, 3, 4], ndmin=2)    # alternate
print(c.ndim)
print(c.shape)

# Dimension and shape
A = np.array([[[1, 2, 3, 4]]])
print(A.ndim)
print(A.shape)

B = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(B.ndim)
print(B.shape)
print(B.T)      # transpose

# 3D array indexing
arr = np.array([[[1, 3], [5, 4]], [[9, 6], [3, 6]]])
print(arr.ndim)
print(arr.shape)
print(arr[1, 1, 1])

# Slicing a 2D array
A = np.array(range(9)).reshape(3, 3)
print(A)
print(A[0])         # first row
print(A[:1])        # first row (as 2D)
print(A[0, 1])      # element at row 0, col 1
print(A[0:1, 1:2])  # submatrix slice
print(A[1:-1])      # middle row
