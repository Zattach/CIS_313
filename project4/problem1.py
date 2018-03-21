import sys

# node class creates a node containing a key, a parent, a left node, and a right node
class Node:
	def __init__(self, newKey):
		self.key = newKey
		self.val = 0
		self.left = None
		self.right = None
		self.parent = None
		return

# BST class creates a binary search tree
class BST:
	class Underflow(Exception):
		def __init__(self, data=None):
			super().__init__(data)

# initializes the binary search tree
	def __init__(self):
		self.root = None
		self.best = None

# inserts a node onto the binary search tree and reconfigures it's parent, left, and right
	def insert(self, node):
		y = None
		x = self.root
		while x is not None:
			y = x
			if node.key < x.key:
				x = x.left
			else:
				x = x.right
		node.parent = y
		if y is None:
			self.root = node
		elif node.key < y.key:
			y.left = node
			node.val = y.val
		else:
			y.right = node
			node.val = y.val
		if node.key % 10 is 5:
			n = abs(node.key)
			array = [int(d) for d in str(n)]
			node.val += array.count(5)

# removes a node from the tree and reconfigures any nodes around it
	def remove(self, node):
		if node.left is None:
			self.transplant(node, node.right)
		elif node.right is None:
			self.transplant(node, node.left)
		else:
			y = self.minimum(node.right)
			if y.parent is not node:
				self.transplant(y, y.right)
				y.right = node.right
				y.right.parent = y
			self.transplant(node, y)
			y.left = node.left
			y.left.parent = y

# transplants trees messed up by remove
	def transplant(self, u, v):
		if u.parent is None:
			self.root = v
		elif u is u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v is not None:
			v.parent = u.parent

# searches the tree for a specific node, returns Not Found if not found
	def search(self, x, key) -> Node:
		while x is not None and key is not x.key:
			if key < x.key:
				x = x.left
			else:
				x = x.right
		return x

# returns the smallest value in the tree
	def minimum(self, x):
		while x.left is not None:
			x = x.left
		return x

# returns the largest value in the tree
	def maximum(self, x):
		while x.right is not None:
			x = x.right
		return x

# returns the best path value of the tree
	def best_path_value(self) -> int:
		if self.root is None:
			return 0
		self.best = self.root
		self.findBest(self.root)
		return self.best.val

# a helper function used to find the best node
	def findBest(self, x):
		if x is not None:
			if x.val > self.best.val:
				self.best = x
			self.findBest(x.left)
			self.findBest(x.right)

# driver that takes in a list of actions and numbers to use for the actions requested
def driver():
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		b = BST()
		for _ in range(n):
			in_data = f.readline().strip().split()
			action, value_option = in_data[0], in_data[1:]
			if action == "insert":
				value = int(value_option[0])
				node = Node(value)
				b.insert(node)
			elif action == "remove":
				value = int(value_option[0])
				node = b.search(b.root, value)
				if node is None:
					print("TreeError")
				else:
					b.remove(b.search(b.root, value))
			elif action == "bpv":
				value = b.best_path_value()
				if value is 0:
					print("TreeError")
				else:
					print(value)

# this code should work with either python or python3
if __name__ == "__main__":
	driver()
