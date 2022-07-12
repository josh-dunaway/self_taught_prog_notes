def square(x):
    return x*x

def square_range(lower, upper):
    while lower <= upper:
        print(square(lower))
        lower += 1

square_range(0, 10)
square_range(11, 3)
square_range(3, 3)

#small example of Docstring
def even_odd(x):
    """
    Returns str "even" if x is even or "odd" if x is odd
    :param x: int
    :return: str
    """
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'

print(even_odd(17))

#some basic exception handling
def ask_user_for_division():
    try:
        x = input("type 1st number:")
        y = input("type 2nd number:")
        x = int(x)
        y = int(y)
        print(x/y)
    except (ZeroDivisionError, ValueError):
        print("Invalid Input.")

ask_user_for_division()

#page 65 challenges
#1 - see top of page

#2
def print_string(string):
    print(string)

print_string("what is the point of writing this function?")

#3
def add_5(num1, num2, num3, num4 = 0, num5 = 0):
    return num1 + num2 + num3 + num4 + num5

print(add_5(3, 4, 5))
print(add_5(3, 4, 5, 1, 1))

#4
def half(x):
    return x / 2

def quadruple(x):
    return x * 4

num1 = half(14)
num2 = quadruple(num1)
print(num2)

#5
def string_to_float(string):
    try:
        result = float(string)
        return result
    except ValueError:
        print("Invalid Parameter")

print(string_to_float(0))
