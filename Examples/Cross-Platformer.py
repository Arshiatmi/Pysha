from pysha import *

cross_platform = CrossPlatformer()
cross_platform["clearScreen"] = {"windows": "cls", "linux": "clear"}
cross_platform["listFiles"] = {"windows": "dir", "linux": "ls"}


print(cross_platform["clearScreen"])  # It Will Return Value Depends On OS.
