import time
from typing import Callable, TypeVar
from os import mkdir, makedirs, rmdir
from shutil import rmtree
from colors import *
from exceptions import *
import re
import readchar
import sys
from security import *


NoneOrStr = TypeVar('NoneOrStr', None, str)
NoneOrStrOrInt = TypeVar('NoneOrStrOrInt', None, str, int)
ListOrString = TypeVar('ListOrString', list, str)


def colorprompt(prompt: str, out=sys.stdout, char_color=fore["reset"]):
    """
This Will Act Like Input. But Characters That User Enters Will Be Colored :)
Args :
* prompt      ->   The Text For Print And Wait For Input.

* out         ->   Just Standard Output. DO NOT TOUCH THIS :/

* char_color  ->   The Color Of Character. Each Character Will Have This 
                Color.

    """
    out.write(prompt)
    out.flush()
    password = ""
    while True:
        ch = str(readchar.readchar(), encoding='UTF-8')
        if ch == '\r':
            break
        elif ch == '\b':
            out.write('\b \b')
            password = password[0:len(password)-1]
            out.flush()
        elif ch == "\x03":
            print("\n")
            raise KeyboardInterrupt("You Pressed Ctrl+C")
        else:
            password += ch
            out.write(char_color + ch + fore["reset"])
            out.flush()
    print()
    return password


def passprompt(prompt: str, out=sys.stdout, mask_color=fore["reset"], mask='*') -> str:
    """
This Will Get Password And Replace Characters With A Mask For Example '*'.
Args :
* prompt      ->   The Text For Print And Wait For Input.

* out         ->   Just Standard Output. DO NOT TOUCH THIS :/

* mask_color  ->   The Color Of Mask. For Example You Can Print Red Stars For
                Each Character :))

* mask        ->   The Mask. Every Character That User Type, Will Be Replaced With
                This Character :)
    """
    out.write(prompt)
    out.flush()
    password = ""
    while True:
        ch = str(readchar.readchar(), encoding='UTF-8')
        if ch == '\r':
            break
        elif ch == '\b':
            out.write('\b \b')
            password = password[0:len(password)-1]
            out.flush()
        elif ch == "\x03":
            print("\n")
            raise KeyboardInterrupt("You Pressed Ctrl+C")
        else:
            password += ch
            out.write(mask_color + mask + fore["reset"])
            out.flush()
    print()
    return password


def escape_translator(target, char: str) -> list:
    """
This Function Will Help You To Recover Escaped Characters That Wrongly Splitted.
Args :
* target         ->   A List Of Splitted String/ A String That You Want To Escape.

* char           ->   The Character That You Want To Escape.

Example :
```escape_translator("Hello Lets Escape All < That Have \ Like \< . All \< Will Be Escaped.","<")```

Out :
`['Hello Lets Escape All ', ' That Have \\ Like \\< . All \\< Will Be Escaped.']`
    """

    if type(target) == str:
        target = target.split(char)
    elif type(target) == list:
        pass
    else:
        raise TypeError("Type Should Be List Or String.")
    ans = []
    escape = False
    for i in target:
        print(i, ans)
        if i[-1] == "\\":
            if escape:
                ans[-1] = ans[-1] + char + i
            else:
                ans.append(i)
            escape = True
        else:
            if escape:
                ans[-1] = ans[-1] + char + i
            else:
                ans.append(i)
            escape = False
    return ans


