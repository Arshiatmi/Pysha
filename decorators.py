import sys
import datetime
from inspect import signature

from data_structures import PyshaString


def retry(count, exceptions='*'):
    """
This Function Acts As A Decorator For Retring On Some Exceptions That You Define.
For Example You Can Set That If Running A Function Have HTTPConnectionError, Function
Retries And Run Again. You Can Define Count Of Retries Too.

Agrs : 
* count : Count Of Retries For Target Function
* exceptions : a list contains all exceptions that should retry on them or '*' character
            means all of exceptions should be retried.

    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            tested = 0
            while tested < count:
                try:
                    func(*args, **kwargs)
                except:
                    if exceptions == '*':
                        tested += 1
                        continue
                    inf = sys.exc_info()
                    if inf[0] in exceptions:
                        tested += 1
                        continue
                    else:
                        raise
        return wrapper
    return decorator


def ignore(exceptions='*'):
    """
This Function Acts As A Decorator For Ignoring Some Exceptions That You Define.
For Example You Can Set That If Running A Function Have ZeroDivisionError, Function
Ignore The Problem And Not Make Exception.

Agrs : 
* exceptions That Should Be A List Of Exceptions You Want To Ignore Or '*' Character
* That Means All Of Exceptions Must Ignore.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                if exceptions == '*':
                    return
                inf = sys.exc_info()
                if inf[0] in exceptions:
                    return
                else:
                    raise
        return wrapper
    return decorator


def once(func):
    """
This Function Acts As A Decorator For Process Initialization. Every Function
That Has This Decorator Will Be Called Before The Main Function Once. Important
Thing Is That Function Must Not Have Any Arguments Or Kwarguments To Be Called.

Important Thing : 
* This Function Will Be Called Before The Main Function.
* Function Must Not Have Any Arguments Or Kwarguments To Be Called.
    """
    func()

    def decorator(*args, **kwargs):
        func(*args, **kwargs)
    return decorator


def timer(string):
    """
This Function Acts As A Decorator For Check Spent Time On Executing Functions.
Args:
Gets One Argument For Printing Format. For Example :
```
    @time("Spent Time Was _T_")
    def test():
        return True
```
And Output Of This Code After Calling test() Will Be Something Like That : 
    ```Spent Time Was 0:00:00.100404```

Important Parameters : 
* _T_ : Will Be Replaced With [Hour]:[Minute]:[Second].[MiliSecond]
* _H_ : Will Be Replaced With [Hour]
* _M_ : Will Be Replaced With [Minute]
* _S_ : Will Be Replaced With [Second]
* _MS_ : Will Be Replaced With [MiliSecond]

Important :
**You Can Escape All Of This Parameters With (\)**

    """
    def sec(func):
        def run(*args, **kwargs):
            start = datetime.datetime.now()
            func(*args, **kwargs)
            end = datetime.datetime.now()
            ans = PyshaString(string)
            s = ans.replace_with_escape("_T_", str(end - start))
            s = s.replace_with_escape("_S_", str(end - start).split(':')
                                      [2].split('.')[0].strip())
            try:
                s = s.replace_with_escape("_MS_", str(end - start).split(':')
                                          [2].split('.')[1].strip())
            except:
                s = s.replace_with_escape("_MS_", "0")
            s = s.replace_with_escape("_M_", str(
                end - start).split(':')[1].strip())
            s = s.replace_with_escape("_H_", str(
                end - start).split(':')[0].strip())
            print(s)
        return run
    return sec

class interface:
    """
You Can Make Interfaces ( Inspired From PHP ! ) .
In Fact You Can Define An Structure That All Of Classes That Extends That Interface Must Have This
Structure That You Defined.

You Can Use It Like Decorator. For Example : 

```
@interface
class UserStructure:
    name = None
    family = None
    username = None
    password = None

@interface(UserStructure)
class SpecialUsers:
    name = None
    family = None
    username = None
    password = None

@interface(UserStructure)
class Users:
    name = None
    family = None
    username = None
    password = None
```
    """
    instances: dict = {}

    def __init__(self, target_class):
        self.is_parent_interface = False
        try:
            class_name = target_class.__name__
        except:
            try:
                class_name = target_class._class.__name__
            except:
                raise ValueError("You Should Pass className.")
        if (type(target_class) == type):
            self._class = target_class
            self.is_parent_interface = True
            interface.instances[class_name] = self
        else:
            self._parent = target_class
            self.is_parent_interface = False

    def __get_class_attrs(self):
        method_list = [method for method in dir(
            self._class) if method not in dir(self)]
        return method_list

    def __get_class_attr_types(self):
        attrs = self.__get_class_attrs()
        method_list = [func for func in attrs if callable(
            getattr(self._class, func))]
        variables = [func for func in attrs if not callable(
            getattr(self._class, func))]
        return method_list, variables

    def __is_ok(self):
        if not self._parent:
            return True
        attrs = self.__get_class_attr_types()
        parent_attrs = self._parent.__get_class_attr_types()
        for methods in attrs[0]:
            this_sig = signature(getattr(self._class, methods))
            this_params = this_sig.parameters
            parent_sig = signature(getattr(self._parent._class, methods))
            parent_params = parent_sig.parameters
            if (this_params) == parent_params:
                continue
            return f"Parameters Of Methods Are Not Equal (child( {' '.join(this_params)} ) , parent( {' '.join(parent_params) }))"
        for variable in parent_attrs[1]:
            if self.has_attr(variable):
                continue
            return f"Variable Problem. ( {variable} Not Defined In Child Class )"
        return True

    def has_attr(self, attr):
        """
            Checks If This Class Has Specific Attribute Or Not. ( Checks For Every Attribute Like Methods,Variables,... )
        """
        if attr in self.__get_class_attrs():
            return True
        return False

    def is_allowed_structure(self):
        """
            Checks If Has Allowed Structure Or Not.
        """
        is_ok = self.__is_ok()
        if is_ok != True:
            return is_ok
        return True

    def __call__(self, *parent_args, **parent_kwds):
        if self.is_parent_interface:
            return self._class(*parent_args, **parent_kwds)
        else:
            def wrapper(*args, **kwds):
                self._class = parent_args[0]
                interface.instances[self._class.__name__] = self._class
                try:
                    is_allowed = self.is_allowed_structure(self._parent)
                except:
                    raise ValueError("There Is No Interface With This Name.")
                if is_allowed != True:
                    raise ValueError(
                        f"This Class Does Not Extends From {self._class.__name__} Interface. {is_allowed}")
                return self._class(*args, **kwds)
            return wrapper

