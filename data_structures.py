from typing import TypeVar
from exceptions import *

ListOrDict = TypeVar('ListOrDict', list, dict)
ListOrString = TypeVar('ListOrString', list, str)


class Stack:
    """
        The Common Stack Data Structure That You Can Use Here.
    """

    def __init__(self, inf=1, capacity=0):
        """
            Arguements :
                inf=1, # Set If Stack Is Infinite Or Not. Default Is Infinite Stack.
                capacity=0 # Set Capacity In Case Of limited Stack.
        """
        self.inf = inf
        if inf:
            self.__storage = []
        else:
            self.ind = 0
            self.__storage = [0 for _ in range(capacity)]
            if capacity == 0:
                raise ValueError(
                    "If You Set Inf Mode To Limited You Must Set Capacity For Stack.")
            self.capacity = capacity

    @property
    def storage(self):
        return self.__storage

    def push(self, elem):
        """
            Push The Value To Stack
        """
        if self.inf:
            self.__storage.append(elem)
        else:
            if self.ind == self.capacity:
                raise StackError("Stack Is Full !")
            self.__storage[self.ind] = elem
            self.ind += 1

    def pop(self):
        """
            Pop The Value From Stack ( Returns The Removed Value )
        """
        if self.__storage:
            return self.__storage.pop()
        else:
            raise StackError("Stack Is Empty !")

    def display(self):
        """
            Display Stack Data
        """
        return self.storage


class LIFO(Stack):
    """
        You Can Use This Insted Of Stack. All Methods Of Stack Are Available Here.
    """
    pass


class Queue:
    """
        The Common Queue Data Structure That You Can Use Here.
    """

    def __init__(self, inf=1, capacity=0):
        self.inf = inf
        if inf:
            self.__storage = []
        else:
            self.ind = 0
            self.__storage = [0 for _ in range(capacity)]
            if capacity == 0:
                raise ValueError(
                    "If You Set Inf Mode To Limited You Must Set Capacity For Queue.")
            self.capacity = capacity

    @property
    def storage(self):
        return self.__storage

    def add(self, elem):
        """
            Add Value To Queue.
        """
        if self.inf:
            self.__storage.append(elem)
        else:
            if self.ind == self.capacity:
                raise QueueError("Queue Is Full !")
            self.__storage[self.ind] = elem
            self.ind += 1

    def remove(self):
        """
            Remove From Queue ( Returns The Removed Value )
        """
        if self.__storage:
            return self.__storage.pop(0)
        else:
            raise QueueError("Queue Is Empty !")

    def display(self):
        """
            Display The Queue.
        """
        return self.storage


class FIFO(Queue):
    """
        You Can Use This Insted Of Queue. All Methods Of Queue Are Available Here.
    """
    pass


class PyshaList(list):
    """
        PyshaList That Have Some Advanteges To Normal List.
    """

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
        """
            Left Shift In Times That You Specify
        """
        for _ in range(times):
            self = self[1:] + [self[0]]

    def rshift(self, times):
        """
            Right Shift In Times That You Specify
        """
        for _ in range(times):
            self = [self[-1]] + self[:-1]

    # Just String,Int And Boolean Are Handled Here.
    def count_deep(self, tar):
        """
            Deep Count. If You Pass A list Of String, It Will Check If The tar ( Argument That Passed To This Function )
            Is Inside The list itself or is inside the elements of list or not. If you pass a list with complex dimentions
            it will count inside of all of elements even insidest element ! and it will count it for you.
        """
        if not (type(tar) == int or type(tar) == str or type(tar) == bool):
            raise TypeError(
                "CountDeep Just Supports String,Integer And Boolean Types.")
        if not any(list(map(lambda x: type(x) == list or type(x) == set or type(x) == tuple, self))):
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
        """
            You Can Shift Your Array Better That Just lshift And rshift Methods. You Can Define Which Index To
            Shift, Type Of Shift ( left or right ) And how_many To Shift.

            Arguments :
                index, # Index That You Want To Shift
                left_shift=True, # Left Or Right Shift That You Can Specifiy. Default Is Left Shift
                how_many=1 # How Many Shifts That You Want. Default Is One
        """
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
        elif type(k) == tuple:
            self.set_array(k, v)
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

    @staticmethod
    def make_array(dimentions):
        """
            Make Array In Complex Dimentions. You Can Use This Method Like : 
                PyshaList.make_array([1,2,4,5,4,32])
        """
        ans = [None for _ in range(dimentions[-1])]
        for i in dimentions[:-1][::-1]:
            ans = [ans for _ in range(i)]
        return ans

    def set_array(self, dimentions, value):
        """
            Set Array In Complex Dimentions. You Can Use This Method Like : 
                array = PyshaList.make_array([1,2,4,5,4,32]) # Just A Complex Array
                array.set_array([0,2,4,0,4,3],"test")
            Or Like This :
                array[0,2,4,0,4,3] = "test"
            Cool, Right ? :)
        """
        array = self
        for i in dimentions:
            array = array[i]
        array = value
        return array