def colorize(string: str) -> str:
    """
It Will Colorize The Input.
Example :
```colorize("(Fore.GREEN)[Hello !]")```
Output :
* Green Foreground -> |Hello !|

Possible Colors:
```
fore = {
    "green" : Fore.GREEN,
    "black":Fore.BLACK,
    "red":Fore.RED,
    "yellow":Fore.YELLOW,
    "blue":Fore.BLUE,
    "cyan":Fore.CYAN,
    "light_black":Fore.LIGHTBLACK_EX,
    "light_blue":Fore.LIGHTBLUE_EX,
    "light_cyan":Fore.LIGHTCYAN_EX,
    "light_green":Fore.LIGHTGREEN_EX,
    "light_magenta":Fore.LIGHTMAGENTA_EX,
    "light_red":Fore.LIGHTRED_EX,
    "light_white":Fore.LIGHTWHITE_EX,
    "light_yellow":Fore.LIGHTYELLOW_EX,
    "magenta":Fore.MAGENTA,
    "reset":Fore.RESET,
    "white":Fore.WHITE
}

back = {
    "green":Back.GREEN,
    "black":Back.BLACK,
    "red":Back.RED,
    "yellow":Back.YELLOW,
    "blue":Back.BLUE,
    "cyan":Back.CYAN,
    "light_black":Back.LIGHTBLACK_EX,
    "light_blue":Back.LIGHTBLUE_EX,
    "light_cyan":Back.LIGHTCYAN_EX,
    "light_green":Back.LIGHTGREEN_EX,
    "light_magenta":Back.LIGHTMAGENTA_EX,
    "light_red":Back.LIGHTRED_EX,
    "light_white":Back.LIGHTWHITE_EX,
    "light_yellow":Back.LIGHTYELLOW_EX,
    "magenta":Back.MAGENTA,
    "reset":Back.RESET,
    "white":Back.WHITE
}
```

You Can Always Access The Colors Like That :
* pysha.fore[...]
* pysha.back[...]
    """
    data = re.findall("\(Back|\(Fore\.[A-Z]*\)\[[^\[\]]*\]", string)
    print(data)
    for i in data:
        tp = i.split('.')[0][1:].strip()
        colr = i.split('.')[1].split(')')[0].strip()
        text = '['.join(i.split('[')[1:])[:-1]
        if tp.lower() == "fore":
            c = getattr(Fore, colr)
            string = string.replace(i, c + text + Fore.RESET)
        elif tp.lower() == "back":
            c = getattr(Back, colr)
            string = string.replace(i, c + text + Back.RESET)
        else:
            raise TypeError("Type Must Be Back Or Fore.")
    return string


def make_possibles(data):
    """
    Tries To Get Possible Situations Of For Loops ( Max 3 Variable ).
    """
    if len(data.keys()) == 1:
        return list(range(list(data.values())[0]))
    elif len(data.keys()) == 2:
        temp = []
        for i in range(list(data.values())[0]):
            for j in range(list(data.values())[1]):
                temp.append([i, j])
        return temp
    elif len(data.keys()) == 3:
        temp = []
        for i in range(list(data.values())[0]):
            for j in range(list(data.values())[1]):
                for z in range(list(data.values())[2]):
                    temp.append([i, j, z])
        return temp
    else:
        pass


def display(temp: dict, string: str, c=True) -> None:
    """
Related To Loop Command. It Will Print String And Replace _i_ , _i++_ ... With The Value.

Args :
* temp    ->     Carries Variables.
* string  ->     The String Pattern That Should Be Printed In Output.
* c       ->     If Its True, Answer Will colorized. And Else Won't Be Colorized.
    """
    ans = string
    for i, j in temp.items():
        ans = (ans.replace(f"_{i}_", str(j)).replace(
            f"_{i}++_", str(j+1)).replace(f"_{i}--_", str(j-1)))
    if not c:
        print(ans)
    else:
        print(colorize(ans))


def get_ans(temp: dict, string: str, c=True) -> str:
    """
Related To Loop Command. It Will Get Input And Replace _i_ , _i++_ ... With The Value.

Args :
    * temp    ->     Carries Variables.
    * string  ->     The String Pattern That Should Be Printed In Output.
    * c       ->     If Its True, Answer Will colorized. And Else Won't Be Colorized.
    """
    ans = string
    for i, j in temp.items():
        ans = (ans.replace(f"_{i}_", str(j)).replace(
            f"_{i}++_", str(j+1)).replace(f"_{i}--_", str(j-1)))
    if not c:
        return input(ans)
    else:
        return input(colorize(ans))


