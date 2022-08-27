from enum import Enum
from inspect import signature
import platform
from secrets import choice
from data_structures import PyshaString
from functions import *
from os import environ, popen, remove


class command:
    """
        This Class Will Be Use For Fun Part Of This Framework :)
    """

    def __init__(self):
        self.arr_data = []
        self.dic_tar = {}
        self._mode = 'p'

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, m):
        if m not in ['p', 'i']:
            raise ModeError(
                "Modes Should Be 'p' Or 'i'. Default Is 'p' / Print Mode.")
        else:
            self._mode = m

    def loop(self, cmd, mode='p', c=True):
        """
        2 Types Of Loop Currently Exists. i(Input) and p(Print) Mode.
        In print mode you can make a print loop like that :
            <i:3>{You Are In _i_ Loop}
        And This Will Be Printed Like That : 
            You Are In 0 Loop
            You Are In 1 Loop
            You Are In 2 Loop

        And In Input Mode You Can Do This :
            <i:3>{Enter _i_ Number : }
        It Will Get 3 Input Like This :
            Enter 0 Number : (input0)
            Enter 1 Number : (input1)
            Enter 2 Number : (input2)
        And Will Return [input0,input1,input2]

        More Options :
            <i:3>{Enter _i++_ Number : }
            <i:3>{Enter _i--_ Number : }
            <i:2,j:2>{Enter Row _i++_ And Column _j++_  Number : }
            <i:2>{Enter (Fore.CYAN)[_i++_] Number : }

        Notes :
            Just Maded Maximum For 2 Variables Not More.
        """
        if self.mode != 'p':
            mode = self.mode
        if mode == "p":  # Print Mode
            self.dic_tar.clear()
            self.arr_data.clear()
            alls = cmd.split(">")[0][1:]
            string = cmd.split("{")[1][:-1]
            for i in alls.split(','):
                itemp = i.split(':')
                self.arr_data.append(itemp[0].strip())
                self.dic_tar[itemp[0].strip()] = int(itemp[1].strip())
            if len(self.dic_tar.keys()) >= 4:
                raise LoopError(
                    "Loops With 4 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            for i in tars:
                temp = {}
                if not (type(i) == int) and len(i) == 2:
                    temp = {self.arr_data[0]: i[0], self.arr_data[1]: i[1]}
                elif not (type(i) == int) and len(self.dic_tar) == 3:
                    temp = {
                        self.arr_data[0]: i[0], self.arr_data[1]: i[1], self.arr_data[2]: i[2]}
                else:
                    temp = {self.arr_data[0]: i}
                display(temp, string, c)
        elif mode == 'i':  # input Mode
            self.dic_tar.clear()
            self.arr_data.clear()
            alls = cmd.split(">")[0][1:]
            string = cmd.split("{")[1][:-1]
            for i in alls.split(','):
                itemp = i.split(':')
                self.arr_data.append(itemp[0].strip())
                self.dic_tar[itemp[0].strip()] = int(itemp[1].strip())
            if len(self.dic_tar.keys()) >= 4:
                raise LoopError(
                    "Loops With 4 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            x = 0
            y = 0
            z = 0
            ls = []
            if len(self.dic_tar) == 2:
                x = (list(self.dic_tar.values())[0])
                y = (list(self.dic_tar.values())[1])
                ls = [["" for _ in range(y)] for __ in range(x)]
            elif len(self.dic_tar) == 1:
                x = (list(self.dic_tar.values())[0])
                ls = ["" for _ in range(x)]
            elif len(self.dic_tar) == 3:
                x = (list(self.dic_tar.values())[0])
                y = (list(self.dic_tar.values())[1])
                z = (list(self.dic_tar.values())[2])
                ls = [[["" for _ in range(z)] for __ in range(y)]
                      for ___ in range(x)]
            x = 0
            y = 0
            z = 0
            for i in tars:
                temp = {}
                if not (type(i) == int) and len(i) == 2:
                    temp = {self.arr_data[0]: i[0], self.arr_data[1]: i[1]}
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
                    temp = {
                        self.arr_data[0]: i[0], self.arr_data[1]: i[1], self.arr_data[2]: i[2]}
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
                    temp = {self.arr_data[0]: i}
                    try:
                        ls[x] = get_ans(temp, string, c)
                        ls[x]
                        x += 1
                    except:
                        pass

            return ls
        else:
            raise ValueError("Mode Should Be 'p' Or 'i' !")

    def condition(self, check, p=True, **kwargs):
        """
        This Function Act As c++ One Line Condition.
        You Can Use This Function Like :

            `condition('i > j ? "i Is Grater" : "j Is Grater"',i=20,j=23)`

        Output Will Be :

            `"j Is Grater"`

        Notes & Warnings :

            `-> '(Quotes) Are Not Working, Always Use "(Double Quotes)`
        """
        if not re.match("""(\"?)[ -~]+(\"?)(>|<|==|>=|<=)(\"?)[ -~]+(\"?)\?(\"?)[ -~]+(\"?):\W{,1}(\"?)[!-~]+(\"?)""", ''.join(check.split(' '))):
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
                print(eval(ok, kwargs, {}))
            else:
                return eval(ok, kwargs, {})
        else:
            if p:
                print(eval(not_ok, kwargs, {}))
            else:
                return eval(not_ok, kwargs, {})

    def exe(self, string, priority=0, strip_response=True):
        """
            In Progress But This Function Should Get Text Between () Of $(cmd)
            And Run It In Terminal Then Replace The Output With $(cmd) And Should
            Get #(cmd) Too And Run It As Python Code And Replace This Output Too.
                Problem Now :
                    Use This 2 Thing Together.

            Args : 

                * string          ->    The String Pattern That You Want To Make.

                * priority        ->    If Its 0 First System Commands Will Replace Then
                                    Python Commands Will Replace. And If Its 1 First
                                    Python Commands Will Replace Then System Commands
                                    Will Be Replaced. Default Is 0.

                * strip_response  ->     Default Is True. It Wanted To Know That Your
                                        String That Replaced Should Be striped ? ( Remove
                                        Addtion New Lines And Spaces In Start And End Of 
                                        String ? )

            Example :

                * exe("You Current Directory :\n $(dir)\nFinished :)")
        """
        s = re.compile(
            "\$\([A-Za-z0-9_ \$\&\!\@\#\%\^\*\+\=\-\]\[\~\?\'\"\;\:]+\)")
        p = re.compile(
            "\#\([A-Za-z0-9_ \$\&\!\@\#\%\^\*\+\=\-\]\[\~\?\'\"\;\:]+\)")
        if priority == 0:
            # First System Then Python
            for cmd in s.finditer(string):
                cmds = cmd.group()[2:-1]
                ans = popen(cmds).read()
                string = string[:cmd.start()] + ans + \
                    string[cmd.start() + len(cmd.group()):]
            for cmd in p.finditer(string):
                cmds = cmd.group()[2:-1]
                f = open("temp.py", "w")
                f.write(cmds)
                f.close()
                ans = popen(environ.get("python") + " temp.py").read()
                remove("temp.py")
                string = string[:cmd.start()] + ans + \
                    string[cmd.start() + len(cmd.group()):]
            if strip_response:
                return string.strip()
            else:
                return string
        elif priority == 1:
            # First Python Then System
            for cmd in p.finditer(string):
                cmds = cmd.group()[2:-1]
                f = open("temp.py", "w")
                f.write(cmds)
                f.close()
                ans = popen(environ.get("python") + " temp.py").read()
                remove("temp.py")
                string = string[:cmd.start()] + ans + \
                    string[cmd.start() + len(cmd.group()):]
            for cmd in s.finditer(string):
                cmds = cmd.group()[2:-1]
                ans = popen(cmds).read()
                string = string[:cmd.start()] + ans + \
                    string[cmd.start() + len(cmd.group()):]
            if strip_response:
                return string.strip()
            else:
                return string
        else:
            ValueError(
                "Priority Should Be 0 (System First) Or 1 (Python First).")


class Switch:
    """
        The Famous Switch-Case :)
    """

    def __init__(self, var):
        self.var = var

    def case(self, tar, func, args=tuple()):
        if self.var == tar or (hasattr(tar, '__name__') and tar.__name__ == "Case" and tar == self.var) or (tar == self.var) or (hasattr(tar, '__name__') and tar.__name__ == "Default"):
            func(*args)

    def __getitem__(self, all_funcs):
        dic = {}
        for i in all_funcs:
            dic[i.start] = i.stop
        for i, j in dic.items():
            if self.var == i or (hasattr(i, '__name__') and i.__name__ == "Case" and i.tar == self.var) or (hasattr(i, 'tar') and i.tar == self.var) or (hasattr(i, '__name__') and i.__name__ == "Default"):
                if hasattr(j, '__call__'):
                    j()
                    return
                elif type(j) == str:
                    parts = j.split('\n')
                    if parts[0].strip():
                        t = parts[0].index(j.split('\n')[0].strip())
                    else:
                        t = parts[1].index(j.split('\n')[1].strip())
                    ok_code = ""
                    for i in j.split('\n'):
                        ok_code += i[t:] + "\n"
                    b = compile(ok_code, 'user_code', 'exec')
                    a = exec(b)
                    if a != None:
                        print(a)
                    return
                if len(j) == 3:
                    j[0](*j[1], **j[2])
                    return
                elif len(j) == 2:
                    j[0](*j[1])
                    return
                elif len(j) == 1:
                    j[0]()
                    return

    def cases(self, all_funcs):
        """
            This Function Should Get A Dictionary That Key Is Case And Value Is Function That Will Run On That
            Case. You Can Pass Lots Of Types For Example :
            ```
                Case(5):
                    [
                        func,
                        arguments,
                        kwargs
                    ]
            ```
            Or :
            ```
                Case(1):
                    " \
                        print("yay")
                    "
            ```
            Or :
            ```
                Case(6):
                    lambda x,y:
                        print(x,y)
            ```
            For More Models You Can See Examples.
        """
        for i, j in all_funcs.items():
            if self.var == i or (hasattr(i, '__name__') and i.__name__ == "Case" and i.tar == self.var) or (hasattr(i, 'tar') and i.tar == self.var) or (hasattr(i, '__name__') and i.__name__ == "Default"):
                if hasattr(j, '__call__'):
                    j()
                    return
                elif type(j) == str:
                    parts = j.split('\n')
                    if parts[0].strip():
                        t = parts[0].index(j.split('\n')[0].strip())
                    else:
                        t = parts[1].index(j.split('\n')[1].strip())
                    ok_code = ""
                    for i in j.split('\n'):
                        ok_code += i[t:] + "\n"
                    b = compile(ok_code, 'user_code', 'exec')
                    a = exec(b)
                    if a != None:
                        print(a)
                    return
                if len(j) == 3:
                    j[0](*j[1], **j[2])
                    return
                elif len(j) == 2:
                    j[0](*j[1])
                    return
                elif len(j) == 1:
                    j[0]()
                    return


class Default:
    """
        Default Case Of Switch-Case. Its Not Doing Anything But You Can Use It On Your Switch Cases.
    """
    pass


class Case:
    """
        Define Case Of Switch-Case. Just In Case You Want To Use It Like Case(x).
    """

    def __init__(self, tar):
        self.tar = tar


class Vars:
    """
        In Case You Want To Define Some Variables In lambdas, You Can Set Attributes Of This Class.
    """
    pass


class PercentPrinter:
    """
        Pretty Percent Printer For Loading Some Progress Or Downloading :)
        In Fact, Its Progressbar Itself :)
    """

    def __init__(self, chars=100, pass_color=fore["reset"], loading_color=fore["reset"]):
        """
            Arguments :
                * chars=50, # Characters Of Progressbar
                * pass_color=fore["reset"], # The Color Of Passed Part
                * loading_color=fore["reset"], # The Color Of Loading Part ( Still Not Fulled Part )
        """
        self._percent = 0
        self.chars = chars
        self.pass_color = pass_color
        self.loading_color = loading_color
        self.char_ok = '#'
        self.char_loading = '-'

    def config(self, char_ok, char_loading):
        """
            Set char_ok And char_loading For Progressbar.
        """
        self.char_ok = char_ok
        self.char_loading = char_loading

    def show(self, char_ok='#', char_loading='-', end='\n'):
        """
            This Function Just Shows The Progressbar.
        """
        if char_ok == '#':
            if self.char_ok != '#':
                char_ok = self.char_ok
        if char_loading == '-':
            if self.char_loading != '-':
                char_loading = self.char_loading

        num = self._percent
        string = "\r"
        string += (self.pass_color + char_ok + Fore.RESET) * \
            int(num * (self.chars / 100))
        string += (self.loading_color + char_loading + Fore.RESET) * \
            int((100 - num) * (self.chars / 100))
        print(string, end=end)

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, p):
        if p > 100:
            raise ValueError("Value Most Be Less Than 100 !")
        elif p < 0:
            raise ValueError("Value Most Be More Than 0 !")
        else:
            self._percent = p

    def increase(self, p=1, show=True):
        """
            Increses Progressbar In Percents That You Set.
        """
        self._percent += p
        if show:
            self.show()

    def finish(self, show=True):
        """
            Finishes The Progressbar.
        """
        self._percent = 100
        if show:
            self.show()


class CrossPlatformer:
    """
        This Class Will Make An Environment For You To Have Easier And Better Experience :)
    """

    def __init__(self, supported_os=["linux", "windows", "mac"]) -> None:
        """
            Arguments : 
                * supported_os # You Can Set Supported Oses. Default is ["linux", "windows", "mac"]
        """
        self.user_os = platform.system().strip().lower()
        self.all_commands = {}
        self.supported_os = supported_os
        self.platforms = {
            "windows": ["windows", "win32"],
            "linux": ["linux", "linux2"],
            "mac": ["mac", "darwin"]
        }

    def get_os_name(self):
        """Get User Os Name"""
        if self.user_os == "linux" or self.user_os == "linux2":
            return "Linux"
        elif self.user_os == "darwin":
            return "Mac"
        elif self.user_os == "win32" or self.user_os == "windows":
            return "Windows"
        else:
            return "Unknown"

    def is_os_supported(self, os_name):
        """Check If An Os Is Supported"""
        for i, j in self.platforms.items():
            if os_name.lower().strip() in j or os_name.lower().strip() == i:
                return True
        return False

    def get_os_version(self):
        """Get User Os Version"""
        if self.user_os == "linux" or self.user_os == "linux2":
            return platform.linux_distribution()[0]
        elif self.user_os == "darwin":
            return platform.mac_ver()[0]
        elif self.user_os == "win32" or self.user_os == "windows":
            return platform.win32_ver()[0]
        else:
            return "Unknown"

    def get_os_command(self, name):
        """
        Get Command For User Os. Arguments :
            * name : Command Name
        For Example :

            If You Set add_os_commands("clear", {"linux": "clear", "windows": "cls", "mac": "clear"}) :
                * get_os_command("clear")

            Will Return You The Command Depends On Your Os.
        """
        try:
            return self.all_commands[name][self.user_os]
        except:
            return None

    def add_os_commands(self, name, commands: dict):
        """
        Set Command For User Os. Arguments Are : 
            * name : Name Of Command
            * commands : Dictionary Of Commands
        For Example : 
            * add_os_commands("git", {"linux": "git", "windows": "git.exe"})
        Or : 
            * add_os_commands("clear", {"linux": "clear", "windows": "cls", "mac": "clear"})
        """
        for i in commands:
            if not self.is_os_supported(i):
                raise ValueError(f"This OS ({i}) Is Not Supported !")
        self.all_commands[name] = commands

    def __getitem__(self, name):
        return self.get_os_command(name)

    def __setitem__(self, name, commands):
        self.add_os_commands(name, commands)


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


class Cond:
    """
        Thats Just Normal One line Conditions That Exists in C++. ( Inspired From C++ )
        You Can Use It Like : 
            * Cond( condition )( if_its_true, if_its_false )
        For Example :
            * Cond(i > j)(i,j)
        Or Cool Things Like :
            * Cond(i > j)(minus,add)(i,j)
        Thats Your Creativity That Makes Your Application Cool :)
    """

    def __init__(self, condition) -> None:
        self.condition = condition

    def __call__(self, t1, t2):
        if self.condition:
            return t1
        else:
            return t2


class Loop:
    """
        This Option Is Unique Too Pysha. Its Not From Anywhere Else But Anyway I Think Its Not That Cool :/
        You Can Use It Like : 
            ```Loop(x,y)("Enter Number[_1_][_2_] :",Loop.Modes.Input) # Input Mode Is Default```

        ### Modes : 
            * Input = 0
            * Print = 1

        Input Is Where You Want To Get Input Just Not Print The Text In x * y Times. It Will Return x * y Array Contains Inputs.
        Print Is Where You Want To Just Print The Text In x * y Times.
    """

    def __init__(self, *args):
        try:
            self.x = list(map(lambda x: int(x) - 1, args))
        except:
            raise ValueError("Values Must Be Int.")
        self.var_names = self.__get_var_name()
        self.index = 0
        self.ans_array = [None for _ in range(self.x[-1])]
        for i in self.x[:-1][::-1]:
            self.ans_array = [self.ans_array for _ in range(i)]

    def __get_var_name(self):
        self.index += 1
        return str(self.index)

    class Modes(Enum):
        Input = 0
        Print = 1

    def __format_text(self, text, from_replace=[], to_replace=[]):
        text = PyshaString(text)
        for c, i in enumerate(from_replace):
            text = text.replace(i, str(to_replace[c]))
        return text

    def __call__(self, text, mode=Modes.Input):
        cur = len(self.x) - 1
        self.y = [0 for _ in range(cur+1)]
        while True:
            text = self.__format_text(text, self.var_names, self.y)
            if mode == self.Modes.Input:
                set_array(self.ans_array, self.y, input(text))
            else:
                print(text)
            if self.y[cur] < self.x[cur]:
                self.y[cur] += 1
            elif list(self.x) == list(self.y):
                break
            else:
                self.y[cur] = 0
                ind = cur - 1
                while self.y[ind] == self.x[cur]:
                    self.y[ind] = 0
                    ind -= 1
                    if ind == 0:
                        break
                self.y[ind] += 1
        if mode == self.Modes.Input:
            return self.ans_array
