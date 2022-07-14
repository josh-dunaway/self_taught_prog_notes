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

print('''
syntax for basic while loop:
while [expression]:
    [code_to_execute]''')

print('''
Break statement terminates a loop. Useful for continuously asking
user for input until they type a terminating key:

user_inputs = []
while True:
    print("Type q to quit")
    a = input("Type whatever you want and press enter:")
    if a == 'q':
        break
    user_inputs.append(a)

print('Your inputs = {}'.format(user_inputs))
''')

user_inputs = []
while True:
    print("Type q to quit")
    a = input("Type whatever you want and press enter:")
    if a == 'q':
        break
    user_inputs.append(a)

#note to self - start using format strings more
print('Your inputs = {}'.format(user_inputs))

print('''
another way of using user-inputed terminator for infinite loop:

while input('repeat? y or n): ') != 'x':
    for i in range(5):
        print(i)
        ''')

while input('print 0-4? (y or n): ') != 'n':
    for i in range(5):
        print(i)

print('''
Continue keyword ends current iteration and moves on to next
rather than quitting the loop completely like break does.

for i in range(1,6):
    if i == 3:
        continue
    print(i)''')

for i in range(1,6):
    if i == 3:
        continue
    print(i)

ch7_vocab = {'Loop': '''A piece of code that continually executes instructions
until a condition defined in the code is satisfied.''',
              'Iterating': '''Using a loop to access each item in an iterable.''',
              'For-loop': '''A loop used to iterate through an iterable, like a
string, list, tuple, or dictionary.''',
              'Index variable': '''A variable that holds an integer representing
an index in an iterable.''',
              'While-loop': '''A loop that executes code as long as an expression
evaluates to True.''',
              'Infinite loop': '''A loop that never ends.''',
              'Break-statement': '''A statement with the keyword break in it used
to terminate a loop.''',
              'Continue-statement': '''A statement with the keyword continue used to
stop the current iteration of a loop and move on to the net iteration of it.''',
              'Outer loop': '''A loopo with a nested loop inside it.''',
              'Inner loop': '''A loop nested in another loop.'''}

def print_numbered_dict_keys(dictionary: dict) -> None:
    for i, k in enumerate(dictionary):
        print('{}. {}'.format(i+1, k))

def get_nth_key(dictionary: dict, index = 0):
    if index < 0:
        index += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == index:
            return key
    raise IndexError('dictionary index out of range')

def get_value_from_key(dictionary: dict, key):
    if key in dictionary:
        return key
    return None

def print_formatted_definition(key: str, value: str) -> None:
    print('{} - {}'.format(key, value))

print_numbered_dict_keys(ch7_vocab)
while True:
    user_selection = input('Select vocab for definition (q to quit): ')
    if user_selection == 'q':
        break
    if user_selection not in range(len(ch7_vocab) + 1):
        print('Invalid selection. Enter 1 thru {}:'.format(len(ch7_vocab)))
        continue
    else:
        key = get_nth_key(ch7_vocab, user_selection - 1)
        value = get_value_from_key(ch7_vocab, key)
        print_formatted_definition(key, value)
    print_numbered_dict_keys(ch7_vocab)