def loop(cmd: str, mode='p', c=True) -> NoneOrStr:
    """
All Descriptions From This Function Came In `classes.py` - command Class.
    """
    if mode == "p":  # Print Mode
        alls = cmd.split(">")[0][1:]
        string = cmd.split("{")[1][:-1]
        arr_data = []
        dic_tar = {}
        for i in alls.split(','):
            itemp = i.split(':')
            arr_data.append(itemp[0].strip())
            dic_tar[itemp[0].strip()] = int(itemp[1].strip())
        if len(dic_tar.keys()) >= 4:
            raise LoopError(
                "Loops With 4 Or More Variables Are Not Supported In This Version.")
        tars = make_possibles(dic_tar)
        for i in tars:
            temp = {}
            if not (type(i) == int) and len(i) == 2:
                temp = {arr_data[0]: i[0], arr_data[1]: i[1]}
            elif not (type(i) == int) and len(dic_tar) == 3:
                temp = {arr_data[0]: i[0], arr_data[1]: i[1], arr_data[2]: i[2]}
            else:
                temp = {arr_data[0]: i[0]}
            display(temp, string, c)
    elif mode == 'i':  # input Mode
        alls = cmd.split(">")[0][1:]
        string = cmd.split("{")[1][:-1]
        arr_data = []
        dic_tar = {}
        for i in alls.split(','):
            itemp = i.split(':')
            arr_data.append(itemp[0].strip())
            dic_tar[itemp[0].strip()] = int(itemp[1].strip())
        if len(dic_tar.keys()) >= 4:
            raise LoopError(
                "Loops With 4 Or More Variables Are Not Supported In This Version.")
        tars = make_possibles(dic_tar)
        x = 0
        y = 0
        z = 0
        ls = []
        if len(dic_tar) == 2:
            x = (list(dic_tar.values())[0])
            y = (list(dic_tar.values())[1])
            ls = [["" for _ in range(y)] for __ in range(x)]
        elif len(dic_tar) == 1:
            x = (list(dic_tar.values())[0])
            ls = ["" for _ in range(x)]
        elif len(dic_tar) == 3:
            x = (list(dic_tar.values())[0])
            y = (list(dic_tar.values())[1])
            z = (list(dic_tar.values())[2])
            ls = [[["" for _ in range(z)] for __ in range(y)]
                  for ___ in range(x)]
        x = 0
        y = 0
        z = 0
        for i in tars:
            temp = {}
            if not (type(i) == int) and len(i) == 2:
                temp = {arr_data[0]: i[0], arr_data[1]: i[1]}
                try:
                    ls[x][y] = get_ans(temp, string, c)
                    ls[x][y + 1]
                    y += 1
                except:
                    try:
                        ls[x + 1][y]
                        x += 1
                        y = 0
                    except:
                        pass
            elif not (type(i) == int) and len(i) == 3:
                temp = {arr_data[0]: i[0], arr_data[1]: i[1], arr_data[2]: i[2]}
                try:
                    ls[x][y][z] = get_ans(temp, string, c)
                    ls[x][y][z + 1]
                    z += 1
                except:
                    try:
                        ls[x][y + 1][z]
                        y += 1
                        z = 0
                    except:
                        try:
                            ls[x + 1][y][z]
                            x += 1
                            y = 0
                            z = 0
                        except:
                            pass
            else:
                temp = {arr_data[0]: i}
                try:
                    ls[x] = get_ans(temp, string, c)
                    ls[x]
                    x += 1
                except:
                    pass
        return ls
    else:
        raise ModeError("Mode Should Be 'p' Or 'i' !")


def condition(check: str, p=True, **kwargs) -> NoneOrStrOrInt:
    """
Descrioptions Are Available In 'classes.py' And In command Class.
    """
    if not re.match("""(\"?)[ -~]+(\"?)(>|<|==|>=|<=)(\"?)[ -~]+(\"?)\?(\"?)[ -~]+(\"?):(\"?)[ -~]+(\"?)""", ''.join(check.split(' '))):
        raise ConditionError("An Error In Parsing Condition :(")
    if "eval" in check:
        if not check[check.find("eval") - 1:].startswith("\eval"):
            raise SecurityError("Using This Funcion Is Forbidden.")
    if "exec" in check:
        if not check[check.find("exec") - 1:].startswith("\exec"):
            raise SecurityError("Using This Funcion Is Forbidden.")
    index_of_ok_sign = not_between_index("?", check)
    p1 = index_split(check, index_of_ok_sign)[0].strip()
    p2 = index_split(check, index_of_ok_sign)[1].strip()
    ans = eval(p1, kwargs, {})
    index_of_ok_sign = not_between_index(":", p2)
    ok = index_split(p2, index_of_ok_sign)[0].strip()
    not_ok = index_split(p2, index_of_ok_sign)[1].strip()
    if ans:
        if p:
            print(eval(ok, kwargs))
        else:
            return eval(ok, kwargs)
    else:
        if p:
            print(eval(not_ok, kwargs))
        else:
            return eval(not_ok, kwargs)


