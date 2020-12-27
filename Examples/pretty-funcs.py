from pysha import *


pp("Salam",[1,2,3],["S","v"],[True,False],{"Salam":"Man Arshiam"})

rect("Test",distance_down=2,distance_up=2)

rect("Salam\nMan Arshiam :)",first_line=("-",Fore.YELLOW),last_line=("-",Fore.YELLOW),sep=("!",Fore.YELLOW),text_color=Fore.RED)

banner("Salam")

banner("Salam",font="3-d")

pp("(: (Fore.GREEN)[WElcome] To (Fore.RED)[T3sT] AppliCaTion :)",colon_c=Fore.RED)

l(('-',Fore.CYAN),count=50)

name = xp("(Fore.RED)[Enter Your Name :] ")

pp(f"Hello (Fore.RED)[{name}]")

name = colorprompt(colorize("(Fore.GREEN)[Enter Your Name :] "),char_color=fore["cyan"])
password = passprompt(colorize("(Fore.GREEN)[Enter Your Password :] "),mask_color=fore["cyan"])
pp(name)

a = PercentPrinter(chars=30)
a.increase(10)
a.show()
a.increase(10)
a.show()
a.increase(10)
a.show()
a.increase(10)
a.show()
a.increase(10)
a.show()
a.finish()
a.show()