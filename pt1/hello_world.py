print("Hello, World")
print("No, I am your father.")

import math

#length of a diagonal
l = 4
w = 10
d = math.sqrt(l**2 + w**2)
print(d)

#backward slash to extend code to next line (not common)
print\
("""This is a really really
really really long line of code.""")

#elif (if first if == false, first elif == true will execute)
#if if and no elif == true, then execute else
home = "Germany"
if home == "America":
    print("Hello, America!")
elif home == "Brasil":
    print("Hello, Brasil!")
elif home == "Germany":
    print("Hello, Germany!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")

#Challenges from page 44
#1
print("String 1")
print("String 2")
print("String 3")

#2 (hopefully will learn to handle exception in future)
value = "bad"
if isinstance(value, int) or isinstance(value, float):
    if value < 10:
        print(str(value) + " < 10")
    elif value >= 10:
        print(str(value) + " >= 10")
    else:
        print("error: value of " + str(value) + " invalid.")
else:
    print("value must be a number")

#3 (going to skip the value checking for now, will handle exceptions in future)
value = 17
if value <= 10:
    print(str(value) + " <= 10")
elif value > 10 and value <= 25:
    print("10 < " + str(value) + " <= 25")
else:
    print(str(value) + " > 25")

#4 - divide two variables and prints the remainder
value1 = 17
value2 = 7
print(value1 % value2)

#5 - divide two variables and print quotient
print(value1 // value2)

#6
age = 31
if age < 18:
    print("Not an adult.")
elif age >= 18 and age < 65:
    print("Working age.")
else:
    print("Time to retire!")
