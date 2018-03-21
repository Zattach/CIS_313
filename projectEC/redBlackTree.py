# from sys import argv
from enum import Enum

class Color(Enum):
	RED = 1
	BLACK = 2

class RBNode:
	def __init__(self, x: "comparable", tDotNil, other=None):
		self.key = x
		self.other = other
		self.color = Color.RED
		self.left = tDotNil
		self.right = tDotNil
		self.parent = tDotNil

class RBTree:
	class EmptyTree(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	class NotFound(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	def __init__(self, other=None):
		self.root = self.nil = RBNode(None, None, other)
		self.nil.color = Color.BLACK

	def leftRotate(self, x: RBNode) -> None:
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

	def rightRotate(self, x: RBNode) -> None:
		y = x.left
		x.left = y.right
		if y.right != self.nil:
			y.right.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.right = x
		x.parent = y

	def insert(self, z: RBNode) -> None:
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
		z.left = z.right = self.nil
		z.color = Color.RED
		self.insertFixup(z)

	def insertFixup(self, z) -> None:
		while z.parent.color == Color.RED:
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == Color.RED:
					z.parent.color = Color.BLACK
					y.color = Color.BLACK
					z.parent.parent.color = Color.RED
					z = z.parent.parent
				else:
					if z == z.parent.right:
						z = z.parent
						self.leftRotate(z)
					z.parent.color = Color.BLACK
					z.parent.parent.color = Color.RED
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y.color == Color.RED:
					z.parent.color = Color.BLACK
					y.color = Color.BLACK
					z.parent.parent.color = Color.RED
					z = z.parent.parent
				else:
					if z == z.parent.left:
						z = z.parent
						self.rightRotate(z)
					z.parent.color = Color.BLACK
					z.parent.parent.color = Color.RED
					self.leftRotate(z.parent.parent)
		self.root.color = Color.BLACK

	def searchIterative(self, x: RBNode, k: "comparable") -> RBNode:
		while x != self.nil and k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def search(self, x: RBNode, k: "comparable") -> RBNode:
		z = self.searchIterative(x, k)
		if z == self.nil:
			raise RBTree.NotFound('search({}) not found'.format(k))
		return z

	def minimum(self, x: RBNode) -> RBNode:
		if x == self.nil:
			raise RBTree.EmptyTree('minimum() invoked on empty tree')
		while x.left != self.nil:
			x = x.left
		return x

	def maximum(self, x: RBNode) -> RBNode:
		if x == self.nil:
			raise RBTree.EmptyTree('maximum() invoked on empty tree')
		while x.right != self.nil:
			x = x.right
		return x

	def transplant(self, u: RBNode, v: RBNode) -> None:
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	def remove(self, x: RBNode) -> None:
		z = self.searchIterative(self.root, x.key)
		if z == self.nil:
			raise RBTree.NotFound('delete() cannot find element')
		y = z
		yOriginalColor = y.color
		if z.left == self.nil:
			x = z.right
			self.transplant(z, z.right)
		elif z.right == self.nil:
			x = z.left
			self.transplant(z, z.left)
		else:
			y = self.minimum(z.right)
			yOriginalColor = y.color
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
		if yOriginalColor == Color.BLACK:
			self.removeFixup(x)

	def removeFixup(self, x: RBNode) -> None:
		while x != self.root and x.color == Color.BLACK:
			if x == x.parent.left:
				w = x.parent.right
				if w.color == Color.RED:
					w.color = Color.BLACK
					x.parent.color = Color.RED
					self.leftRotate(x.parent)
					w = x.parent.right
				if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
					w.color = Color.RED
					x = x.parent
				else:
					if w.right.color == Color.BLACK:
						w.left.color = Color.BLACK
						w.color = Color.RED
						self.rightRotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = Color.BLACK
					w.right.color = Color.BLACK
					self.leftRotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == Color.RED:
					w.color = Color.BLACK
					x.parent.color = Color.RED
					self.rightRotate(x.parent)
					w = x.parent.left
				if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
					w.color = Color.RED
					x = x.parent
				else:
					if w.left.color == Color.BLACK:
						w.right.color = Color.BLACK
						w.color = Color.RED
						elf.leftRotate(w)
					w.color = x.parent.color
					x.parent.color = Color.BLACK
					w.left.color = Color.BLACK
					self.rightRotate(x.parent)
					x = self.root
		x.color = Color.BLACK

	def preOrderHelper(self, n: RBNode, l: "list of keys") -> None:
		if n != self.nil:
			l.append(n.key)
			self.preOrderHelper(n.left, l)
			self.preOrderHelper(n.right, l)

	def preOrder(self) -> "list of keys":
		l = []
		self.preOrderHelper(self.root, l)
		return l

	def inOrderHelper(self, n: RBNode, l: "list of keys") -> None:
		if n != self.nil:
			self.inOrderHelper(n.left, l)
			l.append(n.key)
			self.inOrderHelper(n.right, l)

	def inOrder(self) -> "list of keys":
		l = []
		self.inOrderHelper(self.root, l)
		return l

	def postOrderHelper(self, n: RBNode, l: "list of keys") -> None:
		if n != self.nil:
			self.postOrderHelper(n.left, l)
			self.postOrderHelper(n.right, l)
			l.append(n.key)

	def postOrder(self) -> "list of keys":
		l = []
		self.postOrderHelper(self.root, l)
		return l

# def main() -> None:
# 	st = RBTree()
# 	f = open(argv[1], "r")
# 	nl = int(f.readline().strip())
# 	for i in range(nl):
# 		l = f.readline().strip()
# 		if l == 'max':
# 			try:
# 				x = st.maximum(st.root)
# 				print(x.key)
# 			except RBTree.EmptyTree as e:
# 				print('Empty')
# 		elif l == 'min':
# 			try:
# 				x = st.minimum(st.root)
# 				print(x.key)
# 			except RBTree.EmptyTree as e:
# 				print('Empty')
# 		elif l == 'preprint':
# 			keys = st.preOrder()
# 			if len(keys) == 0:
# 				print('Empty')
# 			else:
# 				strings = [str(x) for x in keys]
# 				print(' '.join(strings))
# 		elif l == 'inprint':
# 			keys = st.inOrder()
# 			if len(keys) == 0:
# 				print('Empty')
# 			else:
# 				strings = [str(x) for x in keys]
# 				print(' '.join(strings))
# 		elif l == 'postprint':
# 			keys = st.postOrder()
# 			if len(keys) == 0:
# 				print('Empty')
# 			else:
# 				strings = [str(x) for x in keys]
# 				print(' '.join(strings))
# 		else:
# 			v = l.split()
# 			if v[0] == 'insert':
# 				k = int(v[1])
# 				z = RBNode(k, st.nil)
# 				st.insert(z)
# 			elif v[0] == 'remove':
# 				k = int(v[1])
# 				try:
# 					z = st.search(st.root, k)
# 					st.remove(z)
# 				except RBTree.NotFound as e:
# 					print('TreeError')
# 			elif v[0] == 'search':
# 				k = int(v[1])
# 				try:
# 					z = st.search(st.root, k)
# 					print('Found')
# 				except RBTree.NotFound as e:
# 					print('NotFound')
# 			else:
# 				print("illegal input line: ", l)
# 	f.close()

# if __name__ == "__main__":
# 	main()