from pysha import *

a = Auth(first_prompt="(Fore.CYAN)[Enter User :] ",second_prompt="(Fore.CYAN)[Enter Password :] ",mode=1)
print(a.auth(mask_color=fore["red"],inp_color=fore["yellow"]))

name = colorprompt(colorize("(Fore.GREEN)[Enter Your Name :] "),char_color=fore["cyan"])
password = passprompt(colorize("(Fore.GREEN)[Enter Your Password :] "),mask_color=fore["cyan"])
pp(name)