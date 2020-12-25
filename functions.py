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
All Descriptions From This Function Came In `classes.py`
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
            if len(i) == 2:
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
        x = (list(dic_tar.values())[0])
        y = (list(dic_tar.values())[1])
        ls = [["" for _ in range(y)] for __ in range(x)]
        x = 0
        y = 0
        for i in tars:
            temp = {}
            if len(i) == 2:
                temp = {arr_data[0]:i[0],arr_data[1]:i[1]}
            else:
                temp = {arr_data[0]:i[0]}
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


def calculate(a: str,op: str,b: str,**kwargs) -> bool:
    elem1 = a
    elem2 = b
    try:
        if not ((elem1.startswith('"') and elem1.endswith('"')) or (elem1.startswith("'") and elem1.endswith("'"))):
            elem1 = int(elem1)
        else:
            elem1 = elem1[1:-1]
    except:
        try:
            elem1 = kwargs[elem1]
        except:
            raise ConditionError(f"An Error In Handling {elem1} Variable")
    try:
        if not ((elem2.startswith('"') and elem2.endswith('"')) or (elem2.startswith("'") and elem2.endswith("'"))):
            elem2 = int(elem2)
        else:
            elem2 = elem2[1:-1]
    except:
        try:
            elem2 = kwargs[elem2]
        except:
            raise ConditionError(f"An Error In Handling {elem2} Variable")
    if op == ">":
        return elem1 > elem2
    elif op == "<":
        return elem1 < elem2
    elif op == "<=":
        return elem1 <= elem2
    elif op == ">=":
        return elem1 >= elem2
    elif op == "==":
        return elem1 == elem2
    else:
        raise ConditionError(f"Unsupported Operator `{op}`. You Can Use `>` , `<` , `==` , `>=` and `<=`.")


def condition(check : str,p=True,**kwargs) -> Union[None,str,int]:
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
            ok = float(ok)
        else:
            ok = ok[1:-1]
    except:
        try:
            ok = kwargs[ok]
        except:
            raise ConditionError(f"An Error In Handling {ok} Variable")
    try:
        if not ((not_ok.startswith('"') and not_ok.endswith('"')) or (not_ok.startswith("'") and not_ok.endswith("'"))):
            not_ok = float(not_ok)
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