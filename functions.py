from typing import Union
from colors import *
from exceptions import *
import re
import readchar,sys

def colorprompt(prompt: str,out = sys.stdout,char_color=fore["reset"]):
    out.write(prompt); out.flush()
    password = ""
    while True:
        ch = str(readchar.readchar(), encoding='UTF-8')
        if ch == '\r':
            break
        elif ch == '\b':
            out.write('\b \b')
            password = password[0:len(password)-1]
            out.flush()
        else: 
            password += ch
            out.write(char_color + ch + fore["reset"])
            out.flush()
    return password

def passprompt(prompt: str, out = sys.stdout,mask_color=fore["reset"],mask='*') -> str:
    out.write(prompt); out.flush()
    password = ""
    while True:
        ch = str(readchar.readchar(), encoding='UTF-8')
        if ch == '\r':
            break
        elif ch == '\b':
            out.write('\b \b')
            password = password[0:len(password)-1]
            out.flush()
        else: 
            password += ch
            out.write(mask_color + mask + fore["reset"])
            out.flush()
    return password

def colorize(string: str) -> str:
    data = re.findall("\(Back|\(Fore\.[A-Z]*\)\[[a-zA-Z0-9_ :\/\\\'\"\+\=\-\$\%\^\&\*\@\!\#\(\)\?]*\]",string)
    for i in data:
        tp = i.split('.')[0][1:].strip()
        colr = i.split('.')[1].split(')')[0].strip()
        text = '['.join(i.split('[')[1:])[:-1]
        if tp.lower() == "fore":
            c = getattr(Fore,colr)
            string = string.replace(i,c + text + Fore.RESET)
        elif tp.lower() == "back":
            c = getattr(Back,colr)
            string = string.replace(i,c + text + Back.RESET)
        else:
            raise TypeError("Type Must Be Back Or Fore.")
    return string

def make_possibles(data):
    if len(data.keys()) == 1:
        return list(range(list(data.values())[0]))
    else:
        l1 = list([[i] for i in range(list(data.items())[0][1])])
        ans = []
        for i in l1:
            temp = []
            for key,value in list(data.items())[1:]:
                for j in range(value):
                    temp.append(i + [j])
            ans.extend(temp)
        return ans


def display(temp: dict,string: str,c=True) -> None:
    ans = string
    for i,j in temp.items():
        ans = (ans.replace(f"_{i}_",str(j)).replace(f"_{i}++_",str(j+1)).replace(f"_{i}--_",str(j-1)))
    if not c:
        print(ans)
    else:
        print(colorize(ans))

def get_ans(temp: dict,string: str,c=True) -> str:
    ans = string
    for i,j in temp.items():
        ans = (ans.replace(f"_{i}_",str(j)).replace(f"_{i}++_",str(j+1)).replace(f"_{i}--_",str(j-1)))
    if not c:
        return input(ans)
    else:
        return input(colorize(ans))


"""
All Descriptions From This Function Came In `classes.py` - command Class.
"""
def loop(cmd: str,mode='p',c=True) -> Union[None,str]:
    if mode == "p": # Print Mode
        alls = cmd.split(">")[0][1:]
        string = cmd.split("{")[1][:-1]
        arr_data = []
        dic_tar = {}
        for i in alls.split(','):
            itemp = i.split(':')
            arr_data.append(itemp[0].strip())
            dic_tar[itemp[0].strip()] = int(itemp[1].strip())
        if len(dic_tar.keys()) >= 3:
            raise LoopError("Loops With 3 Or More Variables Are Not Supported In This Version.")
        tars = make_possibles(dic_tar)
        for i in tars:
            temp = {}
            if not (type(i) == int) and len(i) == 2:
                temp = {arr_data[0]:i[0],arr_data[1]:i[1]}
            else:
                temp = {arr_data[0]:i[0]}
            display(temp,string,c)
    elif mode == 'i': #input Mode
        alls = cmd.split(">")[0][1:]
        string = cmd.split("{")[1][:-1]
        arr_data = []
        dic_tar = {}
        for i in alls.split(','):
            itemp = i.split(':')
            arr_data.append(itemp[0].strip())
            dic_tar[itemp[0].strip()] = int(itemp[1].strip())
        if len(dic_tar.keys()) >= 3:
            raise LoopError("Loops With 3 Or More Variables Are Not Supported In This Version.")
        tars = make_possibles(dic_tar)
        x = 0
        y = 0
        ls = []
        if len(dic_tar) == 2:
            x = (list(dic_tar.values())[0])
            y = (list(dic_tar.values())[1])
            ls = [["" for _ in range(y)] for __ in range(x)]
        elif len(dic_tar) == 1:
            x = (list(dic_tar.values())[0])
            ls = ["" for _ in range(x)]
        x = 0
        y = 0
        for i in tars:
            temp = {}
            if not (type(i) == int) and len(i) == 2:
                temp = {arr_data[0]:i[0],arr_data[1]:i[1]}
            else:
                temp = {arr_data[0]:i}
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
        raise ModeError("Mode Should Be 'p' Or 'i' !")


"""
Descrioptions Are Available In 'classes.py' And In command Class.
"""
def condition(check : str,p=True,**kwargs) -> Union[None,str,int]:
    if not re.match("""(\'?|\"?)[ -~]+(\'?|\"?)(>|<|==|>=|<=)(\'?|\"?)[ -~]+(\'?|\"?)\?(\'?|\"?)[ -~]+(\'?|\"?):(\'?|\"?)[ -~]+(\'?|\"?)""",''.join(check.split(' '))):
        raise ConditionError("An Error In Parsing Condition :(")
    p1 = check.split("?")[0].strip()
    p2 = check.split("?")[1].strip()
    ans = eval(p1,kwargs)
    ok = p2.split(':')[0].strip()
    not_ok = p2.split(':')[1].strip()
    if ans:
        if p:
            print(eval(ok,kwargs))
        else:
            return eval(ok,kwargs)
    else:
        if p:
            print(eval(not_ok,kwargs))
        else:
            return eval(not_ok,kwargs)