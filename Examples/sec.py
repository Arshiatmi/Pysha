from pysha import *

a = make_enc(Algorithms.XOR,10)
b = make_enc([Algorithms.XOR,Algorithms.Base64],10)
print(a.enc("Salam"))
print(b.enc("Salam"))
print(b.dec("WWtma2c="))