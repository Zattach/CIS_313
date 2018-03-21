import sys
import copy
from linked_list import *


# custom Underflow exception
class Underflow(Exception):
    pass  # make it fancier if you want :)

# Stack class
class Stack:

    # class constructor
    def __init__(self):
        self.list = List()
        return

    # push method
    def push(self, x):
        self.list.add(x)
        return

    # pop method
    def pop(self):
        return self.list.rem(False)

    # is_empty method
    def is_empty(self):
        return self.list.list_empty()


# args: s, Stack
def print_stack(s):
    if s.is_empty():
        print("Empty")
    else:
        temp = Stack()
        temp = copy.deepcopy(s)
        while temp.list.head.getNext() != None:
            value = temp.pop()
            print(value, end=' ')
        value = temp.pop()
        print(value)
    return


# this function runs the program according to the problem specification
def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                s.push(value)

            elif action == "pop":
                try:
                    value = s.pop()
                    print(value)
                except:
                    print("StackError")

            elif action == "print":
                print_stack(s)


# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