class PyshaString(str):
    """
        In PyshaString You Have Lots Of Methods To Do Some Things.
    """

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

    def find_first(self, data_to_search: list, return_type=int):
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
        for c, i in enumerate(self):
            if i in data_to_search:
                if return_type == int:
                    return c
                else:
                    return i

    def find_last(self, data_to_search: list, return_type=int):
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
        for c, i in enumerate(self[::-1]):
            if i in data_to_search:
                if return_type == int:
                    return len(self) - c - 1
                else:
                    return i

    def replace_array(self, data_to_replace: list, replace_with: ListOrString):
        """
            In This Function You Can Replace An Array With Another Array ! ( in a string ).
            Its Possible That You Replace An Array Of String With A Single String Too.

            Args :
                data_to_replace ->  Data That You Wanted To Be Replaced For Example If Data Is 
                                    ["Hello", "World"] And replace_with Argument Is ["Hi", "There"]
                                    All Of "Hello" And "World" Will Be Replaced With "Hi" And "There".

                replace_with ->  Described In data_to_replace Argument.

        """
        if type(replace_with) == str:
            for i in data_to_replace:
                self = self.replace(i, replace_with)
        else:
            for c, i in enumerate(data_to_replace):
                self = self.replace(i, replace_with[c])
        return self

    def replace_dict(self, data_to_replace: dict):
        """
            This Is replace_array But You Can Pass Dictionary To Replace With.

            Args :
                data_to_replace ->  A Dictionary Of Data To Replace. For Example 
                                    {"Hello": "Hi", "World": "There"} Will Replace "Hello" With "Hi"
                                    And "World" With "There". ( All Of String )

        """
        for j, i in data_to_replace.items():
            self = self.replace(j, i)
        return self

    def exists(self, data_to_search: list, line_start=-1, line_end=-1, start_index=-1, end_index=-1):
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

    def replace_with_escape(self, string_to_find, to_replace, escape_char='\\', remove_escapes=False):
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

    def __ilshift__(self, other):
        """
            This Function Is "<<=" Operator. It Will Append Another String To The End Of This String.
        """
        self = self + other
        return self

    def __iadd__(self, other):
        """
            This Function Is "+=" Operator. It Will Append Another String To The End Of This String.
        """
        self = self + other
        return self

    def __irshift__(self, other):
        """
            This Function Is ">>=" Operator. It Will Append Another String To Start Of This String.
        """
        self = other + self
        return self

    def __lshift__(self, other):
        """
            This Function Is "<<" Operator. It Will Append Another String To The End Of This String. ( Not Set )
        """
        return self + other

    def __rshift__(self, other):
        """
            This Function Is ">>" Operator. It Will Append Another String To Start Of This String. ( Not Set )
        """
        return other + self

    def __isub__(self, other):
        """
            This Function Is "-=" Operator. It Will Remove A String From This String.
        """
        self = self.replace(other, "")
        return self

    def __sub__(self, other):
        """
            This Function Is "-" Operator. It Will Remove A String From This String. ( Not Set )
        """
        return self.replace(other, "")


class PyshaDict(dict):
    """
        Thats Just Normal Dictionary Just With 2 Or 3 More Option.
        PyshaDict Operators :
            ~myDict # Returns Dictionary Inverse
            myDict - "elem" # Returns Dicionary With Removed "elem" Key.
    """
    @property
    def inverse(self):
        """
            You Can Get inverse Of A Dictionary. For Example Dict -> {"nickname":"MrMegaExpert"}, Inverse -> {"MrMegaExpert":"nickname"}
            You Can Set And Change Dicitonary In Inverse Mode ! You Can Get Inverse Of A Dictionary In 2 Ways :
                myDict.inverse
                ~myDict
        """
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
