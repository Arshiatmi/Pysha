from pysha import *

a = make_enc(Algorithms.XOR,10)
b = make_enc([Algorithms.XOR,Algorithms.Base64],10)
print(a[0]("Salam"))
print(b[0]("Salam"))
print(b[1]("WWtma2c="))