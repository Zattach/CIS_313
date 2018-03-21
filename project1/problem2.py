import sys
import copy
from linked_list import *


# custom Underflow exception
class Underflow(Exception):
    pass  # make it fancier if you want :)

class Overflow(Exception):
    pass

# Queue class
class Queue:

    # class constructor
    def __init__(self):
        self.list = List()
        return

    # enqueue method
    def enqueue(self, x):
        self.list.add(x)
        return

    # dequeue method
    def dequeue(self):
        return self.list.rem(True)

    # is_empty method
    def is_empty(self):
        return self.list.list_empty()


# args: q, Queue
def print_queue(q):
    if q.is_empty():
        print("Empty")
    else:
        temp = Queue()
        temp = copy.deepcopy(q)
        while temp.list.tail.getPrev() != None:
            value = temp.dequeue()
            print(value, end=' ')
        value = temp.dequeue()
        print(value)
    return


# this function runs the program according to the problem specification
def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)

            elif action == "dequeue":
                try:
                    value = q.dequeue()
                    print(value)
                except:
                    print("QueueError")

            elif action == "print":
                print_queue(q)


# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
