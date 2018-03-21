
# List class
class List:

	# List constructor
	def __init__(self):
		self.head = None
		self.tail = None
		return

	# add method, adds a node onto the list
	def add(self, newData):
		temp = Node(newData)
		temp.setNext(self.head)
		if self.list_empty():
			self.tail = temp
		else:
			self.head.setPrev(temp)
		self.head = temp
		return

	# remove mthod, removes a node from the list depending on whether it's tail or head
	def rem(self, tail_bool):
		if not tail_bool:
			var = self.head.getData()
			self.head = self.head.getNext()
		else:
			var = self.tail.getData()
			self.tail = self.tail.getPrev()
		return var

	#  empty method, returns if the list is empty or not
	def list_empty(self):
		if self.head == None:
			return True
		return False


# Node class
class Node:

	# Noce constructor
	def __init__(self, newData):
		self.data = newData
		self.next = None
		self.prev = None
		return

	# get Data method returns the data in the node
	def getData(self):
		return self.data

	# get next method returns the next node in the list
	def getNext(self):
		return self.next

	# get previous method returns the previous node in the list
	def getPrev(self):
		return self.prev

	# set next method, sets a node as the next node for the current node
	def setNext(self, newNode):
		self.next = newNode
		return

	# set previuos method, sets a node as the previous node for the current node
	def setPrev(self, newNode):
		self.prev = newNode
		return
		