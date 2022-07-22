print('''
██╗  ██╗    ██████╗ ██╗██╗     ██╗      █████╗ ██████╗ ███████╗
██║  ██║    ██╔══██╗██║██║     ██║     ██╔══██╗██╔══██╗██╔════╝
███████║    ██████╔╝██║██║     ██║     ███████║██████╔╝███████╗
╚════██║    ██╔═══╝ ██║██║     ██║     ██╔══██║██╔══██╗╚════██║
     ██║    ██║     ██║███████╗███████╗██║  ██║██║  ██║███████║
     ╚═╝    ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                               
 ██████╗ ███████╗     ██████╗  ██████╗ ██████╗                 
██╔═══██╗██╔════╝    ██╔═══██╗██╔═══██╗██╔══██╗                
██║   ██║█████╗      ██║   ██║██║   ██║██████╔╝                
██║   ██║██╔══╝      ██║   ██║██║   ██║██╔═══╝                 
╚██████╔╝██║         ╚██████╔╝╚██████╔╝██║                     
 ╚═════╝ ╚═╝          ╚═════╝  ╚═════╝ ╚═╝                     
                                                               ''')

print('''
Encapsulation - refers to two concepts:
    1) objects group variables (state) and methods (for altering state
        or doing calculations that use state) in a single unit - the object))
    2) hiding class's internal data to prevent the client (code outside the
        class that uses the object) from directly accessing it)

    note: Python does not have 'private' variables and methods... seems like
    there is some 'honor' system in place.. if a variable of method begins with
    underscore, then that means its probalby 'unsafe' and that the client
    should use at his/her own risk
''')

print('''
Abstraction - process of taking away or removing characteristics from something
    in order to reduce it to a set of essential characteristics.
''')

print('''
Polymorphism - the ability to present the same interface for different underlying
    forms (data types). Interface = function or method

    note: will mostly likely show example of this in challenges below
''')

print('''
Inheritance - child classes can inherit methods and variables from a parent class.

example:

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def print_size(self):
        print('...')
        
class Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(20,20)
print(a_square.area())

Child class can also override parent methods by simply redefining them
''')

print('''
Composition - not one of the four pillars but....

describes a 'has a' relationship.... when an object has 
    another object stored as a variable)
''')

print('''
**********************************CHALLENGES**********************************
''')

print('''
1 - create a Rectangle and Square class with method calculate_perimeter.
create Rectangle and Square objects and call method on both of them

note: I first used inheritance but then decided it wasn't necessary
for the example
''')

class Shape:
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return (2 * self.width) + (2 * self.length)

class Square(Shape):
    def __init__(self, w):
        self.width = w
    def change_size(self, amount):
        self.width += amount
    def calculate_perimeter(self):
        return 4 * self.width

rect = Rectangle(5, 10)
sqr = Square(20)

shapes = [rect, sqr]

for Rectangle in shapes:
    print('perimeter = {}'.format(Rectangle.calculate_perimeter()))

print('''
2 - define method in Square class called change_size that allows us to pass 
a number that increase/decrease each side of a Square by that number

note: see changes above
''')

print('sqr.change_size(-10) = {}'.format(sqr.width))
print('sqr.calculate_perimeter() = {}'.format(sqr.calculate_perimeter()))

print('''
3 - create class called Shape. Define method called what_am_i() that prints
    "I am a shape" when called. change Square and Rectangle class above to
    inherit from Shape, create Square and Rectangle objects, and call new method
''')

print('rect.what_am_i() >> ', end='')
rect.what_am_i()
print('sqr.what_am_i() >> ', end='')
sqr.what_am_i()

print('''
4 - create class called Horse and class Rider. use composition to
model horse that has a rider)
''')

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

rider_tom = Rider('Tom')
horse_spot = Horse('Spot', rider_tom) 

print(horse_spot.rider.name)