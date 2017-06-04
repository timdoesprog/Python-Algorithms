# 14.05.2017
# First try of coding a trie in python

# 16.05.2017
# Changed the self.children to a dictionary for better performance.
# Could also use a sorted list and insert the new node at the correct postion
# when it is created.


class Node:

    def __init__(self, data):
        self.data = data
        self.isEnd = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        word = word.lower()
        parent = self.root
        for letter in word:
            if letter in parent.children:
                parent = parent.children[letter]
            else:
                parent.children[letter] = Node(letter)
                parent = parent.children[letter]
        parent.isEnd = True

    def insertAll(self, word_list):
        for word in word_list:
            self.insert(word)

    def contains(self, word):
        word = word.lower()
        parent = self.root
        for letter in word:
            if letter in parent.children:
                parent = parent.children[letter]
            else:
                return False
        return parent.isEnd


trie = Trie()
trie.insert("tim")
print(trie.contains("tim"))
print(trie.contains("vale"))
trie.insertAll([
    "this",
    "is",
    "a",
    "lot",
    "of",
    "words",
    "word"
])
print(trie.contains("word"))
print(trie.contains("words"))