def write_file(file_name: str, text: ListOrString) -> bool:
    """
You Can Write Into A File :)

Args :
* file_name
* text
Returns True If Its Successfully Done, Else Return False
    """
    if type(text) == str:
        try:
            a = open(file_name, "w")
            a.write(text)
            a.close()
            return True
        except:
            return False
    elif type(text) == list:
        try:
            a = open(file_name, "w")
            a.writelines(text)
            a.close()
            return True
        except:
            return False


def read_file(file_name: str, mode="s") -> ListOrString:
    """
You Can Read Data From A File :)

Args :
* file_name

* mode(Default:'s') :   The Mode Can Be 's' Or 'l' Means List Or String.
                    If You Want To Get Output As String Mode 's' Will
                    Be Good For You And If You Want To Get As list
                    Mode 'l' Is Good For You.

Returns list of lines Of The File If mode Is 'l', string of lines
If mode is 's'.
    """
    try:
        a = open(file_name, "r")
        d = a.readlines()
        a.close()
        if mode == "s":
            return "".join(d)
        elif mode == "l":
            return d
        else:
            raise ModeError(
                f"Mode {mode} Not Found ! Mode Should Be 's'(string) Or 'l'(List)")
    except:
        return ""


def append_file(file_name: str, text: str) -> bool:
    """
You Can Append to A File.

Args :
* file_name
* text
Returns True If Its Successfully Done, Else Return False
    """

    if type(text) == str:
        try:
            a = open(file_name, "a")
            a.write(text)
            a.close()
            return True
        except:
            return False
    elif type(text) == list:
        try:
            a = open(file_name, "a")
            a.writelines(text)
            a.close()
            return True
        except:
            return False


def create_dir(dir_name: str, create_parents=False) -> bool:
    """
Tries To Create A Directory.

Args :
* dir_name ->  Directory Name. You Can Pass An String Like 'test' Or 
        'test/test1/test2' For Directory. But If You Want To 
        Make Parents Too, You Have To Pass Next Argument Manually
        Too.

* create_parents(Default:False) ->  If Its False, Parents Will Not Be
                                    Created If They Are Not Exists. 
                                    And If Its True, Parents Will Be
                                    Created Too !

Returns True If Its Successfully Done, Else Return False
    """
    if create_parents:
        try:
            makedirs(dir_name)
            return True
        except:
            return False
    else:
        try:
            mkdir(dir_name)
            return True
        except:
            return False


def replace_in_file(file_name: str, data_to_replace: dict) -> bool:
    """
Tries To Replace A Dictionary.

Args :
* file_name ->  File Name. You Can Pass File Name That You Want Data 
            To Change.

* data_to_replace ->  Data That You Want To Replace As Dictinary.
                    For Example : {'test':'test1'} Will Replace All
                    'test' With 'test1' In The File.

Returns True If Its Successfully Done, Else Return False
    """
    f = open(file_name, "r")
    data = f.readlines()
    f.close()
    for i in data:
        for key, value in data_to_replace.items():
            if key in i:
                i = i.replace(key, value)
    f = open(file_name, "w")
    f.writelines(data)
    f.close()


def rm_dir(dir_name: str, force=False) -> bool:
    """
Tries To Remove A Directory.

Args :
* dir_name ->  Directory Name. You Can Pass An String Like 'test' Or 
        'test/test1/test2' For Directory. If You Want To Force
        Remove That Childs Will Remove Too, Pass Next Argument
        Manually.

* force(Default:False) ->  If Its False And If directory Has Childs,
                        Directory Won't Be Removed.But If Its False
                        Doesn't Matter What We Are Cold-Blood Murderes
                        And We Kill Them All :)

Returns True If Its Successfully Done, Else Return False
    """
    if not force:
        try:
            rmdir(dir_name)
            return True
        except:
            return False
    else:
        try:
            rmtree(dir_name)
            return True
        except:
            return False


