import pyfiglet
import datetime
from classes import *
from data_structures import *
from auth import *

def pp(*args,curly_c=Fore.RESET,colon_c=Fore.RESET,quote_c=Fore.RESET,mode='k',end='\n'):
    for i in args:
        if type(i) == list:
            print("[",' , '.join([str(j) for j in i]),"]",end=end)
        elif type(i) == dict:
            print(curly_c + "{" + Fore.RESET)
            for a,b in i.items():
                print("\t" + quote_c + "'" + Fore.RESET + a.replace("'","\\" + quote_c + "'" + Fore.RESET) + quote_c + "'" + Fore.RESET + colon_c + " : " + Fore.RESET + quote_c + "'" + Fore.RESET + b.replace("'","\\" + quote_c + "'" + Fore.RESET) + quote_c + "'" + Fore.RESET + " ,")
            print(curly_c + "}" + Fore.RESET,end=end)
        elif type(i) == set:
            print(curly_c + "{" + Fore.RESET)
            for a in i:
                print("\t",a,",")
            print(curly_c + "}" + Fore.RESET,end=end)
        elif type(i) == str:
            if mode == 'k': # Kwargs Mode
                i = i.replace("{",curly_c + "{" + Fore.RESET)
                i = i.replace("}",curly_c + "}" + Fore.RESET)
                i = i.replace("'",quote_c + "'" + Fore.RESET)
                i = colorize(i)
                i = i.replace(":",colon_c + ":" + Fore.RESET)
                print(i,end=end)
            elif mode == 'i': # Input Mode
                i = colorize(i)
                print(i,end=end)
        else:
            print(i,end=end)


def timer(string):
    def sec(func):
        def run(*args,**kwargs):
            start = datetime.datetime.now()
            func(*args,**kwargs)
            end = datetime.datetime.now()
            ans = string
            s = ans.replace("_T_",str(end - start))
            s = s.replace("_S_",str(end - start).split(':')[2].split('.')[0].strip())
            try:
                s = s.replace("_MS_",str(end - start).split(':')[2].split('.')[1].strip())
            except:
                s = s.replace("_MS_","0")
            s = s.replace("_M_",str(end - start).split(':')[1].strip())
            s = s.replace("_H_",str(end - start).split(':')[0].strip())
            pp(s)
        return run
    return sec
    
def rect(*args,text_color=Fore.RESET,first_line=("=",Fore.RESET),sep=("|",Fore.RESET),last_line=("=",Fore.RESET),distance_up=1,distance_down=1,length=30,p=True):
    ans = []
    for i in args:
        ans.extend(i.split('\n'))
    args = ans.copy()
    del ans
    if len(first_line) == 1:
        first_line = first_line,Fore.RESET
    if len(sep) == 1:
        sep = sep,Fore.RESET
    if len(last_line) == 1:
        last_line = last_line,Fore.RESET
    max_length = 0
    for i in args:
        if len(i) > max_length:
            max_length = len(i)
    max_length += 10
    if length > max_length:
        max_length = length
    if p:
        print(first_line[1] + first_line[0] * max_length + Fore.RESET)
        for i in range(distance_up):
            print(sep[1] + sep[0] + Fore.RESET,end='')
            print(' ' * (max_length-2),end='')
            print(sep[1] + sep[0] + Fore.RESET)
        for i in args:
            print(sep[1] + sep[0] + Fore.RESET,end='')
            print(text_color + i.center(max_length-2) + Fore.RESET,end='')
            print(sep[1] + sep[0] + Fore.RESET)
        for i in range(distance_down):
            print(sep[1] + sep[0] + Fore.RESET,end='')
            print(' ' * (max_length-2),end='')
            print(sep[1] + sep[0] + Fore.RESET)
        print(last_line[1] + last_line[0] * max_length + Fore.RESET)
    else:
        s = first_line[1] + first_line[0] * max_length + Fore.RESET
        for i in range(distance_up):
            s += sep[1] + sep[0] + Fore.RESET + ' ' * (max_length-2)
            s += sep[1] + sep[0] + Fore.RESET + "\n"
        for i in args:
            s += (sep[1] + sep[0] + Fore.RESET)
            s += (text_color + i.center(max_length-2) + Fore.RESET)
            s += (sep[1] + sep[0] + Fore.RESET + "\n")
        for i in range(distance_down):
            s += (sep[1] + sep[0] + Fore.RESET) + (' ' * (max_length-2))
            s += (sep[1] + sep[0] + Fore.RESET + "\n")
        s += (last_line[1] + last_line[0] * max_length + Fore.RESET)
        return s


