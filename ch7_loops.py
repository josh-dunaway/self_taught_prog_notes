print('''
   ___ _       _____             __                       
  / __\ |__   |___  |           / /  ___   ___  _ __  ___ 
 / /  | '_ \     / /   _____   / /  / _ \ / _ \| '_ \/ __| 
/ /___| | | |   / /   |_____| / /__| (_) | (_) | |_) \__ \ 
\____/|_| |_|  /_/            \____/\___/ \___/| .__/|___/
                                               |_|
''')

print('''I already have quite a bit of experience with loops in other programming
languages. I will give basic examples but will mainly only note those things I find
interesting.''')

print('''
**********************************************************************
The info contained between these lines are from the following site:
https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html
This site seems to be a useful one and I will come back to it.
''')

print('''
Iterables that can be iterated with for loop:
- Sequences: lists, tuples, and strings
- Any object with __iter__() method or with __getitem__() method
    that implements Sequence semantics.''')

print('''
Built-in functions that accept iterables as arguments:
- list, tuple, dict, set: construct list, tuple, etc from contents of an iterable
- sum: sum contents of iterable
- sorted: returns a list of the sorted contents of an iterable
- any: returns True and ends the iteration immediately if bool(item) as True for any item
- all: returns True only if bool(item) was True for all items in iterable
- max: returns largest value in iterable
- min: returns smallest value in iterable

example of 'any()' =
print(any((0, None, [], 0))) = ''')
print(any((0, None, [], 0)))

print('''
**********************************************************************''')

print('''
Using a for-loop to change items in a mutable iterable (list, dict, set, NOT tuple)''')
tv = ['The Office', 'Demon Hunter', 'New Girl']
i = 0
print('tv = ')
print(tv)
print('i = 0')
print('''
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
    
print(tv) = ''')
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

print('''
**********************************************************************
Back to an interesting find from this site:
https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html

Iterable Unpacking - Python 'sees' pattern of variables to left of assignment,
and will 'unpack' the iterable. example:

my_list = [7, 9, 11]
x, y, z = my_list
print(x, y, z) = ''')
my_list = [7, 9, 11]
x, y, z = my_list
print(my_list)

print('''
Useful for performing for-loops through iterables-of-iterables. example:

grades = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]

for name, grade in grades:
    print(name)
    print(grade)
    print()

= ''')

grades = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]

for name, grade in grades:
    print(name)
    print(grade)
    print()

print('''View this page for solution to providing too few variables for
number of iterables, 'PEP 3132 - Extended Iterable Unpacking':
https://peps.python.org/pep-3132/#specification''')

print('''
Enumeration - should be used (in conjunction with iterator unpacking)
whenever it is necessary to track iteration count of a for-loop.
simple example:

for entry in enumerate("abcd"):
    print(entry) = ''')
for entry in enumerate("abcd"):
    print(entry)

print('''
Useful example is for tracking indices in iterable. example, finding None
values in a list:

none_indices = []

for iter_cnt, item in enumerate([2, None, -10, None, 4, 8]):
    if item is None:
        none_indices.append(iter_cnt)

print(none_indices) = ''')
none_indices = []

for iter_cnt, item in enumerate([2, None, -10, None, 4, 8]):
    if item is None:
        none_indices.append(iter_cnt)

print(none_indices)

print('''
**********************************************************************
Back to the book!''')

