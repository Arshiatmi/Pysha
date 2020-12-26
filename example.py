from pysha import *
import time,random

@timer("Time Was (Fore.RED)[_H_] : (Fore.RED)[_M_] : (Fore.RED)[_S_] And In (Fore.CYAN)[_MS_] Miliseconds")
def test():
    print(fore["green"] + "Started" + fore["reset"])
    print(fore["green"] + "[+] " + fore["reset"] + "Loading...")
    time.sleep(random.randint(1,10) / 10)
    print(fore["red"] + "END" + fore["reset"])

test()

pp("Salam",[1,2,3],["S","v"],[True,False],{"Salam":"Man Arshiam"})

rect("Test",distance_down=2,distance_up=2)

rect("Salam\nMan Arshiam :)",first_line=("-",Fore.YELLOW),last_line=("-",Fore.YELLOW),sep=("!",Fore.YELLOW),text_color=Fore.RED)

banner("Salam")

banner("Salam",font="3-d")

pp("(: (Fore.GREEN)[WElcome] To (Fore.RED)[T3sT] AppliCaTion :)",colon_c=Fore.RED)

l(('-',Fore.CYAN),count=50)

name = xp("(Fore.RED)[Enter Your Name :] ")

pp(f"Hello (Fore.RED)[{name}]")

a = command()
ans = a.loop("<i:2,j:3>{Enter Your (Fore.RED)[Name] Person _i_ And _j_ : }")
a.condition("name == 'Arshia' ? 'Welcome' : 'Nice To Meet You'",name="Arshia")
a.condition("i > j ? 'YAY' : 'NO'",i=10,j=20)
# a.condition("i > j ? 'YAY' : 'NO :('",i=10,j=20) # Error For Using ':(' Dont Use Signs
a.condition("i == j ? i : j",i=10,j=20)
print(ans)
print(a.exe("That $(dir) List : \n#(a = '12/23/2020'; a = a.replace('12/23/2020','Fake'); print(a))\n Finished :)"))

d = condition("i == j ? i : j",i=10,j=20,p=False)
pp(f"(Fore.RED)[{d}]")

print(a.condition("i == j ? '\eval()' : '\exec()'",i=10,j=2))

print(a.loop("<i:2,j:3>{We Are In Row (Fore.RED)[_i++_] And Column (Fore.RED)[_j++_] : }",'p'))
print(a.loop("<i:2>{Enter Your (Fore.RED)[Name] Person _i++_ : }",'i'))

########################## Stack ########################
# Model 1
a = Stack(inf=0,capacity=1)
a.push("test")
print(a.display())
a.pop()

# Model 2
a = Stack() # Infinite Stack
a.push("test")
print(a.display())
a.pop()
########################################################

########################## Queue ########################
# Model 1
a = Queue(inf=0,capacity=1)
a.add("test")
print(a.display())
a.remove()

# Model 2
a = Queue() # Infinite Stack
a.add("test")
print(a.display())
a.remove()
#########################################################

a = Auth(first_prompt="(Fore.CYAN)[Enter User :] ",second_prompt="(Fore.CYAN)[Enter Password :] ",mode=1)
print(a.auth(mask_color=fore["red"],inp_color=fore["yellow"]))

class Colors(Enum):
    Red = 0
    Green = 1
    Yellow = 2    

for c in Colors:
    print(c)


#####################################################
# You Can Use lambda Or You Can Use A Function Name #

# Model 1
var = 10
a = Switch(var)
a.cases({
    5:
        lambda: (
            print("Number Wasnt 5.") ,
            print(2)
        ),
    10:
        lambda: (
            print("Number Was 10 !") ,
            print(2)
        ),
    15:
        lambda: (
            print("Number Wasnt 15.") ,
            print(2)
        ),
    20:
        lambda: (
            print("Number Wasnt 20.") ,
            print(2)
        )
})

# Model 2
a = Switch(var)
a.cases({
    5:
        """print("Number Wasnt 5.") ;print(2)""",
    10:
        """print("Number Was 10 !") ;print(2)""",
    15:
        """print("Number Wasnt 15.") ;print(2)""",
    20:
        """print("Number Wasnt 20.") ;print(2)"""
})

# Model 3
a = Switch(var)
a.cases({
    5:
        [lambda num:print(num),(5,)],
    10:
        [lambda num:print(num),(10,)],
    15:
        [lambda num:print(num),(15,)],
    20:
        [lambda num:print(num),(20,)],
})

# Function Model

def test(num):
    print(num)

a = Switch(var)
a.cases({
    5:
        [test,(5,)],
    10:
        [test,(10,)],
    15:
        [test,(15,)],
    20:
        [test,(20,)],
})

# You Can Use lambda Or You Can Use A Function Name #
#####################################################