from sys import argv
from redBlackTree import *

# an exception raised in the case that an incorrect order is asked for
class WrongOrder(Exception):
	def __init__(self, data=None):
		super().__init__(data)

# orders the sizes correctly by calling on a helper function
def findSubtreeSizes(self) -> None:
	self.findSizeHelp(self.root)

# a recursive helper function that will give each node the correct size
def findSizeHelp(self, x: RBNode) -> int:
	if x != self.nil:
		left = self.findSizeHelp(x.left)
		right = self.findSizeHelp(x.right)
		x.other = left + right + 1
		return x.other
	x.other = 0
	return x.other

# returns the node that is the kth smallest by calling a recursive helper function
def orderStatistic(self, k) -> RBNode:
	if k < 1 or k > self.root.other:
		raise RBTree.WrongOrder('orderStatistic({}) not found'.format(k))
	if k == 1:
		x = self.minimum(self.root)
	else:
		x = self.orderStatHelp(self.root, k)
	if x == self.nil:
		raise RBTree.WrongOrder('orderStatistic({}) not found'.format(k))
	return x

# a recursive helper function that will search for the kth smallest node
def orderStatHelp(self, x: RBNode, i) -> RBNode:
	if x != self.nil:
		i -= 1
		if i < x.left.other:
			x = self.orderStatHelp(x.left, i)
		elif i > x.left.other:
			x = self.orderStatHelp(x.right, i - (x.left.other))
	return x

# adds all previous functions and exceptions to the RBTree class
RBTree.WrongOrder = WrongOrder
RBTree.findSubtreeSizes = findSubtreeSizes
RBTree.findSizeHelp = findSizeHelp
RBTree.orderStatistic = orderStatistic
RBTree.orderStatHelp = orderStatHelp

# a driver function that is takes in the file and completes what is asked for
def main() -> None:
	st = RBTree()
	f = open(argv[1], "r")
	nl = int(f.readline().strip())
	for i in range(nl):
		l = f.readline().strip()
		if l == 'get_subtree_sizes':
			st.findSubtreeSizes()
		else:
			v = l.split()
			if v[0] == 'insert':
				k = int(v[1])
				z = RBNode(k, st.nil, 1)
				st.insert(z)
			elif v[0] == 'order':
				k = int(v[1])
				try:
					z = st.orderStatistic(k)
					print(z.key)
				except RBTree.WrongOrder as e:
					print('TreeError')
			else:
				print("illegal input line: ", l)
	f.close()

# this code should work with either python or python3
if __name__ == "__main__":
	main()