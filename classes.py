from functions import *
from os import environ, popen, remove

"""
    This Class Will Be Use For Fun Part Of This Framework :)
    Most Important Part Of This Framework Exists In This Class.
"""
class command:
    def __init__(self):
        self.arr_data = []
        self.dic_tar = {}
        self._mode = 'p'
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self,m):
        if m not in ['p','i']:
            raise ModeError("Modes Should Be 'p' Or 'i'. Default Is 'p' / Print Mode.")
        else:
            self._mode = m

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
    def loop(self,cmd,mode='p',c=True):
        if self.mode != 'p':
            mode = self.mode
        if mode == "p": # Print Mode
            self.dic_tar.clear()
            self.arr_data.clear()
            alls = cmd.split(">")[0][1:]
            string = cmd.split("{")[1][:-1]
            for i in alls.split(','):
                itemp = i.split(':')
                self.arr_data.append(itemp[0].strip())
                self.dic_tar[itemp[0].strip()] = int(itemp[1].strip())
            if len(self.dic_tar.keys()) >= 4:
                raise LoopError("Loops With 4 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            for i in tars:
                temp = {}
                if not (type(i) == int) and len(i) == 2:
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1]}
                elif not (type(i) == int) and len(self.dic_tar) == 3:
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1],self.arr_data[2]:i[2]}
                else:
                    temp = {self.arr_data[0]:i}
                display(temp,string,c)
        elif mode == 'i': #input Mode
            self.dic_tar.clear()
            self.arr_data.clear()
            alls = cmd.split(">")[0][1:]
            string = cmd.split("{")[1][:-1]
            for i in alls.split(','):
                itemp = i.split(':')
                self.arr_data.append(itemp[0].strip())
                self.dic_tar[itemp[0].strip()] = int(itemp[1].strip())
            if len(self.dic_tar.keys()) >= 4:
                raise LoopError("Loops With 4 Or More Variables Are Not Supported In This Version.")
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
                ls = [[["" for _ in range(z)] for __ in range(y)] for ___ in range(x)]
            x = 0
            y = 0
            z = 0
            for i in tars:
                temp = {}
                if not (type(i) == int) and len(i) == 2:
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1]}
                    try:
                        ls[x][y] = get_ans(temp,string,c)
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
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1],self.arr_data[2]:i[2]}
                    try:
                        ls[x][y][z] = get_ans(temp,string,c)
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
                    temp = {self.arr_data[0]:i}
                    try:
                        ls[x] = get_ans(temp,string,c)
                        ls[x]
                        x += 1
                    except:
                        pass
                
            return ls
        else:
            raise ValueError("Mode Should Be 'p' Or 'i' !")
    

    """
    This Function Act As c++ One Line Condition.
    You Can Use This Function Like :
        condition('i > j ? "i Is Grater" : "j Is Grater"',i=20,j=23)
    Output Will Be :
        "j Is Grater"
    
    Notes & Warnings :
        -> '(Quotes) Are Not Working, Always Use "(Double Quotes)
    """
    def condition(self,check,p=True,**kwargs):
        if not re.match("""(\"?)[ -~]+(\"?)(>|<|==|>=|<=)(\"?)[ -~]+(\"?)\?(\"?)[ -~]+(\"?):(\"?)[ -~]+(\"?)""",''.join(check.split(' '))):
            raise ConditionError("An Error In Parsing Condition :(")
        if "eval" in check:
            if not check[check.find("eval") - 1:].startswith("\eval"):
                raise SecurityError("Using This Funcion Is Forbidden.")
        if "exec" in check:
            if not check[check.find("exec") - 1:].startswith("\exec"):
                raise SecurityError("Using This Funcion Is Forbidden.")
        index_of_ok_sign = not_between_index("?",check)
        p1 = index_split(check,index_of_ok_sign)[0].strip()
        p2 = index_split(check,index_of_ok_sign)[1].strip()
        ans = eval(p1,kwargs,{})
        index_of_ok_sign = not_between_index(":",p2)
        ok = index_split(p2,index_of_ok_sign)[0].strip()
        not_ok = index_split(p2,index_of_ok_sign)[1].strip()
        if ans:
            if p:
                print(eval(ok,kwargs,{}))
            else:
                return eval(ok,kwargs,{})
        else:
            if p:
                print(eval(not_ok,kwargs,{}))
            else:
                return eval(not_ok,kwargs,{})
    
    """
        In Progress But This Function Should Get Text Between () Of $(cmd)
        And Run It In Terminal Then Replace The Output With $(cmd) And Should
        Get #(cmd) Too And Run It As Python Code And Replace This Output Too.
            Problem Now :
                Use This 2 Thing Together.
        
        Args : 
            string          ->    The String Pattern That You Want To Make.

            priority        ->    If Its 0 First System Commands Will Replace Then
                                Python Commands Will Replace. And If Its 1 First
                                Python Commands Will Replace Then System Commands
                                Will Be Replaced. Default Is 0.
            
            strip_response  ->     Default Is True. It Wanted To Know That Your
                                    String That Replaced Should Be striped ? ( Remove
                                    Addtion New Lines And Spaces In Start And End Of 
                                    String ? )
        
        Example :
            exe("You Current Directory :\n $(dir)\nFinished :)")
    """
    def exe(self,string,priority=0,strip_response=True):
        s = re.compile("\$\([A-Za-z0-9_ \$\&\!\@\#\%\^\*\+\=\-\]\[\~\?\'\"\;\:]+\)")
        p = re.compile("\#\([A-Za-z0-9_ \$\&\!\@\#\%\^\*\+\=\-\]\[\~\?\'\"\;\:]+\)")
        if priority == 0:
            # First System Then Python
            for cmd in s.finditer(string):
                cmds = cmd.group()[2:-1]
                ans = popen(cmds).read()
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            for cmd in p.finditer(string):
                cmds = cmd.group()[2:-1]
                f = open("temp.py","w")
                f.write(cmds)
                f.close()
                ans = popen(environ.get("python") + " temp.py").read()
                remove("temp.py")
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            if strip_response:
                return string.strip()
            else:
                return string
        elif priority == 1:
            # First Python Then System
            for cmd in p.finditer(string):
                cmds = cmd.group()[2:-1]
                f = open("temp.py","w")
                f.write(cmds)
                f.close()
                ans = popen(environ.get("python") + " temp.py").read()
                remove("temp.py")
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            for cmd in s.finditer(string):
                cmds = cmd.group()[2:-1]
                ans = popen(cmds).read()
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            if strip_response:
                return string.strip()
            else:
                return string
        else:
            ValueError("Priority Should Be 0 (System First) Or 1 (Python First).")

