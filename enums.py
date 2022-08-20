from enum import *

class Algorithms(Enum):
    XOR = 0
    Base64 = 1
    Cipher = 2
    Base85 = 3
    Base32 = 4
    Base16 = 5
    ROT13 = 6

class AIModes(Enum):
    All = 0
    Some = 1