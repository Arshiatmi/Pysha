from typing import Union
from os import mkdir,makedirs,rmdir
from shutil import rmtree
from colors import *
from exceptions import *
import re
import readchar,sys
from security import *


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
        elif ch == "\x03":
            print("\n")
            raise KeyboardInterrupt("You Pressed Ctrl+C")
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
        elif ch == "\x03":
            print("\n")
            raise KeyboardInterrupt("You Pressed Ctrl+C")
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
Tries To Get Possible Situations Of For Loops ( Max 3 Variable ).
"""
def make_possibles(data):
    if len(data.keys()) == 1:
        return list(range(list(data.values())[0]))
    elif len(data.keys()) == 2:
        temp = []
        for i in range(list(data.values())[0]):
            for j in range(list(data.values())[1]):
                temp.append([i,j])
        return temp
    elif len(data.keys()) == 3:
        temp = []
        for i in range(list(data.values())[0]):
            for j in range(list(data.values())[1]):
                for z in range(list(data.values())[2]):
                    temp.append([i,j,z])
        return temp
    else:
        pass

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
        if len(dic_tar.keys()) >= 4:
            raise LoopError("Loops With 4 Or More Variables Are Not Supported In This Version.")
        tars = make_possibles(dic_tar)
        for i in tars:
            temp = {}
            if not (type(i) == int) and len(i) == 2:
                temp = {arr_data[0]:i[0],arr_data[1]:i[1]}
            elif not (type(i) == int) and len(dic_tar) == 3:
                temp = {arr_data[0]:i[0],arr_data[1]:i[1],arr_data[2]:i[2]}
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
        if len(dic_tar.keys()) >= 4:
            raise LoopError("Loops With 4 Or More Variables Are Not Supported In This Version.")
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
            ls = [[["" for _ in range(z)] for __ in range(y)] for ___ in range(x)]
        x = 0
        y = 0
        z = 0
        for i in tars:
            temp = {}
            if not (type(i) == int) and len(i) == 2:
                temp = {arr_data[0]:i[0],arr_data[1]:i[1]}
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
                temp = {arr_data[0]:i[0],arr_data[1]:i[1],arr_data[2]:i[2]}
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
                temp = {arr_data[0]:i}
                try:
                    ls[x] = get_ans(temp,string,c)
                    ls[x]
                    x += 1
                except:
                    pass
        return ls
    else:
        raise ModeError("Mode Should Be 'p' Or 'i' !")


"""
Descrioptions Are Available In 'classes.py' And In command Class.
"""
def condition(check : str,p=True,**kwargs) -> Union[None,str,int]:
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
            print(eval(ok,kwargs))
        else:
            return eval(ok,kwargs)
    else:
        if p:
            print(eval(not_ok,kwargs))
        else:
            return eval(not_ok,kwargs)

"""
    You Can Write Into A File :)
    Args :
        file_name
        text
    Returns True If Its Successfully Done, Else Return False
"""
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


"""
    You Can Read Data From A File :)
    Args :
        file_name

        mode(Default:'s') :   The Mode Can Be 's' Or 'l' Means List Or String.
                            If You Want To Get Output As String Mode 's' Will
                            Be Good For You And If You Want To Get As list
                            Mode 'l' Is Good For You.

    Returns list of lines Of The File If mode Is 'l', string of lines
    If mode is 's'.
"""
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

"""
    You Can Append to A File.
    Args :
        file_name
        text
    Returns True If Its Successfully Done, Else Return False
"""
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


"""
    Tries To Create A Directory.
    Args :
        dir_name ->  Directory Name. You Can Pass An String Like 'test' Or 
                   'test/test1/test2' For Directory. But If You Want To 
                   Make Parents Too, You Have To Pass Next Argument Manually
                   Too.

        create_parents(Default:False) ->  If Its False, Parents Will Not Be
                                            Created If They Are Not Exists. 
                                            And If Its True, Parents Will Be
                                            Created Too !

    Returns True If Its Successfully Done, Else Return False
"""
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


"""
    Tries To Remove A Directory.
    Args :
        dir_name ->  Directory Name. You Can Pass An String Like 'test' Or 
                   'test/test1/test2' For Directory. If You Want To Force
                   Remove That Childs Will Remove Too, Pass Next Argument
                   Manually.

        force(Default:False) ->  If Its False And If directory Has Childs,
                                Directory Won't Be Removed.But If Its False
                                Doesn't Matter What We Are Cold-Blood Murderes
                                And We Kill Them All :)

    Returns True If Its Successfully Done, Else Return False
