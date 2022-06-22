#Algorithm for insert:
# 1. Declare a head pointer and make it as NULL.
# 2. Create a new node with the given data.
# 3. Make the new node points to the head node.
# 4. Finally, make the new node as the head node.
import math


class Node:
    def _init_(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
        self.count = 0

    def Insert(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.count +=1

    def Includes(self,x):
        try:
            Temp = self.head
            if(Temp.data != x):
                while(Temp.data != x):
                    Temp = Temp.next
                return True
            else:
                return True
        except:
            return False

    def toString(self):
        Temp = self.head
        if (Temp != None):
            list = []
            while (Temp != None):
                print("{",Temp.data,end = " } -> ")
                list.append(Temp.data)
                Temp = Temp.next
            print(end="NULL")
            return list
        else:
            print("The list is empty.")
            return "The list is empty."

    def Append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.count+=1
            return
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newNode
        self.count+=1


    def InsertBefore(self,data,newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            self.count+=1
            return
        current = self.head
        if current.data == data:
            self.Insert(newData)
            return
        while current.next != None:
            nextNode = current.next
            if current.next.data == data:
                current.next = newNode
                newNode.next = nextNode
                self.count += 1
                return
            current = current.next

        if current.data != data:
            raise Exception(f"The Index {data} is not exist in the list")


    def InsertAfter(self,data,newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            self.count+=1
            return
        current = self.head
        while current.next != None:
            nextNode = current.next
            if current.data == data:
                current.next = newNode
                newNode.next = nextNode
                self.count+=1
                return
            current = current.next
        if current.data == data:
            self.Append(newData)
            return
        if current.data != data:
            raise Exception(f"The Index {data} is not exist in the list")


    def kthFromEnd(self,index):
        if index > self.count - 1:
            raise Exception(f"Index {index} is out of range")
        elif index < 0:
            return "Index should be a positive number"
        current = self.head
        innerCount = self.count-1
        # print(innerCount)
        while current.next != None:
            if index == innerCount:
                return current.data
            else:
                current = current.next
                innerCount -=1
                # print(innerCount)
        return current.data



if __name__ == '_main_':
    list = LinkedList()
    list.insert(555)
    list.Append(444)
    str(list.toString())
    print(list)
