# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage =  DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)


    def dequeue(self):
        
        if (self.size > 0):
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size

    def __str__(self):
        return ('length: '+ str(self.size))

q = Queue()
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q.dequeue()) #100
print(q.len()) #2
print(q.dequeue())#101
print(q.len())#1
print(q.dequeue())#105
print(q.len())#0
print(q.dequeue())
print(q.len())#0

