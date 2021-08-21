from typing import NamedTuple

name = ()

def insertAndReturn(name):
    name = input("input your name: ")
    print("")
    print("Your name is: " + name)

insertAndReturn(name)
