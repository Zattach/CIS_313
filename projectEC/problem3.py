from sys import argv
from redBlackTree import *

class TFTree:
	class EmptyTree(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	class NotFound(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	def __init__(self):
		self.rbt = RBTree()
		self.root = RBTree()

	def insert(self, key):
		self.rbt.insert(key)

	def search(self, key):
		z = self.rbt.searchIterative(self.rbt.root, key)
		if z == self.rbt.nil:
			raise TFTree.NotFound('search({}) not found'.format(key))
		return z

	def to_list_inorder(self) -> "list of keys":
		l = []
		self.rbt.inOrderHelper(self.rbt.root, l)
		if len(l) == 0:
			raise TFTree.EmptyTree('to_list_inorder() called on empty tree')
		return l

	def height(self) -> int:
		x = self.rbt.root
		if x == self.rbt.nil:
			raise TFTree.EmptyTree('height() invoked on empty tree')
		count = 0
		while x.left != self.rbt.nil:
			x = x.left
			count += 1
		return count + 1

	def root_key(self) -> str:
		if self.rbt.root == self.rbt.nil:
			raise TFTree.EmptyTree('root_key() called on empty tree')
		l = []
		if self.rbt.root.right != self.rbt.nil and self.rbt.root.right.color == Color.BLACK:
			l.append(self.rbt.root.right.key)
		l.append(self.rbt.root.key)
		if self.rbt.root.left != self.rbt.nil and self.rbt.root.left.color == Color.BLACK:
			l.append(self.rbt.root.left.key)
		strings = [str(x) for x in l]
		roots = ' '.join(strings)
		return roots
	
def main() -> None:
	st = TFTree()
	f = open(argv[1], "r")
	nl = int(f.readline().strip())
	for i in range(nl):
		l = f.readline().strip()
		if l == 'inprint':
			try:
				keys = st.to_list_inorder()
				strings = [str(x) for x in keys]
				print(' '.join(strings))
			except TFTree.EmptyTree as e:
				print('Empty')
		elif l == 'height':
			try:
				height = st.height()
				print(height)
			except TFTree.EmptyTree as e:
				print('0')
		elif l == 'root':
			try:
				roots = st.root_key()
				print(roots)
			except TFTree.EmptyTree as e:
				print('Empty')
		else:
			v = l.split()
			if v[0] == 'insert':
				k = int(v[1])
				z = RBNode(k, st.rbt.nil)
				st.insert(z)
			elif v[0] == 'search':
				k = int(v[1])
				try:
					z = st.search(k)
					print('Found')
				except TFTree.NotFound as e:
					print('NotFound')
			else:
				print("illegal input line: ", l)
	f.close()

if __name__ == "__main__":
	main()