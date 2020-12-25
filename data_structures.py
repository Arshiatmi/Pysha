from exceptions import *

class Stack:
    def __init__(self,inf=1,capacity=0):
        self.inf = inf
        if inf:
            self.__storage = []
        else:
            self.ind = 0
            self.__storage = [0 for _ in range(capacity)]
            self.capacity = capacity
    
    @property
    def storage(self):
        return self.__storage
    
    def push(self,elem):
        if self.inf:
            self.__storage.append(elem)
        else:
            if self.ind == self.capacity:
                raise StackError("Stack Is Full !")
            self.__storage[self.ind] = elem
            self.ind += 1
    
    def pop(self):
        if self.__storage:
            self.__storage.pop()
        else:
            raise StackError("Stack Is Empty !")
    
    def display(self):
        return self.storage

class LIFO(Stack):
    pass

class Queue:
    def __init__(self,inf=1,capacity=0):
        self.inf = inf
        if inf:
            self.__storage = []
        else:
            self.ind = 0
            self.__storage = [0 for _ in range(capacity)]
            self.capacity = capacity
    
    @property
    def storage(self):
        return self.__storage
    
    def add(self,elem):
        if self.inf:
            self.__storage.append(elem)
        else:
            if self.ind == self.capacity:
                raise QueueError("Queue Is Full !")
            self.__storage[self.ind] = elem
            self.ind += 1
    
    def remove(self):
        if self.__storage:
            self.__storage.pop(0)
        else:
            raise QueueError("Queue Is Empty !")
    
    def display(self):
        return self.storage


class FIFO(Queue):
    pass