"""
This Function Directly Use pyfiglet Library For Making A Banner.
Args:
    text -> The Text That You Want To Convert To A Banner.
    font -> Target Font From Figlet. If You Pass Empty Font Will Be Default
            Figlet Font.
    p    -> If This Argument Is True, It Will Print Output And If 
            Its False, It Will Return Output.

Example : 
    * Code
        banner("pysha","chunky")
    
    * Output
        ______               __
        |   __ \.--.--.-----.|  |--.---.-.
        |    __/|  |  |__ --||     |  _  |
        |___|   |___  |_____||__|__|___._|
                |_____|
"""
def banner(text,font="",p=True):
    if font:
        try:
            if p:
                print(pyfiglet.figlet_format(text,font=font))
            else:
                return pyfiglet.figlet_format(text,font=font)
        except pyfiglet.FontNotFound:
            print("Font " + font + " Not Found :(")
        except:
            raise
        return
    if p:
        print(pyfiglet.figlet_format(text))
    else:
        return pyfiglet.figlet_format(text)

"""
This Function Will Draw A Line In Terminal.
Kwargs:
    char -> You Can Pass (char='-') Then Color Will Be Normal Color. Or
            You Can Pass (char=('-',Fore.[color])) Then Color Will Be [color].
            Default Is ('=',Fore.RESET)
    count -> Count Of Characters That Line Have.
"""
def l(char=('=',Fore.RESET),count=30,p=True):
    if type(char) == str or ((type(char) == list or type(char) == set or type(char) == tuple) and len(char) == 1):
        char = char,Fore.RESET
    if p:
        print(char[1] + char[0] * count + Fore.RESET)
    else:
        return char[1] + char[0] * count + Fore.RESET


"""
This Function Will pp The Arguments.
You Can Set A Prompt If You Want. ( Prompt Will Not Be pp )
After pp And Prompt It Will Get Input And Returns Input.
You Can Change Prompt Color By Pass (prompt,Fore.[color]) To Prompt.
Kwargs:
    prompt -> You Can Pass (prompt='Enter Your Name : ') And It Will Act As
              input('Enter Your Name : '). Or You Can Pass (prompt=('Name : ',Fore.RED))
              And It Will Print 'Name : ' In Red Color.
Example : 
    * Code
        name = xp("(Fore.RED)[W3LC0M3] To (Fore.GREEN)[T3ST] Application.",prompt=('Name : ',Fore.CYAN))
        pp(name)
    * Output
        _RED ->|W3LC0M3|_ To _GREEN -> |T3ST|_ Application.
        _CYAN -> |Name :|_ (input)
        (input)
"""
def xp(*args,prompt=('',Fore.RESET)):
    if (len(prompt) == 1 and (type(prompt) == tuple or type(prompt) == list or type(prompt) == set)) or type(prompt) == str:
        prompt = prompt,Fore.RESET
    pp(*args,mode='i',end='')
    return input(prompt[1] + prompt[0] + Fore.RESET)


"""
print('*'.center(20)) ; print('*       *'.center(20)) ; print('*           *'.center(20)) ; print('*           *'.center(20))
  ; print('*       *'.center(20)) ; print('*'.center(20))

c = 1
f = 0
for i in range(6):
    if i == 0:
        print(" " * 6 + c)
        c += 1
        f += 7
    elif i == 2:
        print(c + " " * f + c)
    elif i == 3:
        f += 3
        f /= 2
        print(c + " " * f + c)
    else:
        print(c + " " * f + c)
        f *= 2
        f -= 3
"""