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

- Switch-Case

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

- Interface ( exists in github but you can not use this in current pip version )

```
@interface
class Car:
    name = None
    speed = 0

    def setSpeed(self,speed):
        pass


@interface(Car)
class Tesla:
    name = "Tesla"
    speed = 0

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed


@interface(Car) # Wrong Because setSpeed Is Not Defined. ( Will Raise Error )
class BMW:
    name = "BMW"
    speed = 0

@interface(Car) # Wrong Because setSpeed Is Not Defined Right ( Parameter Problem ). ( Will Raise Error )
class Benz:
    name = "Benz"
    speed = 0

    def setSpeed(self):
        pass


myCar = Tesla()
myFriendCar = BMW() # Raises Error Because BMW Does Not Have setSpeed Method.
myCar.setSpeed(100)
# Rest Of Your Code...
```

- Pysha Types

```
# PyshaString
a = PyshaString("some string")
print(a << " and something else") # "some string and something else"
print(a - "some") # " string"
print(a.replace_dict({"some":"one","string":"int"})) # "one int"

# PyshaDict
b = PyshaDict({"name":"Arshia"})
print(~b) # {"Arshia":"name"}
print(b - "name") # {}
print(~b.get("Arshia")) # "name"

# PyshaList
c = PyshaList(["name","hay"])
print(c.count_deep("a")) # 2
print(c >> 1) # ["hay","name"] thats just right shift
print(c) # [ name, hay ]
print(c + ["yo"]) # ["name","hay","yo"]

```

- One line Conditions

```
a = command()
print(a.condition("i > j ? i:j",i=10,j=20))

# Or this way
print(Cond(i>j)(i,j)) # This command still is not on pip newest version
```

- One line loop

```
a = command()
a.loop("<i:2,j:3>{hey thats _j_ index in _i_ column}",mode="i")
# "p" mode is for just printing and "i" mode is for get input.

# Or this way ( Not still in newest pip version )
ans = Loop(2,3)("Whats number [_1_][_2_] ?")
# This will automatically loop through an array[2][3] and get input from it and will return answer
```

- CrossPlatformer ( You can make cross platform apps easier )

```
cp = CrossPlatformer()
cp["clearScreen"] = {"windows": "cls", "linux": "clear","mac":"clear"}
cp["listFiles"] = {"windows": "dir", "linux": "ls","mac":"clear"}

# rest of your code...

print(cp["clearScreen"]) # automatically returns value depends on your platform.
```

- Cool Decorators

```
# just for no argument functions that runs once without calling it
@once
def init():
    print("Initializing")

# ignore and continue the process in case of ZeroDivisonError ( you can set '*' to ignore everything )
@ignore(exceptions=[ZeroDivisionError])
def test():
    print(1 / 0)

# retry the function in case of ZeroDivisonError until 3 times ( you can set '*' to ignore everything )
@retry(count=3, exceptions=[ZeroDivisionError])
def calculation():
    print(1 / 0)
```

- Multi-Layer Ecnryption/Decryption

```
variable = make_enc(alg=[Algorithms.XOR,Algorithms.Base64],key=10)
variable.enc("Hello")
variable.dec("Qm9mZmU=")
```

- Colored User-Input

```
name = colorprompt(colorize("(Fore.GREEN)[Enter Your Name :] "),char_color=fore["cyan"])
password = passprompt(colorize("(Fore.GREEN)[Enter Your Password :] "),mask_color=fore["cyan"])
pp(name)
```

- Text Options

```
banner("text",font="3-D") # make cool text with setted font ( uses pyfiglet and figlet fonts )
rect("Hello\nI'm Arshia") # all characters and colors even distances can be customized too
# Customizing helps will be added on wiki

l(('-', Fore.CYAN), count=50) # Draw a line with specific character and color

# and some other cool things :)
```

- Customizable PercentPrinter

```
a = PercentPrinter(chars=30,pass_color=fore["green"],loading_color=fore["cyan"])
a.config(char_ok='@',char_loading='-')
a.show(char_ok='%',char_loading='`') # Overwrite Config But Not Changes It.
a.increase(50)
a.finish(show=False)
print("Done")
```

- Save And Load Variables With Encryption

```
# Save 2 Variables
Save("test.txt",name="Arshia",age=19)()

# Load Those 2 Variables
import sys
this = sys.modules[__name__]

Load("test.txt")(this)
```

**After Load Variables, They Are Accessable In Your Code !**

And Lots Of Beautiful Things :)

You Can Look At More [Examples](https://github.com/Arshiatmi/Pysha/tree/master/Examples) Or [Docs](https://pysha.readthedocs.io/en/latest/) To See More :)
