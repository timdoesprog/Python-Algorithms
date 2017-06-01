# 01.06.2017

import random


class minHeap:

    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self.bubbleUp(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return False
        if len(self.heap) < 2:
            return self.heap.pop()
        self.swap(0, len(self.heap) - 1)
        minimum = self.heap.pop()
        self.bubbleDown(0)
        return minimum

    def bubbleUp(self, index):
        if index == 0:
            return
        parentIndex = self.getParent(index)
        # if item smaller, swap with parent
        if self.heap[index] < self.heap[parentIndex]:
            self.swap(index, parentIndex)
            self.bubbleUp(parentIndex)

    def bubbleDown(self, index):
        leftChild = self.getLeftChild(index)
        rightChild = self.getRightChild(index)

        if self.hasLeftChild(index) and self.hasRightChild(index):
            # if smaller than children just return
            if self.heap[index] < self.heap[leftChild] and self.heap[index] < self.heap[rightChild]:
                return
            # swap index with smaller of its children
            if self.heap[leftChild] < self.heap[rightChild]:
                self.swap(index, leftChild)
                self.bubbleDown(leftChild)
            else:
                self.swap(index, rightChild)
                self.bubbleDown(rightChild)
        elif self.hasRightChild(index):
            if self.heap[index] > self.heap[rightChild]:
                self.swap(index, rightChild)
                self.bubbbleDown(rightChild)
        elif self.hasLeftChild(index):
            if self.heap[index] > self.heap[leftChild]:
                self.swap(index, leftChild)
                self.bubbleDown(leftChild)

    def getParent(self, index):
        return int((index - 1) / 2)

    def getLeftChild(self, index):
        return index * 2 + 1

    def getRightChild(self, index):
        return index * 2 + 2

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def hasRightChild(self, index):
        return self.getRightChild(index) < len(self.heap)

    def hasLeftChild(self, index):
        return self.getLeftChild(index) < len(self.heap)


def sort(array):
    heap = minHeap()
    for num in array:
        heap.insert(num)
    for i in range(len(array)):
        array[i] = heap.pop()


array = [random.randint(1, 10000) for i in range(100000)]
print(array)
sort(array)
print(array)

# heap = minHeap()
# for i in range(2):
#     heap.insert(random.randint(1, 20))
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())
# print(heap.heap)
