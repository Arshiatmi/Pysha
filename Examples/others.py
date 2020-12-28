from pysha import *
import time,random

@timer("Time Was (Fore.RED)[_H_] : (Fore.RED)[_M_] : (Fore.RED)[_S_] And In (Fore.CYAN)[_MS_] Miliseconds")
def test():
    print(fore["green"] + "Started" + fore["reset"])
    print(fore["green"] + "[+] " + fore["reset"] + "Loading...")
    time.sleep(random.randint(1,10) / 10)
    print(fore["red"] + "END" + fore["reset"])

test()

if between(":","Hello. The Character ':' Exists In Here ?","'"):
    print("Yes That Was Between Quotes !") # This Will Print
else:
    print("No :( colon Was Not Between Quotes.")

print(between_index(":",": Out Of Quote,':' In Quote","'")) # 16
print(not_between_index(":","':' In Quote,: Out Of Quote","'")) # 13