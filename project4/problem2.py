import sys

class STNode:

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None


class SyntaxTree:

    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None

        node = STNode(l[i])
        node.left = self.init_helper(2 * i, l)
        node.right = self.init_helper(2 * i + 1, l)
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(1, l)

    # method to generate fully parenthesized expression
    def parenthesize(self):
        array = []
        self.inOrder(self.root, array)
        return array

    # helper function for parenthesize
    def inOrder(self, x, array):
        if x is not None:
            if x.left is not None:
                array.append('(')
            self.inOrder(x.left, array)
            array.append(x.key)
            self.inOrder(x.right, array)
            if x.right is not None:
                array.append(')')

    # method to evaluate the expression
    def solve(self):
        answer = self.postOrder(self.root)
        return answer

    # helper function for solve
    def postOrder(self, x):
        if x is not None:
            a = self.postOrder(x.left)
            b = self.postOrder(x.right)
            if x.key is '+':
                return int(a) + int(b)
            elif x.key is '-':
                return int(a) - int(b)
            elif x.key is '*':
                return int(a) * int(b)
            else:
                return x.key


# driver that takes in a list of actions and numbers to use for the actions requested
def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        in_data = f.readline().strip().split()
        array = []
        array.append(in_data[0])
        for _ in range(n):
            array.append(in_data[_])
        s = SyntaxTree(array)

        print(*s.parenthesize(), sep='')
        print(s.solve())


# this code should work with either python or python3
if __name__ == "__main__":
    driver()
