# Pysha
Pysha Micro Framework. For Doing Something Beautiful In Python :)

Because Currently This Micro Framework Is In Progress, I Will Some Helps Later.

## Installation

Just Run This Command :

`pip install pysha`

## Examples

* Switch-Case

```
Switch(var).cases({
    5:
        lambda: (
            print("Number Wasnt 5.") ,
            print(2)
        ),
    10:
        lambda: (
            print("Number Was 10 !") ,
            print(3)
        ),
    15:
        lambda: (
            print("Number Wasnt 15.") ,
            print(4)
        ),
    20:
        lambda: (
            print("Number Wasnt 20.") ,
            print(5)
        ),
    lambda:"default":
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

**After Load Variables, They Are Accessable In Your Code ! **

And Lots Of Beautiful Things :)

You Can Look At [Full Wiki](https://github.com/Arshiatmi/Pysha/wiki) To See More :)
