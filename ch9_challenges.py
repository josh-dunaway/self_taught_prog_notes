print('\n*************************CHALLENGE #1*************************')

print('''
find a file on your computer and print its contents using Python

found at https://stackoverflow.com/questions/22939211/
what-is-the-proper-way-to-take-a-directory-path-as-user-input''')

if input('Do you want to open file for reading (y / n)') == 'y':
    import sys
    import os

    user_input = input('Enter path for file: ')

    assert os.path.exists(
        user_input), 'I did not find the file at\n{}'.format(str(user_input))
    with open(user_input, 'r+') as f:
        print(f.read())

print('\n*************************CHALLENGE #2*************************')

print('''
write program that asks user a question, and saves
# answer in file''')

user_answer = input("What is your name?")
with open('output_files\\user_answer.txt', 'w') as f:
    f.write(user_answer)

print('\n*************************CHALLENGE #3*************************')

print('''
take items in list of list and write them to csv file''')

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"], 
          ["Training Day", "Man on Fire", "Flight"]]

import csv

#writing to csv file
with open('output_files\\movies.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    for row in movies:
        w.writerow(row)

#reading from csv file
with open('output_files\\movies.csv', 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(','.join(row))