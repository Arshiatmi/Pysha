from pysha import *


#####################################################
# You Can Use lambda Or You Can Use A Function Name #


var = 25

###########################################
# You Can Not Define A Variable In lambda #
###########################################
# Main Model
a = Switch(var)
a.cases({
    Case(5)  : 
        lambda:(
            print("Thats It !")
        ),
    Case(10) : 
        lambda:(
            print("Thats It !")
        ),
    Case(15) : 
        lambda:(
            print("Thats It !")
        ),
    Default : 
        lambda:(
            print("Thats It !")
        )
})


###########################################
# You Can Not Define A Variable In lambda #
###########################################
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

######################################################
# You Have To Use 'exec' Function To Define Variable #
######################################################
# Model 2
a = Switch(var)
a.cases({
    5:
        """
            exec("i = 2")
            print("Number Wasnt 5.")
            print(i)
        """,
    10:
        """
            exec("i = 2")
            print("Number Was 10 !")
            print(i)
        """,
    15:
        """
            exec("i = 2")
            print("Number Wasnt 15.")
            print(i)
        """,
    20:
        """
            exec("i = 2")
            print("Number Wasnt 20.")
            print(i)
        """,
    Default:
        """
            exec("i = 2")
            print("Number Wasnt 20.")
            print(i)
        """
})

######################################################
# You Have To Use 'exec' Function To Define Variable #
######################################################
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