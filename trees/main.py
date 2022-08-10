import numpy as np
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


def printInorder(root):

	if root:
		printInorder(root.left)
		print(root.val),
		printInorder(root.right)

def printPostorder(root):

	if root:

		printPostorder(root.left)
		printPostorder(root.right)
		print(root.val),

def printPreorder(root):

	if root:
		print(root.val),

		printPreorder(root.left)

		printPreorder(root.right)

class BinarySearchTree():
    def __init__(self):
        #self.root = None
        self.root = Node()
        self.size = 0

    def add(self, value):
        self._add(value, self.root)

    def _add(self, value, node):
        if node.value is None:
            node.value = value
        else:
            if value < node.value:
                if node.left is None:
                    node.left = Node()
                self._add(value, node.left)
            else:
                if node.right is None:
                    node.right = Node()
                self._add(value, node.right)


    def contains(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if node is None or node.value is None:
            return False
        else:
            if value == node.value:
                return True
            elif value < node.value:
                return self._contains(value, node.left)
            else:
                return self._contains(value, node.right)


