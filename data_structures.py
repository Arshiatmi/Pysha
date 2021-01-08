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
            return self.__storage.pop()
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
            return self.__storage.pop(0)
        else:
            raise QueueError("Queue Is Empty !")
    
    def display(self):
        return self.storage


class FIFO(Queue):
    pass

class shist:
    def __init__(self,ls: list):
        self.ls = ls
    
    def __str__(self):
        s = "["
        for i in self.ls:
            s += " " + i + " ,"
        s = s[:-1] + "]"
        return s
    
    def __eq__(self, o: object) -> bool:
        if type(o) == list:
            return self.ls == o
        if type(o) == shist:
            return self.ls == o.ls
    
    def pop(self,index=-1):
        return self.ls.pop(index)
    
    def pop_right(self,index=-1):
        return self.ls.pop(index)
    
    def pop_left(self,index=0):
        return self.ls.pop(index)
    
    def push(self,obj):
        self.ls.append(obj)
    
    def push_right(self,obj,index=-1):
        self.ls.insert(index,obj)
    
    def push_left(self,obj,index=0):
        self.ls.insert(index,obj)
    
    def count_deep(self,tar):
        if not any(list(map(lambda x:type(x) == list,self.ls))):
            return self.ls.count(tar)
        obj = Stack()
        lists = Stack()
        target_list = self.ls
        ind = 0
        c = 0
        while ind != len(self.ls):
            b = False
            for i in target_list:
                if type(tar) == type(i):
                    if tar == i:
                        c += 1
                elif type(i) == list and type(tar) != list:
                    obj.push(ind)
                    lists.push(target_list)
                    target_list = i.copy()
                    ind = 0
                    b = True
                    break
                ind += 1
            if not b:
                ind = obj.pop() + 1
                target_list = lists.pop()
        return c
    
    # Start Of List Methods #
    
    def reverse(self):
        self.ls.reverse()
    
    def clear(self):
        self.ls.clear()
    
    def copy(self):
        return self.ls.copy()
    
    def count(self,tar):
        return self.ls.count(tar)
    
    def extend(self,tar):
        self.ls.extend(tar)
    
    def index(self,tar):
        return self.ls.index(tar)
    
    def insert(self,index,obj):
        return self.ls.insert(index,obj)
    
    def remove(self,obj):
        return self.ls.remove(obj)
    
    def sort(self,key="",reverse=False):
        if key:
            self.ls.sort(key=key,reverse=reverse)
        else:
            self.ls.sort(reverse=reverse)
    
    # End Of List Methods #