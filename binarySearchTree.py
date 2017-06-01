# 23.01.2017
# Implement a Binary Search Tree Datastructure in Python
# https://www.youtube.com/watch?v=YlgPi75hIBc&t=173s

# Userfunctions:
# nameOfTree = Tree() Instantiate a bst
# nameOfTree.insert(14) Insert a value
# print the Tree structure in different order:
# nameOfTree.preorder()
# nameOfTree.postorder()
# nameOfTree.inorder()

# Tree Class:
#     insert(self, data)
#     find(self, data)
#     preorder()
#     postorder()
#     inorder()

# Node Class (will have recursive functions):
# insert(self, data)
# find(self, data)
# preorder()
# postorder()
# inorder()

# Changed on 22.05.2017
# added get_max()
# added get_min()
# added find_successor()
# added a reference to the parent of a node for the successor method

# Changed on 26.05.2017
# added a function to check if a tree is a BST
# http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
# my own function didn't work out 100% of the time


class Node:
    def __init__(self, val, parent):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

    def insert(self, data):
        # we dont want to allow duplicates in our Tree
        # this checks if the passed in data matches the value
        # of the Node
        if self.value == data:
            return False

        # check if it is less than current Node value
        # then we want to go to the left child
        elif self.value > data:
            # if there already is a left Child we call the function
            # again on that left child to go down the Tree
            if self.leftChild:
                return self.leftChild.insert(data)
            # if not we insert the data as the left child
            # and return True
            else:
                self.leftChild = Node(data, self)
                return True
        # if the data is greater than the current Node
        # we want to insert to the right child of the Node
        else:
            # check again if there is already a right child and
            # call the function on that node
            if self.rightChild:
                return self.rightChild.insert(data)
            # else we want to create a right child Node
            else:
                self.rightChild = Node(data, self)
                return True

    def find(self, data):
        # if the Nodes value matches the data we return True
        # the data is in the Tree
        if self.value == data:
            return True
        # else we check if the data is greater or smaller than
        # than the nodes value

        # if the data is smaller than the current Node
        # we search the left child of the Node
        elif self.value > data:
            # check if there is a child
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False

        # if the data is greater than the current child
        # we search the right child of the Node
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value), end=" ")
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value), end=" ")

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value), end=" ")
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # if there already is a root Node
        # atleast one Node in the tree
        # the data gets past to the Node class and inserted (recursive)
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data, None)
            return True

    def find(self, data):
        # if there is a root Node we go down the Tree
        if self.root:
            return self.root.find(data)
        # else the Tree is empty and return False
        else:
            return False

    def preorder(self):
        print("Pre Order")
        self.root.preorder()
        print()

    def postorder(self):
        print("Post Order")
        self.root.postorder()
        print()

    # prints all values in descending order
    def inorder(self):
        print("In Order")
        self.root.inorder()
        print()

    # returns the maximum value stored in the tree
    def get_max(self, node=None):
        if not node:
            node = self.root
        while node.rightChild:
            node = node.rightChild
        return node

    # returns the minimum value stored in the tree
    def get_min(self, node=None):
        if not node:
            node = self.root
        while node.leftChild:
            node = node.leftChild
        return node

    def find_successor(self, value):
        node = self.root
        while node.value != value:
            if value < node.value:
                node = node.leftChild
            else:
                node = node.rightChild
        if not node.rightChild:
            while node.parent and node != node.parent.leftChild:
                node = node.parent
            if node == self.root:
                return None
            return node.parent
        return self.get_min(node.rightChild)

    def delete(self, value):
        node = self.root
        while node.value != value:
            if value < node.value:
                node = node.leftChild
            else:
                node = node.rightChild
        # if it's a leaf node, delete it
        if not node.leftChild and not node.rightChild:
            self.delete_leaf(self, node)
            return True

        # if the node has only one child we can swap them
        if node.leftChild and not node.rightChild:
            node.leftChild.parent = node.parent
            if node.parent.leftChild == node:
                node.parent.leftChild = node.leftChild
            else:
                node.parent.rightChild = node.leftChild
            return True
        elif node.rightChild and not node.leftChild:
            node.rightChild.parent = node.parent
            if node.parent.rightChild == node:
                node.parent.rightChild = node.rightChild
            else:
                node.parent.leftChild = node.rightChild
            return True

        # otherwise find the direct successor and swap the values
        successor = self.find_successor(value)
        node.value = successor.value
        self.delete_leaf(successor)

    def delete_leaf(self, node):
        if node.parent.leftChild == node:
            node.parent.leftChild = None
        else:
            node.parent.rightChild = None
        return True


def isBST(node):
    INT_MAX = 4294967296
    INT_MIN = -4294967296
    return isBSTUtil(node, INT_MIN, INT_MAX)


def isBSTUtil(node, mini, maxi):
    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.value < mini or node.value > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.leftChild, mini, node.value - 1) and
            isBSTUtil(node.rightChild, node.value + 1, maxi))


# example Tree and function tests


myTree = Tree()
nums = [1, 4, 64, 3, 65, 7, 33, 33, 97, 5, 6, 7, 32, 12, 75, 35]

for num in nums:
    myTree.insert(num)

print(myTree.find(3))
print(myTree.find(100))
myTree.preorder()
myTree.postorder()
myTree.inorder()
print("The maximum is: " + str(myTree.get_max().value))
print("The minimum is: " + str(myTree.get_min().value))
myTree.delete(97)
myTree.inorder()
print(isBST(myTree.root))
