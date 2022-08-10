class Node:
   """
   class to create nodes
   """
    def __init__(self,data):
       self.data=data
       self.next=None

class LinkedList:
    """
     A Linked List class with a single head node
     """
    def __init__(self):
        """
        Instantiates a singly-linked list with an empty head node.
        arguments: head (None by default)
        Outputs: None
        """
        self.head=None

    def add(self,data):
        """
        This method will add a node at the start of the linked list
        arguments :data
        returns:None
        """
        node=Node(data)
        node.next=self.head
        self.head=node


class HashTable:
    """
    HashTable class will have multiple methods, set, get,
    contains, keys and hash.
    It is a data structure that uses keys and values to store
    data to provide easy and fast access to its items.
    """

    def __init__(self, size=1024):
        """
        Takes one arguments:
        size: int
        returns: None
        """
        self.size = size
        self.buckets = [None] * size
        self.keys = []

    def hash(self, key):
        """
        This method will take a key as an argument and returns
        the index in the collection of buckets for that key.
        """

        hash_key = 0
        for char in key:
            hash_key += ord(char)
        return hash_key * 283 % self.size


    def set(self, key, value):
        """
          this method will  hash the key and set the value and key pair in the buckets,
          also handling the collisions as needed
          Return: Nothing
          Arguments: Key , value
        """

        hashed_key = self.hash(key)
        if self.buckets[hashed_key] == None:
            self.buckets[hashed_key] = LinkedList()
        self.keys.append(key)
        self.buckets[hashed_key].add((key, value))

    def get(self, key):
        """
        Used to find the value that is associated with the passed key.
        Arguments: key
        retern: referenced value by passed key
        """
        hashed_key = self.hash(key)
        ll = self.buckets[hashed_key]
        current = ll.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        return None

    def contains(self, key):
        """
        This method will take a key
        returns : True if the key exists in the hashmap, and False if it doesn't exist
        """
        idx = self.hash(key)
        bucket = self.buckets[idx]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False



    def key(self):
        """
        this method will return a collections of all the keys in hashmap as an object
        """
        return self.keys