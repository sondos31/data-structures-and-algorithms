class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.max = 0

    def pre_order(self):
        """returns array of values ordered root, left, right"""
        output = []
        def _walk(root):
            if not root:
                return 'empty tree'

            output.append(root.value)
            _walk(root.left)
            _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        """returns array of values ordered left, root, right"""
        output = []
        def walk(root):
            """navigates tree"""
            if not root:
                return
            walk(root.left) # check left
            output.append(root.value) # root
            walk(root.right) # check right
        walk(self.root)
        return output

    def post_order(self):
        """returns array of values ordered left, right, root"""
        output = []
        def walk(root):
            """navigates tree"""
            if not root:
                return
            walk(root.left)
            walk(root.right)
            output.append(root.value)
        walk(self.root)
        return output

    def max_tree(self):
        """func without any arguments that depends on recurrsion to return maximum value stored in the tree."""
        if not self.root:
            return 'Tree is Empty'

        def _walk(node):
            if node.value > self.max:
                self.max = node.value
            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)

        _walk(self.root)
        return self.max




if __name__ == "__main__":
     tree=BinaryTree()
     tree.root = Node(1)
     tree.root.right = Node(2)
     tree.root.left = Node(3)
     tree.root.right.left = Node(4)
     tree.root.left.left = Node(5)
     tree.root.right.right = Node(6)
     print(tree.pre_order())
     print(tree.in_order())
     print(tree.post_order())

     print(tree.max_tree())



