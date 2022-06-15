# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


# Iterative function to return the k'th node from the end in a linked list
def findKthNode(head, k):
    curr = head

    # move `k` nodes ahead in the linked list
    for i in range(k):
        # return if `k` is more than the total number of nodes in the list
        if curr is None:
            return None
        curr = curr.next

    # move the `head` and `curr` parallelly till `curr` reaches the end of the list
    while curr:
        head = head.next
        curr = curr.next

    # `head` will now contain the k'th node from the end
    return head


if __name__ == '__main__':

    # input keys
    keys = [1, 2, 3, 4, 5]

    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    k = 2
    node = findKthNode(head, k)

    if node:
        print(node.data-1)
