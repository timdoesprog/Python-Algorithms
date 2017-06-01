# 24.02.2017
# implement Max Heap heapsort
# https://www.youtube.com/watch?v=GnKHVXv_rlQ

# Binary Tree if each layer full but the buttom
# every node is equal to or less than their parent

# Insert O(log n)
# Get Max O(1)          biggest number is always the root node at the top
# Remove max O(log n)

# Implented as an array
# 1   2   3   4   5   6   7   8   9   10    index
# 25  16  24  5   11  19  1   2   3   5     value
# get Parent of node:
#   index = 4
#   parent(i) = i / 2 = 2
# get left Child:
#   left(i) = i * 2 = 8
# get right Child:
#   right(i) = i * 2 + 1 = 9

# Operations:
#   Push(Insert)
#   Peek(get mas)
#   Pop(remove max)


class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        # initialize the index of 0, isn't used
        self.heap = [0]
        for item in items:
            # append all items to the end of the list
            # and then float them up
            self.heap.append(item)
            # len(self.heap) - 1 is the length of the heap
            # because we have 0 at index 0
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        # three possibilities
        # heap has two or more items in it
        if len(self.heap) > 2:
            # first swap the highest value with the last value
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            # bubble the new top down to its proper place
            self.__bubbleDown(1)

        # only one item in the heap
        elif len(self.heap) == 2:
            max = self.heap.pop()

        # else we don't have heap at all
        else:
            max = False

        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        # recursive function
        # get parent index
        parent = index // 2
        if index <= 1:
            return
        # when the item is greater than its parent swap them
        # and floatUp again
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        # recursive function
        left = index * 2
        right = index * 2 + 1
        largest = index
        # determine the largest of its children
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        # when the largest value is not at the index
        # swap the two values and call function again
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)


myHeap = MaxHeap([95, 3, 21])
myHeap.push(10)
print(str(myHeap.heap[0:len(myHeap.heap)]))
print(str(myHeap.pop()))
print(str(myHeap.heap[0:len(myHeap.heap)]))
