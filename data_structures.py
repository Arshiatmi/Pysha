from typing import TypeVar
from exceptions import *

ListOrDict = TypeVar('ListOrDict', list, dict)


class Stack:
    def __init__(self, inf=1, capacity=0):
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

    def push(self, elem):
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
    def __init__(self, inf=1, capacity=0):
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

    def add(self, elem):
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


class PyshaList(list):
    def __str__(self):
        s = "["
        for i in self:
            s += " " + str(i) + " ,"
        s = s[:-1] + "]"
        return s

    def __repr__(self):
        s = "["
        for i in self:
            s += " " + str(i) + " ,"
        s = s[:-1] + "]"
        return s

    def lshift(self, times):
        for _ in range(times):
            self = self[1:] + [self[0]]

    def rshift(self, times):
        for _ in range(times):
            self = [self[-1]] + self[:-1]

    # Just String,Int And Boolean Are Handled Here.
    def count_deep(self, tar):
        if not (type(tar) == int or type(tar) == str or type(tar) == bool):
            raise TypeError(
                "CountDeep Just Supports String,Integer And Boolean Types.")
        if not any(list(map(lambda x: type(x) == list or type(x) == set, self))):
            if type(tar) == str and any(list(map(lambda x: type(x) == str, self))):
                counted = 0
                for index in range(len(self)):
                    try:
                        counted += self[index].count(tar)
                    except:
                        continue
                return counted
            return self.count(tar)
        indexes = Stack()
        lists = Stack()
        target_list = self
        current_index = 0
        counted = 0
        while current_index != len(self):
            has_new_list = False
            for i in target_list:
                if type(tar) == type(i):
                    if tar == i:
                        counted += 1
                elif type(tar) != list:
                    indexes.push(current_index)
                    lists.push(target_list)
                    target_list = i.copy()
                    current_index = 0
                    has_new_list = True
                    break
                current_index += 1
            if not has_new_list:
                current_index = indexes.pop() + 1
                target_list = lists.pop()
        return counted

    def shift_index(self, index, left_shift=True, how_many=1):
        for _ in range(how_many):
            if not left_shift:
                if index == len(self) - 1:
                    self.rshift(1)
                else:
                    self[index], self[index +
                                      1] = self[index + 1], self[index]
                index = (index + 1) % len(self)
            else:
                if index == 0:
                    self.lshift(1)
                else:
                    self[index], self[index -
                                      1] = self[index - 1], self[index]
                index = (index - 1) % len(self)

    def __setitem__(self, k: int, v: object) -> None:
        if type(k) == int:
            if k > len(self):
                self.extend([None for _ in range(k - len(self) + 1)])
                super(PyshaList, self).__setitem__(k, v)
            else:
                super(PyshaList, self).__setitem__(k, v)
        else:
            raise TypeError("Type Of Index Must Be int.")

    # List Operators + Some Beautiful Things :) #

    def __add__(self, o: object) -> list:
        if type(o) == list:
            cp = self.copy()
            cp.extend(o)
            return cp
        else:
            tar = []
            for i in self:
                try:
                    tar.append(i + o)
                except:
                    tar.append(str(i) + " " + str(o))
            return tar

    def __iadd__(self, o: object) -> list:
        if type(o) == list:
            self.extend(o)
        else:
            for i in self:
                try:
                    self.append(i + o)
                except:
                    self.append(str(i) + " " + str(o))

    def __sub__(self, o: object) -> list:
        if type(o) == list:
            tar = []
            for i in self:
                if not i in o:
                    tar.append(i)
            return tar
        if type(o) == int or type(o) == float:
            tar = []
            for i in self:
                try:
                    tar.append(i - o)
                except:
                    pass
            return tar

    # **
    def __pow__(self, o: object) -> list:
        return list(map(lambda elem: elem ** o, self))

    # /
    def __truediv__(self, o: object) -> list:
        return list(map(lambda elem: elem/o, self))

    # //
    def __floordiv__(self, o: object) -> list:
        return list(map(lambda elem: elem//o, self))

    # <<
    def __lshift__(self, o: object) -> list:
        if type(o) == int:
            return self.lshift(o)
        elif type(o) == dict:
            for i, j in o.items():
                if type(i) == int:
                    self.shift_index(i, True, j)
                elif type(i) == tuple or type(i) == list or type(i) == set:
                    for a in i:
                        self.shift_index(a, True, j)
                else:
                    raise TypeError("Type Must Be int,tuple,list or set.")
        else:
            raise TypeError("Type Must Be int Or dict.")

    # >>
    def __rshift__(self, o: object) -> list:
        if type(o) == int:
            return self.rshift(o)
        elif type(o) == dict:
            for i, j in o.items():
                if type(i) == int:
                    self.shift_index(i, False, j)
                elif type(i) == tuple or type(i) == list or type(i) == set:
                    for a in i:
                        self.shift_index(a, False, j)
                else:
                    raise TypeError("Type Must Be int,tuple,list or set.")
        else:
            raise TypeError("Type Must Be int Or dict.")

    # %
    def __mod__(self, o: object) -> list:
        return list(map(lambda elem: elem % o, self))


"""
In PyshaString You Have Lots Of Methods To Do Some Things.
"""


class PyshaString(str):
    def inside(self, data_to_search: ListOrDict, search_mode="key", return_type=bool):
        """
        In This Function You Can Search That If A String Exists In Dict ( Or Inside Of All Elements ).
        Or If A String Exists In List And All Of Its Elements.

        Args :
            data_to_search ->  Data That Wanted To Search In That. For Example
                                Search In List : ["test", "some", "Hello World"] Or
                                Search In dict : {"test": "Hello World", "some": "Hello World"} 
                                -> ( search_mode must be "value" or "both" in dict input )
                                if string is Hello It Will Return True !

            search_mode ->  If You Passed A Dictionary You Can Choose Between "key" Or "value"
                            Or "all"/"both" To Search In Both Of Them. It Does Not Do Anything If
                            You Passed A List.

            return_type ->  If You Passed A Dictionary You Can Choose Between bool and dict or ...
                            if you pass bool, it will return True or False If It Finds Your String.
                            if you pass dict, it will return a dict with key and value of found element.
                            if you pass pass anything else, it will return oposite of search_mode. For
                            Example If You passed "key" And You Found Your String, It Will Return "value".

        """
        if type(data_to_search) == list:
            if self in data_to_search:
                return True
            for i in data_to_search:
                if self in i:
                    return True
            return False
        elif type(data_to_search) == dict:
            ans = {}
            if return_type == dict:
                ans = {}
            else:
                ans = []
            for i, j in data_to_search.items():
                if search_mode == "key":
                    if self in i:
                        if return_type == bool:
                            return True
                        elif return_type == dict:
                            ans[i] = j
                        else:
                            ans.append(j)
                elif search_mode == "value":
                    if self in j:
                        if return_type == bool:
                            return True
                        elif return_type == dict:
                            ans[i] = j
                        else:
                            ans.append(j)
                else:
                    if self in j or self in i:
                        if return_type == bool:
                            return True
                        elif return_type == dict:
                            ans[i] = j
                        else:
                            ans.append(j)
            if return_type != bool:
                return ans
            return False
        else:
            raise TypeError("Type Must Be list Or dict.")

    """
        In This Function You Can Search That an String Contains Some Other String From A List.

        Args :
            data_to_search ->  Strings That You Want To Search For. For Example
                                Search In List : [" ", ":", ","] And If Your String Is 
                                "Hello, Im Arshia" It will Return 5 Thats Index Of ",".
                                If Your String Is "Arshia:Hey" It Will Return 6 Thats Index Of ":".

            return_type ->  You Can pass int To Return Index Of Found String. Or Pass Other
                            Things Like str To Return Found String.

    """

    def find_first(self, data_to_search: list, return_type=int):
        for c, i in enumerate(self):
            if i in data_to_search:
                if return_type == int:
                    return c
                else:
                    return i

    """
        This Function Is Exactly find_first But It Will Return Last Index Of Found String.

        Args :
            data_to_search ->  Strings That You Want To Search For. For Example
                                Search In List : [" ", ":", ","] And If Your String Is 
                                "Hello, Im Arshia" It will Return 10 Thats Index Of " ".
                                If Your String Is "Arshia:Hey" It Will Return 6 Thats Index Of ":".

            return_type ->  You Can pass int To Return Index Of Found String. Or Pass Other
                            Things Like str To Return Found String.

    """

    def find_last(self, data_to_search: list, return_type=int):
        for c, i in enumerate(self[::-1]):
            if i in data_to_search:
                if return_type == int:
                    return len(self) - c - 1
                else:
                    return i

    """
        In This Function You Can Replace An Array With Another Array ! ( in a string )

        Args :
            data_to_replace ->  Data That You Wanted To Be Replaced For Example If Data Is 
                                ["Hello", "World"] And replace_with Argument Is ["Hi", "There"]
                                All Of "Hello" And "World" Will Be Replaced With "Hi" And "There".

            replace_with ->  Described In data_to_replace Argument.

    """

    def replace_array(self, data_to_replace: list, replace_with: list):
        for c, i in enumerate(data_to_replace):
            self = self.replace(i, replace_with[c])
        return self

    """
        This Is replace_array But You Can Pass Dictionary To Replace With.

        Args :
            data_to_replace ->  A Dictionary Of Data To Replace. For Example 
                                {"Hello": "Hi", "World": "There"} Will Replace "Hello" With "Hi"
                                And "World" With "There". ( All Of String )

    """

    def replace_dict(self, data_to_replace: dict):
        for j, i in data_to_replace.items():
            self = self.replace(j, i)
        return self

    """
        This Function Will Check If A List Of Strings Exists In Another String. In Specific
        Part Of It Or Not. It Will Get a Part Of String And Will Check It With A List Of Strings.

        Args :
            data_to_replace ->  A List Of Data That You Want To Check If Exists In Another String.
                                
            line_start ->  Line Start Number ( Starts With 0 )

            line_end ->  Line End Number ( Starts With 0 )

            start_index ->  Start Index Number ( Starts With 0 )

            end_index ->  End Index Number ( Starts With 0 )

    """

    def exists(self, data_to_search: list, line_start=-1, line_end=-1, start_index=-1, end_index=-1):
        if line_start == -1:
            line_start = 0
        if line_end == -1:
            line_end = len(self)
        if start_index == -1:
            start_index = 0
        if end_index == -1:
            end_index = len(self)
        data_to_search = '\n'.join(
            data_to_search.split('\n')[line_start:line_end])[start_index:end_index]
        for i in data_to_search:
            if i in self:
                return True
        return False

    """
        This Function Will Replace Any String That You Want But You Can Define Some Parts
        Not To Replace With Define Escapes !

        Args :
            string_to_find ->  String That You Want To Search For In String.
                                
            to_replace ->  String That You Want To Be Replaced With string_to_find.

            escape_char ->  Escape Character That You Want To Define. ( Default Is \ Character )

            remove_escapes ->  You Can Define That After Replacing, Escape Characters Should Remove
                                Or Not. ( Default Is False )
    """

    def replace_with_escape(self, string_to_find, to_replace, escape_char='\\', remove_escapes=False):
        last_index = self.find(string_to_find, 0)
        while last_index != -1:
            if self[last_index - 1] == escape_char:
                if remove_escapes:
                    self = self[:last_index-1] + self[last_index:]
                last_index = self.find(string_to_find, last_index)
                continue
            self = self[:last_index] + to_replace + \
                self[last_index + len(string_to_find):]
            last_index = self.find(string_to_find, last_index + 1)
        return self

    """
        This Function Is "<<=" Operator. It Will Append Another String To The End Of This String.
    """

    def __ilshift__(self, other):
        self = self + other
        return self

    """
        This Function Is "+=" Operator. It Will Append Another String To The End Of This String.
    """

    def __iadd__(self, other):
        self = self + other
        return self

    """
        This Function Is ">>=" Operator. It Will Append Another String To Start Of This String.
    """

    def __irshift__(self, other):
        self = other + self
        return self

    """
        This Function Is "<<" Operator. It Will Append Another String To The End Of This String. ( Not Set )
    """

    def __lshift__(self, other):
        return self + other

    """
        This Function Is ">>" Operator. It Will Append Another String To Start Of This String. ( Not Set )
    """

    def __rshift__(self, other):
        return other + self

    """
        This Function Is "-=" Operator. It Will Remove A String From This String.
    """

    def __isub__(self, other):
        self = self.replace(other, "")
        return self

    """
        This Function Is "-" Operator. It Will Remove A String From This String. ( Not Set )
    """

    def __sub__(self, other):
        return self.replace(other, "")


class PyshaDict(dict):
    @property
    def inverse(self):
        return PyshaDict({v: k for k, v in self.items()})

    @inverse.setter
    def inverse(self, value):
        value = {v: k for k, v in value.items()}
        self.update(value)

    def __invert__(self):
        return self.inverse

    def __isub__(self, other):
        del self[other]
        return self

    def __sub__(self, other):
        ans = self.copy()
        del ans[other]
        return ans
