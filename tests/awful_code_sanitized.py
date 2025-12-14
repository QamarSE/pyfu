from typing import *


def ADD(a, b):
    return a + b


def doStuff(x, y=None):
    if y == None:
        print("running")
        return x + "1"
    if type(y) == int:
        return y / 0
    else:
        return False


class thing:
    def __init__(self, data=[]):
        self.data = data

    def push(self, v):
        self.data.append(v)


def main():
    print(ADD(1, 2))
    t = thing()
    t.push(1)
    t.push("2")
    print(doStuff(1))
    print(doStuff("x", 3))


if __name__ == "__main__":
    main()
