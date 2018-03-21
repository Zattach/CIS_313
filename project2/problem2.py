import sys

# implements a stack that is used to solve the problem
class Stack:

# creates the underflow exception, should be unnecessary as underflow will just respond with "NO" 
    class Underflow(Exception):
        def __init__(self, data=None):
            super().__init__(data)

# used to create nodes in the stack
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

# initializes the stack
    def __init__(self):
        self.head = None

# pushes a character onto the stack
    def push(self, c):
        n = self.Node(c)
        n.next = self.head
        self.head = n

# pops the top node off of the stack
    def pop(self):
        if self.head == None:
            raise Stack.Underflow("StackError")
        n = self.head
        self.head = n.next
        return n.data

# returns if the stack is empty
    def is_empty(self) -> bool:
        if self.head == None:
            return True
        else:
            return False

# determines if the given string is a well formed set of brackets. Returns false if something other than a bracket is included
def formed(data) -> bool:
    s = Stack()
    closed = True
    for i in range(0, len(data)):
        if (data[i] == '(') | (data[i] == '[') | (data[i] == '<') | (data[i] == '{'):
            s.push(data[i])
        elif s.is_empty():
            closed = False
        elif (data[i] == ')') | (data[i] == ']') | (data[i] == '>') | (data[i] == '}'):
            testChar = s.pop()
            if (data[i] == ')') & (testChar != '('):
                closed = False
            elif (data[i] == ']') & (testChar != '['):
                closed = False
            elif (data[i] == '>') & (testChar != '<'):
                closed = False
            elif (data[i] == '}') & (testChar != '{'):
                closed = False
        else:
            closed = False
    return closed

# main function that will read in file and call formed
def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip()
            if formed(in_data):
                print("YES")
            else:
                print("NO")


# this code should work with either python or python3
if __name__ == "__main__":
    driver()
