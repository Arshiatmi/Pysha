from functions import *
from enum import *
from os import environ, popen, remove

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
            if len(self.dic_tar.keys()) >= 3:
                raise LoopError("Loops With 3 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            for i in tars:
                temp = {}
                if not (type(i) == int) and len(i) == 2:
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1]}
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
            if len(self.dic_tar.keys()) >= 3:
                raise LoopError("Loops With 3 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            x = 0
            y = 0
            ls = []
            if len(self.dic_tar) == 2:
                x = (list(self.dic_tar.values())[0])
                y = (list(self.dic_tar.values())[1])
                ls = [["" for _ in range(y)] for __ in range(x)]
            elif len(self.dic_tar) == 1:
                x = (list(self.dic_tar.values())[0])
                ls = ["" for _ in range(x)]
            x = 0
            y = 0
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
        condition("i > j ? 'i Is Grater' : 'j Is Grater'",i=20,j=23)
    Output Will Be :
        "j Is Grater"
    """
    def condition(self,check,p=True,**kwargs):
        if not re.match("""(\'?|\"?)[ -~]+(\'?|\"?)(>|<|==|>=|<=)(\'?|\"?)[ -~]+(\'?|\"?)\?(\'?|\"?)[ -~]+(\'?|\"?):(\'?|\"?)[ -~]+(\'?|\"?)""",''.join(check.split(' '))):
            raise ConditionError("An Error In Parsing Condition :(")
        if "eval" in check:
            if not check[check.find("eval") - 1:].startswith("\eval"):
                raise SecurityError("Using This Funcion Is Forbidden.")
        if "exec" in check:
            if not check[check.find("exec") - 1:].startswith("\exec"):
                raise SecurityError("Using This Funcion Is Forbidden.")
        p1 = check.split("?")[0].strip()
        p2 = check.split("?")[1].strip()
        ans = eval(p1,kwargs,{})
        ok = p2.split(':')[0].strip()
        not_ok = p2.split(':')[1].strip()
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

    """
    def exe(self,string,priority=0):
        s = re.compile("\$\([ -~]+\)")
        p = re.compile("\#\([ -~]+\)")
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
                ans = popen(environ.get("python") + " temp.py").read().strip()
                remove("temp.py")
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            return string
        elif priority == 1:
            # First Python Then System
            for cmd in p.finditer(string):
                cmds = cmd.group()[2:-1]
                f = open("temp.py","w")
                f.write(cmds)
                f.close()
                ans = popen(environ.get("python") + " temp.py").read().strip()
                remove("temp.py")
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            for cmd in s.finditer(string):
                cmds = cmd.group()[2:-1]
                ans = popen(cmds).read()
                string = string[:cmd.start()] + ans + string[cmd.start() + len(cmd.group()):]
            return string
        else:
            ValueError("Priority Should Be 0 (System First) Or 1 (Python First).")

class Switch:
    def __init__(self,var):
        self.var = var
    
    def case(self,tar,func,args=tuple()):
        if self.var == tar:
            func(*args)
    
    def cases(self,all_funcs):
        for i,j in all_funcs.items():
            if self.var == i:
                if str(type(j)) == "<class 'function'>":
                    j()
                    return
                elif type(j) == str:
                    b = compile(j,'user_code','single')
                    a = eval(b)
                    if a != None:
                        print(a)
                if len(j) == 3:
                    j[0](*j[1],**j[2])
                elif len(j) == 2:
                    j[0](*j[1])
                elif len(j) == 1:
                    j[0]()