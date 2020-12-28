from pysha import *

a = command()
ans = a.loop("<i:2,j:3>{Enter Your (Fore.RED)[Name] Person _i_ And _j_ : }")
a.condition('name == "Arshia" ? "Welcome" : "Nice To Meet You"',name="Arshia")
a.condition('i > j ? "YAY" : "NO"',i=10,j=20)
# a.condition("i > j ? 'YAY' : 'NO :('",i=10,j=20) # Do Not Use This Syntax. It Should Be C-Like Syntax Like "YAY" Not 'YAY'.
a.condition("i == j ? i : j",i=10,j=20)
print(ans)
print(a.exe("That $(dir) List : #(a = 'test'; a = a.replace('s',' - s - '); print(a)) Finished :)"))

d = condition("i == j ? i : j",i=10,j=20,p=False)
pp(f"(Fore.RED)[{d}]")

print(a.condition('i == j ? "\eval()" : "\exec()"',i=10,j=2))

print(a.loop("<i:2,j:3>{We Are In Row (Fore.RED)[_i++_] And Column (Fore.RED)[_j++_] : }",'p'))
print(a.loop("<i:2>{Enter Your (Fore.RED)[Name] Person _i++_ : }",'i'))