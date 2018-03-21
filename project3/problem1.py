import sys

# node class creates a node containing an ip address and a priority
class Node:
	def __init__(self, ip, priority):
		self.ip = ip
		self.priority = priority

# Min Heap code provided by Joe Sventek but is modified to hold a node instead of an int
class MinHeap:
	class Underflow(Exception):
		def __init__(self, data=None):
			super().__init__(data)

# initializes the heap
	def __init__(self, array=None):
		if array is None:
			self.bhsize = 0
			self.length = 1025
			self.array = [None] * self.length
		else:
			self.length = len(array) + 1
			self.array = [None] * self.length
			for i in range (len(array)):
				self.array[i+1] = array[i]
			self.bhsize = self.length - 1
			i = self.length // 2
			while i > 0:
				self.siftDown(i)
				i -= 1

# sifts down from the root making the heap follow the heap principles
	def siftDown(self, i: int) -> None:
		left = 2 * i
		right = left + 1
		smallest = i
		if left <= self.bhsize and self.array[left].priority < self.array[smallest].priority:
			smallest = left
		if right <= self.bhsize and self.array[right].priority < self.array[smallest].priority:
			smallest = right
		if smallest is not i:
			x = self.array[i]
			self.array[i] = self.array[smallest]
			self.array[smallest] = x
			self.siftDown(smallest)

# sifts up from the new node making sure the new branch fits into the heap principles
	def siftUp(self, i: int) -> None:
		parent = i // 2
		while i > 1 and self.array[parent].priority > self.array[i].priority:
			x = self.array[parent]
			self.array[i] = x
			i = parent
			parent = i // 2

# adds a new node onto the heap
	def insert(self, x: "comparable") -> None:
		if self.bhsize >= self.length - 1:
			nlength = 2 * self.length
			narray = [None] * nlength
			for i in range(1, self.bhsize+1):
				narray[i] = self.array[i]
			self.length = nlength
			self.array = narray
		self.bhsize += 1
		self.array[self.bhsize] = x
		self.siftUp(self.bhsize)

# removes the root off of the heap and re-heapifies the heap
	def remove(self) -> "comparable":
		if self.bhsize is 0:
			raise MinHeap.Underflow("remove() called on empty heap")
		minimum = self.array[1]
		self.array[1] = self.array[self.bhsize]
		self.bhsize -= 1
		self.siftDown(1)
		return minimum

# returns the value of the root without removing it
	def look(self) -> "comparable":
		if self.bhsize is 0:
			raise MinHeap.Underflow("look() called on empty heap")
		return self.array[1]

# returns the size of the heap
	def size(self) -> int:
		return self.bhsize

# returns the size of the heap
	def isEmpty(self) -> bool:
		if self.bhsize is 0:
			return True
		else:
			return False

def driver():
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		listA = []	# creates lists to store the data to be heapified later on
		listB = []
		for _ in range(n):
			in_data = f.readline().strip().split()
			ip, tier, priority = in_data[0], in_data[1], in_data[2]
			node = Node(ip, int(priority) + _)
			if tier is 'A':
				listA.append(node)	# decides which list to store the node in
			elif tier is 'B':
				listB.append(node)
			else:
				print("Invalid Tier Entered")
		heapA = MinHeap(listA)	# heapifies both lists 
		heapB = MinHeap(listB)
		while not heapA.isEmpty():
			node = heapA.remove()	# removes all elements from heapA and then heapB
			print(node.ip)
		while not heapB.isEmpty():
			node = heapB.remove()
			print(node.ip)

if __name__ == "__main__":
	driver()
