from sys import argv
from redBlackTree import *

# creates a Map ADT from a red black tree
class Map:

	# raises an exception in the case of a key already existing
	class ExistingKey(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	# raises an exception in the case of a node not existing with the requested key
	class NoKey(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	# constructor for the Map ADT
	def __init__(self):
		self.rbt = RBTree()

	# inserts a node into the map by inserting it into the red black tree with the provided key
	def insert(self, key, value) -> None:
		node = RBNode(key, self.rbt.nil, value)
		self.rbt.insert(node)

	# reassigns a new value to the provided key
	def reassign(self, key, value) -> None:
		try:
			node = self.rbt.search(self.rbt.root, key)
		except RBTree.NotFound as e:
			raise Map.NoKey('reassign({}) did not find the node'.format(key))
		node.other = value

	# removes a node from the map and red black tree
	def remove(self, key) -> None:
		node = self.rbt.search(self.rbt.root, key)
		self.rbt.remove(node)

	# boolean that returns whether or not the node exists
	def lookup(self, key) -> bool:
		try:
			node = self.rbt.search(self.rbt.root, key)
		except RBTree.NotFound as e:
			return False
		return True

	# returns the value of the node with the provided key
	def fetch(self, key) -> str:
		try:
			node = self.rbt.search(self.rbt.root, key)
		except RBTree.NotFound as e:
			raise Map.NoKey('fetch({}) did not find the node'.format(key))
		return node.other

	# converts a provided string into a usable key
	def stringToKey(self, value) -> int:
		s = 0
		for i in range(len(value)):
			s = s + ord(value[i])
		return s

# a main function that takes in an input file and runs the program as requested
def main():
	f = open(argv[1], "r")
	inData = f.readline().strip().split()
	numIn = int(inData[0])
	numOut = int(inData[1])
	if numIn < numOut:
		print("NO\n")
		return
	itWorks = True
	map = Map()
	inData = f.readline().strip().split()
	for i in range(numIn):
		try:
			value = inData[i]
			map.insert(map.stringToKey(value), value)
		except Map.ExistingKey as e:
			map.reassign(map.stringToKey(value), value)
	inData = f.readline().strip().split()
	for i in range(numOut):
		value = inData[i]
		testVar = map.lookup(map.stringToKey(value))
		if testVar == False:
			itWorks = False
		else:
			map.remove(map.stringToKey(value))
	if itWorks:
		print("YES\n")
	else:
		print("NO\n")
	f.close()

# this code works with either python or python3
if __name__ == "__main__":
	main()