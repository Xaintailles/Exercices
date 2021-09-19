# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:38:19 2021

@author: Gebruiker
"""

"""
This problem was asked by Apple.

Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, 
which inserts an element into the queue, and dequeue, which removes it.
"""

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    # EnQueue item to the queue
    def enQueue(self, x):
        self.s1.append(x)
 
    # DeQueue item from the queue
    def deQueue(self):
 
        # if both the stacks are empty
        if len(self.s1) == 0 and len(self.s2) == 0:
            print("Q is Empty")
            return
 
        # if s2 is empty and s1 has elements
        elif len(self.s2) == 0 and len(self.s1) > 0:
            while len(self.s1):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
 
        else:
            return self.s2.pop()
 
    # Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())