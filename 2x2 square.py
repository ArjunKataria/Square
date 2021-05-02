# This function prints string twice
def do_twice(s):
    print(s)
    print(s)

# This function prints string four times
def do_fourth(s):
    do_twice(s)
    do_twice(s)

line = "+ - - - - + - - - - +"
pillar = "|         |         |"

# Creates a box
def box():
    print(line)
    do_fourth(pillar)
    print(line)
    do_fourth(pillar)
    print(line)

box()

