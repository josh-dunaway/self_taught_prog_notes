print('''
 ██████╗██╗  ██╗ █████╗ ██████╗ ████████╗███████╗██████╗      ██╗██████╗ 
██╔════╝██║  ██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗    ███║╚════██╗
██║     ███████║███████║██████╔╝   ██║   █████╗  ██████╔╝    ╚██║ █████╔╝
██║     ██╔══██║██╔══██║██╔═══╝    ██║   ██╔══╝  ██╔══██╗     ██║██╔═══╝ 
╚██████╗██║  ██║██║  ██║██║        ██║   ███████╗██║  ██║     ██║███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═╝╚══════╝
                                                                         ''')

print('''
Syntax for creating a class:
    [name]: [suites]
where: 
    name is name of class and 
    suites are class' suites
    
suites:
   methods (defined in same way as functions, 
    except 'self' in first parameter slot)
   
constructor:
    def __init__(self, [other_parameters]:
        [code run when class instantiated]
        ''')


class Rectange:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

    def print_attributes(self):
        print(', '.join('%s: %s' % item for item in vars(self).items()))


rect = Rectange(5, 5)
rect.print_attributes()
rect.change_size(10, 7)
rect.print_attributes()

print('''
 ██████╗██╗  ██╗ █████╗ ██╗     ██╗     ███████╗███╗   ██╗ ██████╗ ███████╗███████╗
██╔════╝██║  ██║██╔══██╗██║     ██║     ██╔════╝████╗  ██║██╔════╝ ██╔════╝██╔════╝
██║     ███████║███████║██║     ██║     █████╗  ██╔██╗ ██║██║  ███╗█████╗  ███████╗
██║     ██╔══██║██╔══██║██║     ██║     ██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  ╚════██║
╚██████╗██║  ██║██║  ██║███████╗███████╗███████╗██║ ╚████║╚██████╔╝███████╗███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝
                                                                                   ''')

print('''
1 - define class called Apple with four instance variables
''')


class Apple:
    def __init__(self, w, c, s, j):
        self.weight = w
        self.color = c
        self.sweetness = s
        self.juiciness = j


print('''
2 - create Circle class with method called area that calculates
and returns its area. then create Circle obj, call area on it, and print result.
Use python's pi function in the built-in math module
''')


class Circle:
    def __init__(self, r=1):
        self.radius = r

    def area(self):
        import math
        return math.pi * (self.radius ** 2)


circle = Circle(5)
print('area = {}'.format(circle.area()))

print('''
3 - create Triangle class with method called area that calculates and returns area.
Create Triangle object, call area on it, print result)
''')


class Triangle:
    def __init__(self, b=1, h=1):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height) / 2


triangle = Triangle(12, 3)
print('area = {}'.format(triangle.area()))

print('''
4 - make Hexagon class with method calculate_perimeter.
Create Hexagon, call calculate_perimeter, print result
''')


class Hexagon:
    def __init__(self,
                 s1=1,
                 s2=1,
                 s3=1,
                 s4=1,
                 s5=1,
                 s6=1):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def calculate_perimeter(self):
        return (self.side1 + self.side2 + self.side3 
        + self.side4 + self.side5 + self.side6)

hexagon = Hexagon(5, 5, 4, 5, 2, 5)
print('perimeter = {}'.format(hexagon.calculate_perimeter()))