def between(string, string_to_check, start_sign='"', end_sign='"', exact=False, case_sensetive=True):
    """
Checks If An String Exists Between Two Characters In Another String.

Args :
* string ->   A Simple String. (We Need To Check If This String Exists
            In Another String Or Not) For Example If You Want To Check
            If 'hello' is between " Characters, You Need To Pass hello
            As This Argument.

* string_to_check ->   A Big String That We Want To Check And Dive In :)
                    For Example 'hello My Name Is Arshia And "hello" Is
                    ok Now As i think :)' And Pass It As This Argument.

* start_sign -> This Should Be The Start Character That You Are Looking For.
            For Example You Can Pass " As This Argument ( Continue Of Previous
            Part Example ) . But In Another Example That You Want To Check A Tag For
            Example html Tag You Can Pass "<" As Start.

* end_sign -> This Should Be The Start Character That You Are Looking For.
            For Example You Can Pass " As This Argument ( Continue Of Previous
            Part Example ) . Continue Of Tag Example You Can Pass ">" As End.

* exact -> Basically, Checks For <html> Not <*html*>.This Argument Will Check
        For exact Value. For Example If This Option Was False And You Want
        To Check For Tags In  String "This <html Test Fake Text> Is Ok." It
        Will Return True But If This Option Is True,For That String Will
        Return False. Because It Looks For Exact "<html>" Not < Then Anything
        Then html Then Again Anything And > Character.

* case_sensetive -> If Its True, Lower Case Or Upper Case In Words Are Important.
                For Example If Its True, "Html" Is Different From "html" But
                If Its False, "Html" And "html" Are Equal.


Example :
1. between(":",'The : Is Not Between "" Chars.','"') Returns :
1. False
2. between(":",'The ":" Is Between "" Chars !','"') Returns :
2. True

Returns True If Its Found In target Text Else, Returns False.
    """
    is_in = False
    ts = ""
    for c, i in enumerate(string_to_check):
        if is_in:
            if i == end_sign:
                is_in = False
                ts = ""
        else:
            if i == start_sign:
                is_in = True
        if is_in:
            ts += i
        if not exact:
            if case_sensetive:
                if string in ts:
                    return True
            else:
                if string.lower() in ts.lower():
                    return True
        else:
            if case_sensetive:
                if start_sign + string + end_sign in ts:
                    return True
            else:
                if (start_sign + string + end_sign).lower() in ts.lower():
                    return True
    return False


def between_index(string, string_to_check, start_sign='"', end_sign='"', exact=False, case_sensetive=True, start=0):
    """
Acts Like Between Function But It Will Return Index Insted Of Boolean Value.
    """
    is_in = False
    ts = ""
    for c, i in enumerate(string_to_check[start:]):
        if is_in:
            if i == end_sign:
                is_in = False
                ts = ""
        else:
            if i == start_sign:
                is_in = True
        if is_in:
            ts += i
        if not exact:
            if case_sensetive:
                if string in ts:
                    return (c - len(string) + 1 + start)
            else:
                if string.lower() in ts.lower():
                    return (c - len(string) + 1 + start)
        else:
            if case_sensetive:
                if start_sign + string + end_sign in ts:
                    return (c - len(string) + 1 + start)
            else:
                if (start_sign + string + end_sign).lower() in ts.lower():
                    return (c - len(string) + 1 + start)
    return -1


