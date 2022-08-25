
class Node:
    def __init__(self, value=None):
        self.value = value
        self.child  = []


class kTree:
    def __init__(self, root=None):
        self.root = root
    def show_all_values(self):
        all_values = []
        def check_values(node):
            all_values.append(node.value)
            if node.child:
                for child in node.child:
                    check_values(child)
        check_values(self.root)
        return all_values


def fizz_buzz_tree(kTree):
    def _walk(node):
        if node.child :
            for i in node.child :
                node.value = str(node.value)
                if i.value % 3 == 0 and i.value % 5 == 0:
                    i.value = "FizzBuzz"
                elif i.value % 3 == 0:
                    i.value = "Fizz"
                elif i.value % 5 == 0:
                    i.value = "Buzz"
                else:
                    i.value = str(i.value)

    _walk(kTree.root)
    return(kTree)

if __name__ == "__main__":
    tree = kTree()
    tree.root = Node(2)
    tree.root.left = Node(10)
    tree.root.right = Node(15)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    tree.root.right.left = Node(4)



    new = fizz_buzz_tree(tree)
    print(new)