"""
    The Famous Switch-Case :)
"""
class Switch:
    def __init__(self,var):
        self.var = var
    
    def case(self,tar,func,args=tuple()):
        if self.var == tar or (hasattr(tar,'__name__') and tar.__name__ == "Case" and tar == self.var) or (tar == self.var) or (hasattr(tar,'__name__') and tar.__name__ == "Default"):
            func(*args)
    
    def cases(self,all_funcs):
        for i,j in all_funcs.items():
            if self.var == i or (hasattr(i,'__name__') and i.__name__ == "Case" and i.tar == self.var) or (hasattr(i,'tar') and i.tar == self.var) or (hasattr(i,'__name__') and i.__name__ == "Default"):
                if hasattr(j,'__call__'):
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
                    b = compile(ok_code,'user_code','exec')
                    a = exec(b)
                    if a != None:
                        print(a)
                if len(j) == 3:
                    j[0](*j[1],**j[2])
                elif len(j) == 2:
                    j[0](*j[1])
                elif len(j) == 1:
                    j[0]()

"""
    Default Case Of Switch-Case
"""
class Default:
    pass

"""
    Define Every Case
"""
class Case:
    def __init__(self,tar):
        self.tar = tar

"""
    Define Variables Of Switch-Case ( Just lambda Case )
"""
class Vars:
    pass

"""
    Pretty Percent Printer For Loading Some Progress Or Downloading :)
"""
class PercentPrinter:
    def __init__(self,chars=100,pass_color=fore["reset"],loading_color=fore["reset"]):
        self._percent = 0
        self.chars = chars
        self.pass_color=pass_color
        self.loading_color=loading_color
    
    def show(self,char_ok='#',char_loading='-',end='\n'):
        num = self._percent
        string = "\r"
        string += (self.pass_color + char_ok + Fore.RESET) * int(num * (self.chars / 100))
        string += (self.loading_color + char_loading + Fore.RESET) * int((100 - num) * (self.chars / 100))
        print(string,end=end)
    
    @property
    def percent(self):
        return self._percent
    
    @percent.setter
    def percent(self,p):
        if p > 100:
            raise ValueError("Value Most Be Less Than 100 !")
        elif p < 0:
            raise ValueError("Value Most Be More Than 0 !")
        else:
            self._percent = p
    
    def increase(self,p=1):
        self._percent += p
        
    def finish(self):
        self._percent = 100