def not_between_index(string, string_to_check, start_sign='"', end_sign='"', case_sensetive=True, start=0):
    """
Reverse Of Between Plus Index Of Target.

Args :
* string ->   A Simple String. (We Need To Check If This String Exists
            In Another String Or Not) For Example If You Want To Check
            If 'hello' is not between " Characters, You Need To Pass hello
            As This Argument.

* string_to_check ->   A Big String That We Want To Check And Dive In :)
                    For Example 'hello My Name Is Arshia And "hello" Is
                    ok Now As i think :)' And Pass It As This Argument.

* start_sign -> This Should Be The Start Character That You Are Looking For.
            For Example You Can Pass " As This Argument ( Continue Of Previous
            Part Example ) . But In Another Example That You Want To Check Text
            That Does Not In A Tag For Example html Tag You Can Pass "<" As Start.

* end_sign -> This Should Be The Start Character That You Are Looking For.
            For Example You Can Pass " As This Argument ( Continue Of Previous
            Part Example ) . Continue Of Tag Example You Can Pass ">" As End.

* case_sensetive -> If Its True, Lower Case Or Upper Case In Words Are Important.
                For Example If Its True, "Html" Is Different From "html" But
                If Its False, "Html" And "html" Are Equal.

Example :
* not_between_index(":",'Arshia Said : "Hello ! There Is : Hiding Here :)"','"','"')
*  Returns :
    `12`
*  not_between_index(":",'":" Is Not Out Of "" Sign. But Now : It Is.','"','"')
*  Returns :
    `35`

Returns True If Its Found Out Of target Sign, Else Returns False.
    """
    is_in = False
    ts = ""
    for c, i in enumerate(string_to_check[start:]):
        if is_in:
            if i == end_sign:
                is_in = False
        else:
            if i == start_sign:
                is_in = True
                ts = ""
        if not is_in:
            ts += i
        if case_sensetive:
            if string in ts:
                return (c - len(string) + 1 + start)
        else:
            if string.lower() in ts.lower():
                return (c - len(string) + 1 + start)
    return -1


def index_split(string, ind):
    """
Split String By Index.
Example :
```index_split("Hello My Name Is Arshia",10)```
Returns :
```['Hello My N', 'me Is Arshia']```
    """
    return [string[:ind], string[ind + 1:]]


def delay_loop(delay: int, func: Callable, count: int = -1, *args, **kwargs):
    """
This Function Will Try To Loop A Function In Specific count/infinite count.

Example :
* delay_loop(10,func,5,args,kwargs)

In Every 10 Seconds Function func(args,kwargs) Will Be Called 5 Times.
    """
    if count == -1:
        index = 0
        while True:
            time.sleep(delay)
            index += 1
            func(index, *args, **kwargs)
    else:
        for index in range(count):
            time.sleep(delay)
            func(index, *args, **kwargs)


def merge(*args, force_list=False, dont_change=False):
    """
This Function Will Merge Some List Or Some Dict Or Some Dict And List !
Example :
```merge(["a","b"],{"c":"d","e":"f"},["g","h"])```
Returns :
```{"a":"","b":"","c":"","d":"","e":"","f":"","g":"","h":""}```

Example :
```merge(["a","b"],{"c":"d","e":"f"},["g","h"],force_list=True)```
Returns :
```["a","b","c","e","d","f","g","h"]```

Example :
```merge(["a","b"],{"c":"d","e":"f"},["g","h"],force_list=True,dont_change=True)```
Returns :
```["a","b","c","d","e","f","g","h"]```

Example:
```merge(["a","b"],["c","d","e","f"],["g","h"])```
Returns :
```["a","b","c","d","e","f","g","h"]```

In Every 10 Seconds Function func(args,kwargs) Will Be Called 5 Times.
    """
    if list(filter(lambda x: type(x) == dict, args)):
        if not force_list:
            ans = {}
            for i in args:
                if type(i) == list:
                    ans[i] = ""
                elif type(i) == dict:
                    ans.update(i)
            return ans
        else:
            ans = []
            for i in args:
                if type(i) == list:
                    ans.extend(i)
                elif type(i) == dict:
                    if dont_change:
                        for a, b in i.items():
                            ans.extend([a, b])
                    else:
                        ans.extend(i.keys())
                        ans.extend(i.values())
            return ans
    else:
        ans = []
        for i in args:
            ans.extend(i)
        return ans


def make_array(dimentions):
    """
Make An Array In Dimentions That You Gave.
    """
    ans = [None for _ in range(dimentions[-1])]
    for i in dimentions[:-1][::-1]:
        ans = [ans for _ in range(i)]
    return ans


def set_array(array, dimentions, value):
    """
Set An Array Value In Complicated Dimentions.
    """
    for i in dimentions:
        array = array[i]
    array = value
    return array
