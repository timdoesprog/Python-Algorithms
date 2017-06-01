# 25.05.2017
# Implement a queue using two stacks in python

# Operations:
# 1. Enqueue: Put something on the queue
# 2. Dequeue: Pop the oldest item of the queue
# 3. Print: Print the oldest item on the queue


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = Node()

    def put(self, value):
        if not self.top:
            self.top = Node(value)
        else:
            temp = self.top
            self.top = Node(value)
            self.top.next = temp

    def pop(self):
        result = self.top
        if not result:
            return None
        self.top = self.top.next
        return result

    def put_node(self, node):
        if not self.top:
            self.top = node
        else:
            pointer = self.top
            self.top = node
            node.next = pointer


class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def enqueue(self, value):
        while self.right_stack.top.value:
            self.left_stack.put_node(self.right_stack.pop())
        self.left_stack.put(value)
        while self.left_stack.top.value:
            self.right_stack.put_node(self.left_stack.pop())

    def dequeue(self):
        return self.right_stack.pop().value

    def print_first(self):
        value = self.right_stack.pop().value
        print(value)
        self.right_stack.put(value)


my_q = Queue()
my_q.enqueue(42)
my_q.enqueue(13)
my_q.enqueue(12)
my_q.print_first()
my_q.dequeue()
my_q.print_first()
