print('''
 ██████╗██╗  ██╗ █████╗               ███████╗██╗██╗     ███████╗███████╗
██╔════╝██║  ██║██╔══██╗              ██╔════╝██║██║     ██╔════╝██╔════╝
██║     ███████║╚██████║    █████╗    █████╗  ██║██║     █████╗  ███████╗
██║     ██╔══██║ ╚═══██║    ╚════╝    ██╔══╝  ██║██║     ██╔══╝  ╚════██║
╚██████╗██║  ██║ █████╔╝              ██║     ██║███████╗███████╗███████║
 ╚═════╝╚═╝  ╚═╝ ╚════╝               ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝                                                                       
''')

print('************************************************************')

print('''
Python's built-in 'open' function is used to open files.
parameters: 
    string representing file path 
    mode to open file in''')

print('\n************************************************************')

import os
print('''
use Python's built-in 'os' module to build file paths: 
(works regardless of operating system)

import os
os.path.join("Users", "bob", "st.txt") >> {}'''
.format(os.path.join("Users", "bob", "st.txt")))

print('\n************************************************************')

print('''
modes determine actions able to be performed on file. some modes:

"r"     opens file for read only

"w"     opens file for writing only. 
        overwrites file if file exists
        if file does not exist, create new file for writing

"w+"    opens file for reading and writing. 
        overwrites the file if the file exists.
        if the file does not exist, create new file for reading/writing''')

print('\n************************************************************')
        
print('''
preferred way of opening files that automatically closes:

with open(output_files\\test.txt, 'w') as f:
    f.write("Write and automatically close.\n''')

with open('output_files\\test.txt', 'w') as f:
    f.write("Write and automatically close.\n")

print('''
open file we just created in read-only mode: 

with open('output_files\\test.txt', 'r') as f:
    print(f.read())''')

with open('output_files\\test.txt', 'r') as f:
    print(f.read())

print('\n************************************************************')

print('''
If you want to use a value read from file, store in var

my_list.append(f.read())''')

print('\n************************************************************')

print('''
Working with CSV Files - 

Open with with-statement. 
Use csv module method 'writer' to convert from file object to csv object
csv object has 'writerow' method that accepts list)

import csv
with open('output_files\\test.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['one', 'two', 'three'])
    w.writerow(['four', 'five', 'six'])
''')

import csv
with open('output_files\\test.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['one', 'two', 'three'])
    w.writerow(['four', 'five', 'six'])

print('''
reading from csv file - 
open using with-statement and 'r' as mode
call csv 'reader' method, passing file object and delimiter
return iterable you can use to access each row in file

with open('output_files\\test.csv', 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(','.join(row))
''')

with open('output_files\\test.csv', 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(','.join(row))