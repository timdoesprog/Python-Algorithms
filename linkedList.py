# 24.02.2017
# Linked List in Python
# broken at the moment, 24.02.2017

# Every Node has two attributes
# data and pointer to the next Node

# Functions:
#   get_size()      will be a variable
#   find(data)      will start at the root and go down the List
#   add(data)       add to the start
#   remove(data)    first find and then change pointers


class Node(object):
    def __init__(self, data, nextNode= None):
        self.data = data
        self.next_node = nextNode

    def get_next(self):
        return self.next_node

    def set_next(self, nextNode):
        self.next_node = nextNode

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True

            else:
                prev_noce = this_node
                this_node = this_node.get_next()

        # data is not in the list
        return False

    def find(self, data):
        this_node = self.root

        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                self.root = this_node.get_next()
        return None


# doesn't work will have to investigate
myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)

print(myList.remove(12))
print(myList.find(5))
