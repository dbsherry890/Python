# Last in, First out (LIFO)
# append, pop

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def reverse_string(my_string):
    # accumulator pattern. Start with empty bucket that you fill
    reversed_string = ""

    s = Stack()
    for letter in my_string:
        s.push(letter)

    while not s.is_empty():
        reversed_string += s.pop()

    return reversed_string


my_string = "gninraeL nIdekniL htiw tol a nraeL"
print(reverse_string(my_string))
