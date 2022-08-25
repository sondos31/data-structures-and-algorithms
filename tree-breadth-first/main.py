class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

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

    def breadth_first(self, tree):
            '''  method takes binary tree as argument and return a list of all values in the tree, in the order they were encountered'''
            queue = []
            result = []
            if not tree:
                return 'Tree is empty'
            else:
                if tree:
                    queue.append(tree)
                while queue:
                    current = queue.pop(0)
                    result.append(current.value)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
            return result




if __name__ == "__main__":
     tree=BinaryTree()
     tree.root = Node(4)
     tree.root.right = Node(5)
     tree.root.left = Node(6)
     tree.root.right.left = Node(7)
     tree.root.left.left = Node(8)
     tree.root.right.right = Node(9)
     print(tree.in_order())
     print(tree.pre_order())

     print(tree.breadth_first(tree.root))

