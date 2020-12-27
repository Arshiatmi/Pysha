from pysha import *
import time,random

@timer("Time Was (Fore.RED)[_H_] : (Fore.RED)[_M_] : (Fore.RED)[_S_] And In (Fore.CYAN)[_MS_] Miliseconds")
def test():
    print(fore["green"] + "Started" + fore["reset"])
    print(fore["green"] + "[+] " + fore["reset"] + "Loading...")
    time.sleep(random.randint(1,10) / 10)
    print(fore["red"] + "END" + fore["reset"])

test()


files = _("dir")
print(files)