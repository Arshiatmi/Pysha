import enum
from enums import Algorithms
from typing import Union
from os import popen,mkdir,makedirs,rmdir
from shutil import rmtree
from colors import *
from exceptions import *
import re
import readchar,sys


"""
This Will Act Like Input. But Characters That User Enters Will Be Colored :)
Args :
    prompt      ->   The Text For Print And Wait For Input.
    
    out         ->   Just Standard Output. DO NOT TOUCH THIS :/

    char_color  ->   The Color Of Character. Each Character Will Have This 
                     Color.

"""
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
    print()
    return password


"""
This Will Get Password And Replace Characters With A Mask For Example '*'.
Args :
    prompt      ->   The Text For Print And Wait For Input.

    out         ->   Just Standard Output. DO NOT TOUCH THIS :/

    mask_color  ->   The Color Of Mask. For Example You Can Print Red Stars For
                     Each Character :))

    mask        ->   The Mask. Every Character That User Type, Will Be Replaced With
                     This Character :)
"""
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
    print()
    return password

"""
It Will Colorize The Input.
Example :
    colorize("(Fore.GREEN)[Hello !]")
Output :
    Green Foreground -> |Hello !|

Possible Colors:
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

    You Can Always Access The Colors Like That :
        pysha.fore[...]
        pysha.back[...]
"""
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

"""
Tries To Get Possible Situations Of For Loops ( Max 2 Variable ).
"""
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

"""
Related To Loop Command. It Will Print String And Replace _i_ , _i++_ ... With The Value.
    Args :
        temp    ->     Carries Variables.
        string  ->     The String Pattern That Should Be Printed In Output.
        c       ->     If Its True, Answer Will colorized. And Else Won't Be Colorized.
"""
def display(temp: dict,string: str,c=True) -> None:
    ans = string
    for i,j in temp.items():
        ans = (ans.replace(f"_{i}_",str(j)).replace(f"_{i}++_",str(j+1)).replace(f"_{i}--_",str(j-1)))
    if not c:
        print(ans)
    else:
        print(colorize(ans))

"""
Related To Loop Command. It Will Get Input And Replace _i_ , _i++_ ... With The Value.
    Args :
        temp    ->     Carries Variables.
        string  ->     The String Pattern That Should Be Printed In Output.
        c       ->     If Its True, Answer Will colorized. And Else Won't Be Colorized.
"""
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

def _(cmd):
    return popen(cmd).read()

def write_file(file_name: str,text : Union[str,list]) -> bool:
    if type(text) == str:
        try:
            a = open(file_name,"w")
            a.write(text)
            a.close()
            return True
        except:
            return False
    elif type(text) == list:
        try:
            a = open(file_name,"w")
            a.writelines(text)
            a.close()
            return True
        except:
            return False

def read_file(file_name: str,mode="s") -> Union[list,str]:
    try:
        a = open(file_name,"r")
        d = a.readlines()
        a.close()
        if mode == "s":
            return "".join(d)
        elif mode == "l":
            return d
        else:
            raise ModeError(f"Mode {mode} Not Found ! Mode Should Be 's'(string) Or 'l'(List)")
    except:
        return ""


def append_file(file_name: str,text: str) -> bool:
    if type(text) == str:
        try:
            a = open(file_name,"a")
            a.write(text)
            a.close()
            return True
        except:
            return False
    elif type(text) == list:
        try:
            a = open(file_name,"a")
            a.writelines(text)
            a.close()
            return True
        except:
            return False

def create_dir(dir_name: str,create_parents=False) -> bool:
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


def rm_dir(dir_name: str,force=False) -> bool:
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

def make_enc(alg,key=""):
    if type(alg) == enum.EnumMeta:
        print(alg,type(alg))
        if alg == Algorithms.XOR:
            pass
        elif alg == Algorithms.Base64:
            pass
        elif alg == Algorithms.Cypher:
            pass
        else:
            raise AlgorithmError(f"This Algorithm Is Not Available. We Will Be Happy If You Help Us To Make It :)\nGithub : https://github.com/Arshiatmi/Pysha")
    elif type(alg) == list or type(alg) == set:
        for i in alg:
            if type(i) == enum.EnumMeta:
                pass
            else:
                raise AlgorithmError(f"Type {i} Is Not Supported. Just (Algorithms.Base64/Algorithms.XOR/Algorithms.Cypher) Is Supported.")
        pass
    else:
        raise AlgorithmError(f"This Type Of Algorithm Is Not Supported. Just enum.EnumMeta (Algorithms.Base64/...),list and set Are Supported.")