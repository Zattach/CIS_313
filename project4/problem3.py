import sys

# node class creates a node containing a key, a color, a parent, a left node, and a right node
class Node:
	def __init__(self, newKey, newColor, node):
		self.key = newKey
		self.color = newColor
		self.left = node
		self.right = node
		self.parent = node
		return

# RBT class creates a red-black tree
class RBT:

# defines an exception called Empty Tree for when there is no data in the tree
	class EmptyTree(Exception):
		def __init__(self, data=None):
			super().__init__(data)

# defines an exception called NotFound for when the item we search for cannot be found
	class NotFound(Exception):		
		def __init__(self, data=None):
			super().__init__(data)

# initializes the red-black tree by creating a sentinel node and a root
	def __init__(self):
		self.nil = Node(None, 'b', None)
		self.root = self.nil

# a fixer function to perform a left rotate performed in some cases to fix the red-black tree
	def leftRotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != self.nil:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

# a fixer function to perform a right rotate performed in some cases to fix the red-black tree
	def rightRotate(self, x):
		y = x.left
		x.left = y.right
		if y.right != self.nil:
			y.right.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.right:
			x.parent.right = y
		else:
			x.parent.left = y
		y.right = x
		x.parent = y

# a fixer function performed every time a node is inserted into the tree, it makes sure we meet the rules
	def insertFixup(self, z):
		while z.parent.color == 'r':
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == 'r':
					z.parent.color = 'b'
					y.color = 'b'
					z.parent.parent.color = 'r'
					z = z.parent.parent
				else:
					if z == z.parent.right:
						z = z.parent
						self.leftRotate(z.parent.parent)
					z.parent.color = 'b'
					z.parent.parent.color = 'r'
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y.color == 'r':
					z.parent.color = 'b'
					y.color = 'b'
					z.parent.parent.color = 'r'
					z = z.parent.parent
				else:
					if z == z.parent.left:
						z = z.parent
						self.rightRotate(z.parent.parent)
					z.parent.color = 'b'
					z.parent.parent.color = 'r'
					self.leftRotate(z.parent.parent)
		self.root.color = 'b'

# an insert function that determinesthe position of the node and then calls the fixer function
	def insert(self, z):
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
		z.left = self.nil
		z.right = self.nil
		z.color = 'r'
		self.insertFixup(z)

# a fixer function for remove that will replace one tree with another
	def transplant(self, u, v):
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

# a fixer function called every time a node is removed from the tree, it makes sure we follow the rules
	def removeFixup(x):
		while x != self.root and x.color == 'b':
			if x == x.parent.left:
				w = x.parent.right
				if w.color == 'r':
					w.color = 'b'
					x.parent.color = 'r'
					self.leftRotate(x.parent)
					w = x.parent.right
				if w.left.color == 'b' and w.right.color == 'b':
					w.color = 'r'
					x = x.parent
				else:
					if w.right.color == 'b':
						w.left.color = 'b'
						w.color = 'r'
						self.rightRotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = 'b'
					w.right.color = 'b'
					self.leftRotate(x.parent)
					x = self.root
			else: 
				if x == x.parent.right:
					w = x.parent.left
					if w.color == 'r':
						w.color = 'b'
						x.parent.color = 'r'
						self.rightRotate(x.parent)
						w = x.parent.left
					if w.right.color == 'b' and w.left.color == 'b':
						w.color = 'r'
						x = x.parent
					else:
						if w.left.color == 'b':
							w.right.color = 'b'
							w.color = 'r'
							self.leftRotate(w)
							w = x.parent.left
						w.color = x.parent.color
						x.parent.color = 'b'
						w.left.color = 'b'
						self.rightRotate(x.parent)
						x = self.root
		x.color = 'b'

# a function used to remove a node from the red-black tree
	def remove(self, z):
		y = z
		yOriginalcolor = y.color
		if z.left == self.nil:
			x = z.right
			self.transplant(z, z.right)
		elif z.right == self.nil:
			x = z.left
			self.transplant(z, z.left)
		else:
			y = self.minimum(z.right)
			yOriginalcolor = y.color
			x = y.right
			if y.parent == z:
				x.parent = y
			else:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self.transplant(z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if yOriginalcolor == 'b':
			self.removeFixup(x)

# a function that searches the tree for a certain node
	def search(self, x, key):
		while x != self.nil and key != x.key:
			if key < x.key:
				x = x.left
			else:
				x = x.right
		if x == self.nil:
			raise RBT.NotFound('NotFound')
		return x

# a function that returns the smallest node in the tree
	def minimum(self, x):
		if x == self.nil:
			raise RBT.EmptyTree('EmptyTree')
		while x.left != self.nil:
			x = x.left
		return x

# a function that returns the largest node in the tree
	def maximum(self, x):
		if x == self.nil:
			raise RBT.EmptyTree('EmptyTree')
		while x.right != self.nil:
			x = x.right
		return x

# a function that returns a list containing the tree in order from smallest to largest
	def inOrder(self):
		array = []
		self.inOrderHelper(self.root, array)
		return array

# a recursive helper function called by inOrder that will add each node to the list in order
	def inOrderHelper(self, node, array):
		if node != self.nil:
			self.inOrderHelper(node.left, array)
			array.append(node.key)
			self.inOrderHelper(node.right, array)

# a driver function that takes in a list of actions and numbers to use for the actions requested
def driver():
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		rb = RBT()
		for _ in range(n):
			in_data = f.readline().strip().split()
			action, valueOption = in_data[0], in_data[1:]
			if action == "insert":
				value = int(valueOption[0])
				node = Node(value, 'r', rb.nil)
				rb.insert(node)
			elif action == "remove":
				value = int(valueOption[0])
				try:
					node = rb.search(rb.root, value)
					rb.remove(node)
				except RBT.NotFound as e:
					print('TreeError')
			elif action == "search":
				value = int(valueOption[0])
				try:
					node = rb.search(rb.root, value)
					print('Found')
				except RBT.NotFound as e:
					print('NotFound')
			elif action == "max":
				try:
					x = rb.maximum(rb.root)
					print(x.key)
				except RBT.EmptyTree as e:
					print('Empty')
			elif action == "min":
				try:
					x = rb.minimum(rb.root)
					print(x.key)
				except RBT.EmptyTree as e:
					print('Empty')
			elif action == "inprint":
				l = rb.inOrder()
				if len(l) == 0:
					print("Empty")
				else:
					strings = [str(x) for x in l]
					print(' '.join(strings))
	f.close()

# this code should work with either python or python3
if __name__ == "__main__":
	driver()
