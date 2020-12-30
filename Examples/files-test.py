from pysha import *
import sys

thismodule = sys.modules[__name__]

create_dir("test",create_parents=False) # create_parents Default Is False

write_file("test/test.txt","This Is A Test Text")

pp(read_file("test/test.txt"))

append_file("test/test.txt","\n New Line Added :)")

pp(read_file("test/test.txt"))

rm_dir("test",force=True)


#########################################
# Save & Load Variables With Encryption #
#########################################

# Model 1
a = Save("test.txt",name="Arshia",family="Tamimi",age=19)
a.save()  # Or -> a() <-

# Model 2
Save("test.txt",name="Arshia",family="Tamimi",age=19)()

# ----------------------------------------------

# Model 1
b = Load("test.txt")
b.load(thismodule) # Or -> b(thismodule) <-

# Model 2
Load("test.txt")(thismodule)

print(name)