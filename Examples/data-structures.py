from pysha import *


########################## Stack ########################
# Model 1
a = Stack(inf=0,capacity=1)
a.push("test")
print(a.display())
a.pop()

# Model 2
a = Stack() # Infinite Stack
a.push("test")
print(a.display())
a.pop()
########################################################

########################## Queue ########################
# Model 1
a = Queue(inf=0,capacity=1)
a.add("test")
print(a.display())
a.remove()

# Model 2
a = Queue() # Infinite Stack
a.add("test")
print(a.display())
a.remove()
#########################################################