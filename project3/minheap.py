# Min Heap code provided by Joe Sventek

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
		if left <= self.bhsize and self.array[left] < self.array[smallest]:
			smallest = left
		if right <= self.bhsize and self.array[right] < self.array[smallest]:
			smallest = right
		if smallest is not i:
			x = self.array[i]
			self.array[i] = self.array[smallest]
			self.array[smallest] = x
			self.siftDown(smallest)

# sifts up from the new node making sure the new branch fits into the heap principles
	def siftUp(self, i: int) -> None:
		parent = i // 2
		while i > 1 and self.array[parent] > self.array[i]:
			x = self.array[parent]
			self.array[parent] = self.array[i]
			self.array[i] = x
			i = parent
			parent = i // 2

# adds a new node onto the heap
	def insert(self, x: int) -> None:
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
	def remove(self) -> int:
		if self.bhsize is 0:
			raise MinHeap.Underflow("remove() called on empty heap")
		minimum = self.array[1]
		self.array[1] = self.array[self.bhsize]
		self.bhsize -= 1
		self.siftDown(1)
		return minimum

# returns the value of the root without removing it
	def look(self) -> int:
		if self.bhsize is 0:
			raise MinHeap.Underflow("look() called on empty heap")
		return self.array[1]

# returns the size of the heap
	def size(self) -> int:
		return self.bhsize

# returns if the heap is empty
	def isEmpty(self) -> bool:
		if self.bhsize is 0:
			return True
		else:
			return False

# returns the contents of the heap as a string
	def toString(self) -> str:
		if self.bhsize is 0:
			result = "Empty"
		else:
			l = []
			for i in range(1, self.bhsize+1):
				l.append(str(self.array[i]))
			result = ' '.join(l)
		return result