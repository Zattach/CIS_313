import sys

class Heap:

	class Underflow(Exception):
		def __init__(self, data=None):
			super().__init__(data)

	def __init__(self, len):
		self.array = list([0] * len)
		self.size = 0

	def parent(self, i):
		return i // 2

	def left(self, i):
		return (2 * i)

	def right(self, i):
		return ((2 * i) + 1)

	def minHeapify(self, i):
		l = self.left(i)
		r = self.right(i)
		smallest = i
		if (l <= self.size) & (self.array[l] < self.array[i]):
			smallest = l
		if (r <= self.size) & (self.array[r] < self.array[smallest]):
			smallest = r
		if smallest != i:
			var = self.array[i]
			self.array[i] = self.array[smallest]
			self.array[smallest] = var
			self.minHeapify(smallest)

# there is an issue with my insert that will not compare the current with the parent
	def insert(self, x):
		i = self.size
		self.size += 1
		self.array[i] = x
		while (i != 0) & (self.array[self.parent(i)] < self.array[i]):
			var = self.array[i]
			self.array[i] = self.array[self.parent(i)]
			self.array[self.parent(i)] = var
			i = self.parent(i)

	def remove(self):
		if self.size <= 0:
			print("HeapError")
			return
		if self.size is 1:
			self.size = 0
			return self.array[0]
		min = self.array[0]
		self.array[0] = self.array[self.size - 1]
		self.size -= 1
		self.minHeapify(0)
		return min

	def look(self):
		return self.array[0]

	def size(self):
		return self.size

	def is_empty(self):
		if self.size == 0:
			return True
		return False

	def to_string(self) -> str:
		print(self.array)
		return

# main function that will read in file and call solve
def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        h = Heap(n)
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "insert":
                value = int(value_option[0])
                h.insert(value)
            elif action == "remove":
            	h.remove()
            elif action == "print":
            	if h.is_empty():
            		print("Empty")
            	else:
            		h.to_string()
            elif action == "size":
            	print(h.size)
            elif action == "best":
            	if h.is_empty():
            		print("HeapError")
            	else:
            		print(h.look())

# this code should work with either python or python3
if __name__ == "__main__":
    driver()

