#1 - 
from multiprocessing.sharedctypes import Value
from random import Random


print('''
#1 - print each item in a list\n''')

list1 = ['The Walking Dead',
            'Entourage',
            'The Sopranos',
            'The Vampire diaries']

print(list1)

#2 - 
print('''
#2 - Print all numbers from 25 to 50\n''')

#if anybody knows a cleaner way of doing this, please tell me
def print_range_in_grid(rng: range, width: int) -> None:
    if width > 0:
        w = 0
        for i in rng:            
            if w == width:
                w = 0
                print()                
            print(i, end=' ')
            w += 1
        print()

rng = range(25, 51)
print_range_in_grid(rng, 6)

#3 -
print('''
#3 - print each item from #1 and their indexes\n''')

def print_dict_keys_with_index(dictionary: dict) -> None:
    for i, k in enumerate(dictionary):
        print(i, k)

print_dict_keys_with_index(list1)

#4 - 
print('''
Write program with infinite loop (with option to type q to quit)
and a list of numbers. Each time through loop, ask user to guess number
on the list and tell them whether or not they guessed correctly.\n''')

import random
rand_numbers = []
for i in range(5):
    rand_numbers.append(random.randrange(20))

print('5 random numbers between 0-20.')

tries = 0

while(True):
    user_guess = input('Guess number between 0 - 20 (q to quit): ')
    tries += 1
    if user_guess == 'q':
        break
    try:
        if int(user_guess) in rand_numbers:
            print('You win in {} tries!'.format(tries))
            break
        else:
            print('Try again')
            continue
    except ValueError:
        continue

#5 - 
print('''
#5 - multiply all numbers in one list with another and append to third list
# 
# I thought it was a little simple so I tweaked it a bit to generate random
# lists and to multiply those together\n''')

def get_product_of_two_lists(lst1: list, lst2: list) -> list:
    #ensure that length of 1st argument >= 2nd argument
    if len(lst2) > len(lst1):
        return get_product_of_two_lists(lst2, lst1)
    tmp_list1 = list(lst1)
    tmp_list2 = list(lst2)
    #pad 2nd list with zeros if shorter length than 1st list
    if len(tmp_list1) > len(tmp_list2):
        for i in range(len(tmp_list1) - len(tmp_list2)):
            tmp_list2.append(0)
    list_of_products = []
    for i in range(len(tmp_list1)):
        try:
            list_of_products.append(tmp_list1[i] * tmp_list2[i])
        except TypeError:
            list_of_products.append(None)
            print('value at index = {} not a number. Result is None'.format(i))
    return list_of_products

rand_lst1 = []
rand_lst2 = []

for i in range(random.randrange(6)):
    rand_lst1.append(random.randrange(12))
for i in range(random.randrange(6)):
    rand_lst2.append(random.randrange(12))

print('rand_list1 = {}'.format(rand_lst1))
print('rand_list2 = {}'.format(rand_lst2))

print('product = {}'.format(get_product_of_two_lists(rand_lst1, rand_lst2)))

lst1 = [5, 'a', 7]
lst2 = [3, 'b', 1]

print('product = {}'.format(get_product_of_two_lists(lst1, lst2)))
