from pysha import *


create_dir("test",create_parents=False) # create_parents Default Is False

write_file("test/test.txt","This Is A Test Text")

pp(read_file("test/test.txt"))

append_file("test/test.txt","\n New Line Added :)")

pp(read_file("test/test.txt"))

rm_dir("test",force=True)
