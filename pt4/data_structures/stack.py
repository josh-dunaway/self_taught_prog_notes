class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

#simple example use case for Stack
def reverse_string(string):
    stack = Stack()
    try:
        for c in string:
            stack.push(c)
    except TypeError:
        return
    reverse = ''
    while(not stack.is_empty()):
        reverse += stack.pop()
    return reverse