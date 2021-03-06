# 15.06.2017


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index=0):
        # invalid index
        if index < 0:
            return False
        newNode = Node(data)
        # indert at the front of the list
        if index == 0:
            if not self.head:
                self.head = newNode
            else:
                newNode.next = self.head
                self.head = newNode
            return True
        current = self.head
        for i in range(index - 1):
            if not current or not current.next:
                return False
            current = current.next
        newNode.next = current.next
        current.next = newNode
        return True

    def delete(self, index):
        # invalid index
        if index < 0:
            return False
        # list is empty
        if not self.head:
            return False
        # delete the front of the linked list
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                # index out of bound
                if not current.next or current.next.next:
                    return False
                current = current.next
            current.next = current.next.next

    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


myList = LinkedList()
myList.insert(5)
myList.insert(2)
myList.insert(6, 2)
myList.insert(1, 1)
myList.insert(8, 5)
myList.delete(0)
myList.delete(3)
myList.delete(-2)
myList.delete(100)
myList.printList()
