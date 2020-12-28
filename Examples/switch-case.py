from pysha import *


#####################################################
# You Can Use lambda Or You Can Use A Function Name #

class Colors(Enum):
    Red = 0
    Yellow = 1
    Green = 2

color = Colors.Red

Switch(color).cases({
    Case(Colors.Red) :
        lambda:(
            print("Thats Red !")
        ),
    Case(Colors.Yellow) :
        lambda:(
            print("Thats Yellow")
        ),
    Default:
        lambda:(
            print("That Was Something Else :(")
        )
})


var = 25

################################################
# You Can Not Do for loop Or if-else In lambda #
################################################
# Main Model
a = Switch(var)
a.cases({
    Case(5)  : 
        lambda:(
            setattr(Vars,"a","Hello 0"),
            print("Thats It !"),
            print(getattr(Vars,"a"))
        ),
    Case(10) : 
        lambda:(
            setattr(Vars,"a","Hello 1"),
            print("Thats It !"),
            print(getattr(Vars,"a"))
        ),
    Case(15) : 
        lambda:(
            setattr(Vars,"a","Hello 2"),
            print("Thats It !"),
            print(getattr(Vars,"a"))
        ),
    Default : 
        lambda:(
            setattr(Vars,"a","Default Hello"),
            print("Thats It !"),
            print(getattr(Vars,"a"))
        )
})


################################################
# You Can Not Do for loop Or if-else In lambda #
################################################
# Model 1
a = Switch(var)
a.cases({
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

##################################
# Feel Free To Code In String :) #
##################################
# Model 2
a = Switch(var)
a.cases({
    5:
        """
            i = 2
            print("Number Wasnt 5.")
            print(i)
        """,
    10:
        """
            i = 2
            print("Number Was 10 !")
            print(i)
        """,
    15:
        """
            i = 2
            print("Number Wasnt 15.")
            print(i)
        """,
    20:
        """
            i = 2
            print("Number Wasnt 20.")
            print(i)
        """,
    Default:
        """
            i = 2
            print("Number Wasnt 20.")
            print(i)
        """
})

#######################################
# Pass A List Like [func,args,kwargs] #
#######################################
# Model 3
a = Switch(var)
a.cases({
    5:
        [
            lambda num:(print(num)), # Function 
            (5,), # Arguments
            {} # Keywords Arguments
        ],
    10:
        [
            lambda num:(print(num)),
            (10,)
        ],
    15:
        [
            lambda num:(print(num)),
            (15,)
        ],
    20:
        [
            lambda num:(print(num)),
            (20,)
        ],
})

#######################################
# Pass A List Like [func,args,kwargs] #
#######################################

# Function Model
def test(num):
    print(num)

a = Switch(var)
a.cases({
    5:
        [
            test, # Function Name
            (5,), # Arguments
            {} # Keyword Argguments
        ],
    10:
        [
            test,
            (10,)
        ],
    15:
        [
            test,
            (15,)
        ],
    20:
        [
            test,
            (20,)
        ],
})

# You Can Use lambda Or You Can Use A Function Name #
#####################################################