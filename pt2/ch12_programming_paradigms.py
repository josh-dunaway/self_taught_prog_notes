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