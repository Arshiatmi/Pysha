from pysha import *

class Colors(Enum):
    Red = 0
    Green = 1
    Yellow = 2    

print()

for c in Colors:
    print(c)

print()

print(Colors.Red.name,Colors.Red.value)
print(Colors.Green.name,Colors.Green.value)
print(Colors.Yellow.name,Colors.Yellow.value)

print()

print(Colors.Red.value == 0)