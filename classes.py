from functions import *
from enum import *

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
            alls = cmd.split(">")[0][1:]
            string = cmd.split("{")[1][:-1]
            for i in alls.split(','):
                itemp = i.split(':')
                self.arr_data.append(itemp[0].strip())
                self.dic_tar[itemp[0].strip()] = int(itemp[1].strip())
                setattr(self,itemp[0].strip(),int(itemp[1].strip()))
            if len(self.dic_tar.keys()) >= 3:
                raise LoopError("Loops With 3 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            for i in tars:
                temp = {}
                if len(i) == 2:
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1]}
                else:
                    temp = {self.arr_data[0]:i[0]}
                display(temp,string,c)
        elif mode == 'i': #input Mode
            alls = cmd.split(">")[0][1:]
            string = cmd.split("{")[1][:-1]
            for i in alls.split(','):
                itemp = i.split(':')
                self.arr_data.append(itemp[0].strip())
                self.dic_tar[itemp[0].strip()] = int(itemp[1].strip())
                setattr(self,itemp[0].strip(),int(itemp[1].strip()))
            if len(self.dic_tar.keys()) >= 3:
                raise LoopError("Loops With 3 Or More Variables Are Not Supported In This Version.")
            tars = make_possibles(self.dic_tar)
            x = (list(self.dic_tar.values())[0])
            y = (list(self.dic_tar.values())[1])
            ls = [["" for _ in range(y)] for __ in range(x)]
            x = 0
            y = 0
            for i in tars:
                temp = {}
                if len(i) == 2:
                    temp = {self.arr_data[0]:i[0],self.arr_data[1]:i[1]}
                else:
                    temp = {self.arr_data[0]:i[0]}
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
            return ls
        else:
            raise ValueError("Mode Should Be 'p' Or 'i' !")
    

    """
    This Function Act As c++ One Line Condition.
    You Can Use This Function Like :
        condition("i > j ? 'i Is Grater' : 'j Is Grater'",i=20,j=23)
    Output Will Be :
        "j Is Grater"
    
    This Function Now Supports:
        int,float,string Compares For Now.
    """
    def condition(self,check,p=True,**kwargs):
        if not re.match("""(\'?|\"?)[ -~]+(\'?|\"?)(>|<|==|>=|<=)(\'?|\"?)[ -~]+(\'?|\"?)\?(\'?|\"?)[ -~]+(\'?|\"?):(\'?|\"?)[ -~]+(\'?|\"?)""",''.join(check.split(' '))):
            raise ConditionError("An Error In Parsing Condition :(")
        p1 = check.split("?")[0].strip()
        p2 = check.split("?")[1].strip()
        op = ""
        a = ""
        b = ""
        if ">=" in p1:
            op = ">="
            a = p1.split('>=')[0].strip()
            b = p1.split('>=')[1].strip()
        elif "<=" in p1:
            op = "<="
            a = p1.split('<=')[0].strip()
            b = p1.split('<=')[1].strip()
        elif "==" in p1:
            op = "=="
            a = p1.split("==")[0].strip()
            b = p1.split("==")[1].strip()
        elif ">" in p1:
            op = ">"
            a = p1.split('>')[0].strip()
            b = p1.split('>')[1].strip()
        elif "<" in p1:
            op = "<"
            a = p1.split('<')[0].strip()
            b = p1.split('<')[1].strip()
        else:
            raise ConditionError(f"Unsupported Operator `{op}`. You Can Use `>` , `<` , `==` , `>=` and `<=`.")
        t = calculate(a,op,b,**kwargs)
        ok = p2.split(':')[0].strip()
        not_ok = p2.split(':')[1].strip()
        try:
            if not ((ok.startswith('"') and ok.endswith('"')) or (ok.startswith("'") and ok.endswith("'"))):
                ok = int(ok)
            else:
                ok = ok[1:-1]
        except:
            try:
                ok = kwargs[ok]
            except:
                raise ConditionError(f"An Error In Handling {ok} Variable")
        try:
            if not ((not_ok.startswith('"') and not_ok.endswith('"')) or (not_ok.startswith("'") and not_ok.endswith("'"))):
                not_ok = int(not_ok)
            else:
                not_ok = not_ok[1:-1]
        except:
            try:
                not_ok = kwargs[not_ok]
            except:
                raise ConditionError(f"An Error In Handling {not_ok} Variable")
        if t:
            if p:
                print(ok)
            else:
                return ok
        else:
            if p:
                print(not_ok)
            else:
                return not_ok
            