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
