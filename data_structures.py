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
    def __init__(self,*args):
        if len(args) == 1 and type(args[0]) == list:
            self.ls = args
        else:
            self.ls = [*args]
    
    def __str__(self):
        s = "["
        for i in self.ls:
            s += " " + str(i) + " ,"
        s = s[:-1] + "]"
        return s
    
    def __repr__(self):
        s = "["
        for i in self.ls:
            s += " " + str(i) + " ,"
        s = s[:-1] + "]"
        return s
    
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
    
    def lshift(self,times):
        for i in range(times):
            self.ls = self.ls[1:] + [self.ls[0]]
    
    def rshift(self,times):
        for i in range(times):
            self.ls = [self.ls[-1]] + self.ls[:-1]

    # Just String,Int And Boolean Are Handled Here.
    def count_deep(self,tar):
        if not (type(tar) == int or type(tar) == str or type(tar) == bool):
            raise TypeError("CountDeep Just Supports String,Integer And Boolean Types.")
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
    
    def shift_index(self,index,left_shift=True,how_many=1):
        for _ in range(how_many):
            if not left_shift:
                if index == len(self.ls) - 1:
                    self.rshift(1)
                else:
                    self.ls[index],self.ls[index + 1] = self.ls[index + 1],self.ls[index]
                index = (index + 1) % len(self.ls)
            else:
                if index == 0:
                    self.lshift(1)
                else:
                    self.ls[index],self.ls[index - 1] = self.ls[index - 1],self.ls[index]
                index = (index - 1) % len(self.ls)
    
    # Start Of List Methods #

    def __getitem__(self,o: object) -> int:
        if type(o) == int:
            return self.ls[o]
        else:
            raise TypeError("Type Of Index Must Be int.")

    def __setitem__(self,k: object,v: object) -> None:
        if type(k) == int:
            self.ls[k] = v
        else:
            raise TypeError("Type Of Index Must Be int.")
    
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
    
    def append(self,obj):
        self.ls.append(obj)
    
    def sort(self,key="",reverse=False):
        if key:
            self.ls.sort(key=key,reverse=reverse)
        else:
            self.ls.sort(reverse=reverse)
    
    # End Of List Methods #

    # List Operators + Some Beautiful Things :) #

    def __eq__(self, o: object) -> bool:
        if type(o) == list:
            return self.ls == o
        if type(o).__name__ == "shist":
            return self.ls == o.ls
    
    def __gt__(self,o: object) -> bool:
        if type(o) == list:
            return len(self.ls) > len(o)
        if type(o).__name__ == "shist":
            return self.ls > o.ls
    
    def __lt__(self,o: object) -> bool:
        if type(o) == list:
            return len(self.ls) < len(o)
        if type(o).__name__ == "shist":
            return self.ls < o.ls

    def __ge__(self,o: object) -> bool:
        if type(o) == list:
            return len(self.ls) >= len(o)
        if type(o).__name__ == "shist":
            return self.ls >= o.ls
    
    def __le__(self,o: object) -> bool:
        if type(o) == list:
            return len(self.ls) <= len(o)
        if type(o).__name__ == "shist":
            return self.ls <= o.ls
    
    def __add__(self,o: object) -> bool:
        if type(o) == list:
            return self.ls + o
        if type(o).__name__ == "shist":
            return self.ls + o.ls
        if type(o) == int or type(o) == float:
            tar = []
            for i in self.ls:
                tar.append(i + o)
            return tar
    
    def __sub__(self,o: object) -> bool:
        if type(o) == list:
            tar = []
            for i in self.ls:
                if not i in o:
                    tar.append(i)
            return tar
        if type(o).__name__ == "shist":
            tar = []
            for i in self.ls:
                if not i in o.ls:
                    tar.append(i)
            return tar
        if type(o) == int or type(o) == float:
            tar = []
            for i in self.ls:
                tar.append(i - o)
            return tar
    
    # *
    def __mul__(self,o: object) -> list:
        if type(o) == int:
            return self.ls * o
        else:
            raise TypeError("Type Must Be int.")
    
    # **
    def __pow__(self,o: object) -> bool:
        return list(map(lambda elem:elem ** o,self.ls))
    
    # /
    def __truediv__(self,o: object) -> bool:
        return list(map(lambda elem:elem/o,self.ls))
    
    # //
    def __floordiv__(self,o: object) -> bool:
        return list(map(lambda elem:elem//o,self.ls))
    
    # <<
    def __lshift__(self,o: object) -> bool:
        if type(o) == int:
            return self.lshift(o)
        elif type(o) == dict:
            for i,j in o.items():
                if type(i) == int:
                    self.shift_index(i,True,j)
                elif type(i) == tuple or type(i) == list or type(i) == set:
                    for a in i:
                        self.shift_index(a,True,j)
                else:
                    raise TypeError("Type Must Be int,tuple,list or set.")
        else:
            raise TypeError("Type Must Be int Or dict.")
    
    # >>
    def __rshift__(self,o: object) -> bool:
        if type(o) == int:
            return self.rshift(o)
        elif type(o) == dict:
            for i,j in o.items():
                if type(i) == int:
                    self.shift_index(i,False,j)
                elif type(i) == tuple or type(i) == list or type(i) == set:
                    for a in i:
                        self.shift_index(a,False,j)
                else:
                    raise TypeError("Type Must Be int,tuple,list or set.")
        else:
            raise TypeError("Type Must Be int Or dict.")
                

    # %
    def __mod__(self,o: object) -> bool:
        return list(map(lambda elem:elem % o,self.ls))