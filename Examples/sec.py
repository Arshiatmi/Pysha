from pysha import *

# a = make_enc(Algorithms.XOR,10)
b = make_enc([Algorithms.XOR,Algorithms.Base64],10)
# print(a.enc("Hello"))
print(b.enc("Hello"))
# print(b.dec("Qm9mZmU="))