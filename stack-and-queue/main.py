class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:
def __init__(self):
		self.head = Node("head")
		self.size = 0


def push(self, value):
node = Node(value)
node.next = self.head.next
self.head.next = node
self.size += 1

def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value


def getSize(self):
		return self.size
	def isEmpty(self):
		return self.size == 0

def peek(self):.
		if self.isEmpty():
			raise Exception("Peeking from an empty stack")
		return self.head.next.value


class Queue:
    def __init__(self, size):
     self.queue = [None] * size
     self.front = 0
     self.rear = 0
     self.size = size
     self.available = size

def enqueue(self, item):
        if self.available == 0:
            print('Queue Overflow!')
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.available -= 1

def dequeue(self):
        if self.available == self.size:
            print('Queue Underflow!')
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            self.available += 1

def peek(self):.
		if self.isEmpty():
			raise Exception("Peeking from an empty queue")
        return self.items == []





