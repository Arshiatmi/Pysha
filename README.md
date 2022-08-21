# Pysha
Pysha Micro Framework. For Doing Something Beautiful In Python :)

You can See examples of pysha in Examples directory.

## Installation

Just Run This Command :

`pip install pysha`

## Usage
Add This At First Of Your Code :

`from pysha import *`

### Examples

* Switch-Case

```
Switch(var).cases({
    Case(5):
        lambda: (
            print("Number Wasnt 5.") ,
            print(2)
        ),
    Case(10):
        lambda: (
            print("Number Was 10 !") ,
            print(3)
        ),
    Case(15):
        lambda: (
            print("Number Wasnt 15.") ,
            print(4)
        ),
    Case(20):
        lambda: (
            print("Number Wasnt 20.") ,
            print(5)
        ),
    Default:
        lambda:(
            print("Finish")
        )
})
```

* Multi-Layer Ecnryption/Decryption

```
variable = make_enc(alg=[Algorithms.XOR,Algorithms.Base64],key=10)
variable.enc("Hello")
variable.dec("Qm9mZmU=")
```

* Colored User-Input

```
name = colorprompt(colorize("(Fore.GREEN)[Enter Your Name :] "),char_color=fore["cyan"])
password = passprompt(colorize("(Fore.GREEN)[Enter Your Password :] "),mask_color=fore["cyan"])
pp(name)
```

* Save And Load Variables With Encryption

```
# Save 2 Variables
Save("test.txt",name="Arshia",age=19)()

# Load Those 2 Variables
import sys
this = sys.modules[__name__]

Load("test.txt")(this)
```

**After Load Variables, They Are Accessable In Your Code !**

* Pysha Types

```
# PyshaString
a = PyshaString("some string")
print(a << " and something else") # "some string and something else"
print(a - "some") # " string"
print(a.replace_dict({"some":"one","string":"str"})) # "one int"

# PyshaDict
b = PyshaDict({"name":"Arshia"})
print(~b) # {"Arshia":"name"}
print(b - "name") # {}

# PyshaList
c = PyshaList(["name","hay"])
print(c.count_deep("a")) # 2
print(c >> 1) # ["hay","name"]
print(c) # [ name, hay ]
print(c + ["yo"]) # ["name","hay","yo"]

```

And Lots Of Beautiful Things :)

You Can Look At [Full Wiki](https://github.com/Arshiatmi/Pysha/wiki) To See More :)
