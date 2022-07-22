import keyword
import statistics
import random
import math

print('''
   ____ _      ___            __  __           _       _           
  / ___| |__  ( _ )          |  \/  | ___   __| |_   _| | ___  ___ 
 | |   | '_ \ / _ \   _____  | |\/| |/ _ \ / _` | | | | |/ _ \/ __|
 | |___| | | | (_) | |_____| | |  | | (_) | (_| | |_| | |  __/\__ \ 
  \____|_| |_|\___/          |_|  |_|\___/ \__,_|\__,_|_|\___||___/
                                                                   
''')

print('''
import modules using "import" keyword and use functions from module using
[module_name].[code]''')

print('''
**************************example**************************

import math
print(math.pow(2,3)) >> {}'''
      .format(math.pow(2, 3)))

print('''
**************************example**************************

import random
print(random.randint(0,100)) >> {}'''
      .format(random.randint(0, 100)))

nums = []
for i in range(15):
    nums.append(random.randint(1, 50))
print('''
**************************example**************************

generate 15 random numbers between 1-50 and store in list nums
import statistics module to find mean, median, mode

nums = {}
statistics.mean(nums) >> {}
statistics.median(nums) >> {}
statistics.mode(nums) >> {}'''
      .format(
          nums,
          statistics.mean(nums),
          statistics.median(nums),
          statistics.mode(nums)
      )
      )

print('''
**************************example**************************

import keyword

keyword.iskeyword("for") >> {}
keyword.iskeyword("football" >> {}'''
      .format(
          keyword.iskeyword("for"),
          keyword.iskeyword("football")
      )
      )

print('''
**************************example**************************

create module 'ch8_hello.py', import it, and use code from it...
there will be a function defined, and just some runnable code
(both inside and outside of condition described below)

runnable code will execute when the module is imported unless wrapped in:

if __name__== "__main__:
    [code]\n''')
    
print('''import ch8_hello''')
import ch8_hello

print('''\nch8_hello.print_hello()''')
ch8_hello.print_hello()

print('''
**************************exercise 1**************************

Call a different function from the statistics module:
I'm going to generate a list of 50 random numbers from 1-20
and print multimode of list\n''')

list = []
for i in range(50):
    list.append(random.randint(1,20))

print('list = {}\n'.format(list))

print('statistics.multimode(list) >> {}'
.format(statistics.multimode(list)))

print('''
**************************exercise 2**************************

Create module named 'cubed' with a function that takes a number
as a parameter, and returns the number cubed. import and call
the function from this module.
''')
import ch8_cubed
print('ch8_cubed.cube(8) >> {}\n'.format(ch8_cubed.cube(8)))