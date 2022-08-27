import pyfiglet
from classes import *
from data_structures import *
from auth import *
from enums import *
from decorators import *


def pp(*args, curly_c=Fore.RESET, colon_c=Fore.RESET, quote_c=Fore.RESET, mode='k', end='\n'):
    """
    Abbreviation of Pretty Print.
    Args:
        You Can Give As Much As You Can For Print :)

    Kwargs:
        curly_c : Set Curly Brackets Colors or "{}" Color.
        colon_c : Set Colon Colors or ":" Color.
        quote_c : Set Quote Colors or "'" Color.
        mode    : Set Mode Of pp. Modes Are 'k' And 'i'. You Can Read About
                    Them In Modes Part.
        end     : This Will Set End Of Print. Default Is '\n'.

    Modes : 
        k : This Will Use all colors That You Specified As Kwargs.
        i : This Will Ignore Colors(curly_c,colon_c,quote_c) That You
                Specified In Kwargs. 
    """
    for i in args:
        if type(i) == list:
            print("[", ' , '.join([str(j) for j in i]), "]", end=end)
        elif type(i) == dict:
            print(curly_c + "{" + Fore.RESET)
            for a, b in i.items():
                print("\t" + quote_c + "'" + Fore.RESET + a.replace("'", "\\" + quote_c + "'" + Fore.RESET) + quote_c + "'" + Fore.RESET + colon_c +
                      " : " + Fore.RESET + quote_c + "'" + Fore.RESET + b.replace("'", "\\" + quote_c + "'" + Fore.RESET) + quote_c + "'" + Fore.RESET + " ,")
            print(curly_c + "}" + Fore.RESET, end=end)
        elif type(i) == set:
            print(curly_c + "{" + Fore.RESET)
            for a in i:
                print("\t", a, ",")
            print(curly_c + "}" + Fore.RESET, end=end)
        elif type(i) == str:
            if mode == 'k':  # Kwargs Mode
                i = i.replace("{", curly_c + "{" + Fore.RESET)
                i = i.replace("}", curly_c + "}" + Fore.RESET)
                i = i.replace("'", quote_c + "'" + Fore.RESET)
                i = colorize(i)
                i = i.replace(":", colon_c + ":" + Fore.RESET)
                print(i, end=end)
            elif mode == 'i':  # Input Mode
                i = colorize(i)
                print(i, end=end)
        else:
            print(i, end=end)


def rect(*args, text_color=Fore.RESET, first_line=("=", Fore.RESET), sep=("|", Fore.RESET), last_line=("=", Fore.RESET), distance_up=1, distance_down=1, length=30, p=True):
    """
    This Function Will Draw A Rectangle Plus Your Target Text Middle Of It.
    Args:
        Just Your Texts. You Can Pass It Like rect("hello","Thanks") Or rect("hello\nThanks")
    kwargs:
        text_color    ->   Color Of Your Text.

        first_line    ->   This Parameter Will Set First Line Character And Color.
                            You Can Pass A Character, Default Text Color Will Be Setted.
                            Or You Can Pass A Tuple That Contains Character And Color Like
                            ('-',Fore.RED).

        sep           ->   This Parameter Will Set Corners Character And Color.
                            You Can Pass A Character, Default Text Color Will Be Setted.
                            Or You Can Pass A Tuple That Contains Character And Color Like
                            ('-',Fore.RED).

        last_line     ->   This Parameter Will Set Last Line Character And Color.
                            You Can Pass A Character, Default Text Color Will Be Setted.
                            Or You Can Pass A Tuple That Contains Character And Color Like
                            ('-',Fore.RED).

        distance_up   ->   This Parameter Will Set Distance Between Text And First Line.
                            You Can Pass An Integer That Is Line Numbers Of Distance.

        distance_down ->   This Parameter Will Set Distance Between Text And Last Line.
                            You Can Pass An Integer That Is Line Numbers Of Distance.

        length        ->   This Parameter Will Set Number Of Characters In First/Last
                            Line. You Can Pass An Integer That Is Character Count Of First/Last Line.

        p            ->   This Parameter Will Set Print Mode. If Its True It Will Print
                            And If Its False It Will Return Rectangle As String.


    Example : 
        * Code
            rect("Hello\nWelcome To Pysha :)",first_line='-',last_line='-',distance_up=2,distance_down=2)

        * Output
            ------------------------------
            |                            |
            |                            |
            |           Hello            |
            |    Welcome To Pysha :)     |
            |                            |
            |                            |
            ------------------------------
    """
    ans = []
    for i in args:
        ans.extend(i.split('\n'))
    args = ans.copy()
    del ans
    if len(first_line) == 1:
        first_line = first_line, Fore.RESET
    if len(sep) == 1:
        sep = sep, Fore.RESET
    if len(last_line) == 1:
        last_line = last_line, Fore.RESET
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
            print(sep[1] + sep[0] + Fore.RESET, end='')
            print(' ' * (max_length-2), end='')
            print(sep[1] + sep[0] + Fore.RESET)
        for i in args:
            print(sep[1] + sep[0] + Fore.RESET, end='')
            print(text_color + i.center(max_length-2) + Fore.RESET, end='')
            print(sep[1] + sep[0] + Fore.RESET)
        for i in range(distance_down):
            print(sep[1] + sep[0] + Fore.RESET, end='')
            print(' ' * (max_length-2), end='')
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


def banner(text, font="", p=True):
    """
    This Function Directly Use pyfiglet Library For Making A Banner.
    Args:
        text -> The Text That You Want To Convert To A Banner.

        font -> Target Font From Figlet. If You Pass Empty Font Will Be Default
                Figlet Font.

        p    -> This Parameter Will Set Print Mode. If Its True It Will Print
                And If Its False It Will Return Banner As String.

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
    if font:
        try:
            if p:
                print(pyfiglet.figlet_format(text, font=font))
            else:
                return pyfiglet.figlet_format(text, font=font)
        except pyfiglet.FontNotFound:
            print("Font " + font + " Not Found :(")
        except:
            raise
        return
    if p:
        print(pyfiglet.figlet_format(text))
    else:
        return pyfiglet.figlet_format(text)


def l(char=('=', Fore.RESET), count=30, p=True):
    """
    This Function Will Draw A Line In Terminal.
    Kwargs:
        char -> You Can Pass (char='-') Then Color Will Be Normal Color. Or
                You Can Pass (char=('-',Fore.[color])) Then Color Will Be [color].
                Default Is ('=',Fore.RESET)

        count -> Count Of Characters That Line Have.

        p     -> This Parameter Will Set Print Mode. If Its True It Will Print
                And If Its False It Will Return Line As String.
    """
    if type(char) == str or ((type(char) == list or type(char) == set or type(char) == tuple) and len(char) == 1):
        char = char, Fore.RESET
    if p:
        print(char[1] + char[0] * count + Fore.RESET)
    else:
        return char[1] + char[0] * count + Fore.RESET


def xp(*args, prompt=('', Fore.RESET)):
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

    if (len(prompt) == 1 and (type(prompt) == tuple or type(prompt) == list or type(prompt) == set)) or type(prompt) == str:
        prompt = prompt, Fore.RESET
    pp(*args, mode='i', end='')
    return input(prompt[1] + prompt[0] + Fore.RESET)