"""
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


"""
    Checks If An String Exists Between Two Characters In Another String.
    Args :
        string ->   A Simple String. (We Need To Check If This String Exists
                    In Another String Or Not) For Example If You Want To Check
                    If 'hello' is between " Characters, You Need To Pass hello
                    As This Argument.

        string_to_check ->   A Big String That We Want To Check And Dive In :)
                            For Example 'hello My Name Is Arshia And "hello" Is
                            ok Now As i think :)' And Pass It As This Argument.
        
        start_sign -> This Should Be The Start Character That You Are Looking For.
                    For Example You Can Pass " As This Argument ( Continue Of Previous
                    Part Example ) . But In Another Example That You Want To Check A Tag For
                    Example html Tag You Can Pass "<" As Start.
        
        end_sign -> This Should Be The Start Character That You Are Looking For.
                    For Example You Can Pass " As This Argument ( Continue Of Previous
                    Part Example ) . Continue Of Tag Example You Can Pass ">" As End.
        
        exact -> Basically, Checks For <html> Not <*html*>.This Argument Will Check
                For exact Value. For Example If This Option Was False And You Want
                To Check For Tags In  String "This <html Test Fake Text> Is Ok." It
                Will Return True But If This Option Is True,For That String Will
                Return False. Because It Looks For Exact "<html>" Not < Then Anything
                Then html Then Again Anything And > Character.
        
        case_sensetive -> If Its True, Lower Case Or Upper Case In Words Are Important.
                         For Example If Its True, "Html" Is Different From "html" But
                         If Its False, "Html" And "html" Are Equal.
        

    Example :
        1. between(":",'The : Is Not Between "" Chars.','"')
        1. Returns :
            1. False
        2. between(":",'The ":" Is Between "" Chars !','"')
        2. Returns :
            2. True

    Returns True If Its Found In target Text Else, Returns False.
"""
def between(string,string_to_check,start_sign='"',end_sign='"',exact=False,case_sensetive=True):
    is_in = False
    ts = ""
    for c,i in enumerate(string_to_check):
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



"""
    Acts Like Between Function But It Will Return Index Insted Of Boolean Value.
"""
def between_index(string,string_to_check,start_sign='"',end_sign='"',exact=False,case_sensetive=True,start=0):
    is_in = False
    ts = ""
    for c,i in enumerate(string_to_check[start:]):
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


"""
    Reverse Of Between Plus Index Of Target.
    Args :
        string ->   A Simple String. (We Need To Check If This String Exists
                    In Another String Or Not) For Example If You Want To Check
                    If 'hello' is not between " Characters, You Need To Pass hello
                    As This Argument.

        string_to_check ->   A Big String That We Want To Check And Dive In :)
                            For Example 'hello My Name Is Arshia And "hello" Is
                            ok Now As i think :)' And Pass It As This Argument.
                
        start_sign -> This Should Be The Start Character That You Are Looking For.
                    For Example You Can Pass " As This Argument ( Continue Of Previous
                    Part Example ) . But In Another Example That You Want To Check Text
                    That Does Not In A Tag For Example html Tag You Can Pass "<" As Start.
        
        end_sign -> This Should Be The Start Character That You Are Looking For.
                    For Example You Can Pass " As This Argument ( Continue Of Previous
                    Part Example ) . Continue Of Tag Example You Can Pass ">" As End.
        
        case_sensetive -> If Its True, Lower Case Or Upper Case In Words Are Important.
                         For Example If Its True, "Html" Is Different From "html" But
                         If Its False, "Html" And "html" Are Equal.
    
    Example :
        1. not_between_index(":",'Arshia Said : "Hello ! There Is : Hiding Here :)"','"','"')
        1. Returns :
            1. 12
        2. not_between_index(":",'":" Is Not Out Of "" Sign. But Now : It Is.','"','"')
        2. Returns :
            2. 35

    Returns True If Its Found Out Of target Sign, Else Returns False.
"""
def not_between_index(string,string_to_check,start_sign='"',end_sign='"',case_sensetive=True,start=0):
    is_in = False
    ts = ""
    for c,i in enumerate(string_to_check[start:]):
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


"""
    Split String By Index.
    Example :
        index_split("Hello My Name Is Arshia",10)
    Returns :
        ['Hello My N', 'me Is Arshia']
"""
def index_split(string,ind):
    return [string[:ind],string[ind + 1:]]