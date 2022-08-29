import sys
import datetime

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
