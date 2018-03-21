import sys

# node class creates a node containing a key, a parent, a left node, and a right node
class Node:
	def __init__(self, newKey):
		self.key = newKey
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
		else:
			y.right = node

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

# returns a list containing the preoder sorting of the BST
	def to_list_preOrder(self):
		array = []
		x = self.root
		self.preOrder(x, array)
		return array

# recursive helper function to determine the preorder
	def preOrder(self, x, array):
		if x is not None:
			array.append(x.key)
			self.preOrder(x.left, array)
			self.preOrder(x.right, array)

# returns a list containing the inorder sorting of the BST
	def to_list_inOrder(self):
		array = []
		x = self.root
		self.inOrder(x, array)
		return array

# recursive helper function to determine the inorder
	def inOrder(self, x, array):
		if x is not None:
			self.inOrder(x.left, array)
			array.append(x.key)
			self.inOrder(x.right, array)

# returns a list containing the postorder sorting of the BST
	def to_list_postOrder(self):
		array = []
		x = self.root
		self.postOrder(x, array)
		return array

# recursive helper function to determine the postorder
	def postOrder(self, x, array):
		if x is not None:
			self.postOrder(x.left, array)
			self.postOrder(x.right, array)
			array.append(x.key)

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
			elif action == "search":
				value = int(value_option[0])
				search = b.search(b.root, value)
				if search is None:
					print("NotFound")
				else:
					print("Found")
			elif action == "max":
				if b.root is None:
					print("Empty")
				else:
					max = b.maximum(b.root)
					print(max.key)
			elif action == "min":
				if b.root is None:
					print("Empty")
				else:
					min = b.minimum(b.root)
					print(min.key)
			elif action == "preprint":
				if b.root is None:
					print("Empty")
				else:
					array = b.to_list_preOrder()
					print(*array)
			elif action == "inprint":
				if b.root is None:
					print("Empty")
				else:
					array = b.to_list_inOrder()
					print(*array)
			elif action == "postprint":
				if b.root is None:
					print("Empty")
				else:
					array = b.to_list_postOrder()
					print(*array)

# this code should work with either python or python3
if __name__ == "__main__":
	driver()
