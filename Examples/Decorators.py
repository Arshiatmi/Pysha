import random
import time
from pysha import *


# After Just Running The Code Once This Code Will Execute Anyway
@once
def init():
    print("Initializing")


# In Case of ZeroDivisionError, Ignore And Continue The Execution
@ignore(exceptions=[ZeroDivisionError])
def test():
    print(1 / 0)


# In Case of ZeroDivisionError, retry Until 3 times
@retry(count=3, exceptions=[ZeroDivisionError])
def calculation():
    print(1 / 0)


@timer("Time Was (Fore.RED)[_H_] : (Fore.RED)[_M_] : (Fore.RED)[_S_] And In (Fore.CYAN)[_MS_] Miliseconds")
def test():
    print(fore["green"] + "Started" + fore["reset"])
    print(fore["green"] + "[+] " + fore["reset"] + "Loading...")
    time.sleep(random.randint(1, 10) / 10)
    print(fore["red"] + "END" + fore["reset"])


test()
