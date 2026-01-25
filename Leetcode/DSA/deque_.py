from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items  # not empty

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()  # similar to pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):  # without this, print() would give "Queue Object"
        return str(self.items)


# keeps code modular. Won't run if imported by another file.
if __name__ == '__main__':
    q = Queue()
    print(q)  # deque([])
    print(q.is_empty())
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)  # deque(['A', 'B', 'C'])
    print(q.dequeue())  # A
    print(q.dequeue())  # B
    print(q)  # deque(['C']
    print(q.size())  # 1
    print(q.peek())  # C
