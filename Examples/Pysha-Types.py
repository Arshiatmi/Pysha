from pysha import *

#######################################################
#                                                     #
#                      PyshaString                    #
#                                                     #
#######################################################

# This Is PyshaString Type
a = PyshaString("Hello There")

# All Of Normal String Functions Will Work Here
print(a.count("H"))

# Special Things That PyshaString Has Is :
print(a << " And Welcome")  # Concatenation To The End
print(a >> "Yo, ")  # Concatenation At The Start

# If You Want To Set This Variable Too, Use >>= And <<=
a <<= " And Welcome"
a >>= "Yo, "
print(a)

# Or If You Want You Can Even Use += That Works Like <<=
a += "... Again, Welcome :)"

print(a - "Hello")  # Subtraction

# Like Concationation, You Can Use -=
a -= "Hello"
print(a)

# You Can Replace A Dictionary !
# You Can Do It With list Too But Dictionary Is Better I Think :)
# Dictionary :
a.replace_dict({"Yo": "Hi", "There": "There"})
print(a)

# List :
a.replace_array(["Yo", "There"], ["Hi", "There"])
print(a)

# Wait For Good Ones !

# Get First Index Of Some Characters
print(a.find_first([" ", ","]))  # Returns Index Of ","
print(a.find_last([" ", ","]))  # Returns Index Of Last " "

# Returns The Character "," Itself, Shows It Came First.
print(a.find_first([" ", ","], return_type=str))

# Super Power Part !
a = PyshaString("H")
print(a.inside(["Hello", "There"]))  # Returns True Because H Is In "Hello"

# It Will Return False Because H Is Not In Keys Of Dictionary
print(a.inside({"name": "Arshia", "Family": "Tamimi", "Status": "Hopeful"}))

# If You Want To Search In Values :
print(a.inside({"name": "Arshia", "Family": "Tamimi",
                "Status": "Hopeful"}, search_mode="value"))

# If You Want To Search In Keys And Values :
print(a.inside({"name": "Arshia", "Family": "Tamimi",
                "Status": "Hopeful"}, search_mode="both"))

# There Is Something Better Here !
# You Can Choose What inside Method Returns If You Pass A Dictionary To Search.
print(a.inside({"name": "Arshia", "Family": "Tamimi",
                "Status": "Hopeful"}, search_mode="both", return_type=dict))
"""
    Default Of return_type is bool That Returns If It Finds Or Not.
    dict Will Return {"Status": "Hopeful"} As Output Here.
    If You Pass Any Other Types In return_type, It Will Return oposite Of search_mode.
    If search_mode is both, It Will Return Value Of Found String.
"""

print(a.inside({"name": "Arshia", "Family": "Tamimi",
                "Status": "Hopeful"}, search_mode="both", return_type=str))  # It Will Return "Hopeful" As Output Here.

print(a.inside({"name": "Arshia", "Family": "Tamimi",
                "Status": "Hopeful"}, search_mode="key", return_type=str))  # It Will Return "Hopeful" As Output Here.

print(a.inside({"name": "Arshia", "Family": "Tamimi",
                "Status": "Hopeful"}, search_mode="value", return_type=str))  # It Will Return "Status" As Output Here.

#-----------------------------------------------------#

#######################################################
#                                                     #
#                       PyshaDict                     #
#                                                     #
#######################################################

# This Is PyshaDict Type
a = PyshaDict(
    {"name": "Arshia", "nickname": "MrMegaExpert", "Status": "Hopeful"})

# Inverse Of Dictionary
print(a.inverse)

# Or You Can Get inverse Like This :
print(~a)

# Get Key From Value !
print(a.inverse.get("Tamimi"))

#-----------------------------------------------------#
