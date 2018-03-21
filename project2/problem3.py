import sys

# implements a queue for the algorithm used to solve the problem
class Queue:

# raises the uunderflow exception if there is one. Should never be triggered here
	class Underflow(Exception):
		def __init__(self, data=None):
			super().__init__(data)

# allows for the creation of nodes in the queue with the proper data
	class Node:
		def __init__(self, give, spend):
			self.give = give
			self.spend = spend
			self.next = None

# initializes the queue
	def __init__(self):
		self.head = None
		self.tail = None

# adds a node onto the queue
	def enqueue(self, give, spend) -> None:
		n = self.Node(give, spend)
		if self.is_empty():
			self.head = n
		else:
			self.tail.next = n
		self.tail = n

# returns the first node of the queue and shortens the queue
	def dequeue(self) -> Node:
		if self.is_empty():
			raise Queue.Underflow("QueueError")
		n = self.head
		self.head = n.next
		if self.is_empty():
			self.tail = None
		return n

# returns if the queue is empty
	def is_empty(self) -> bool:
		if self.head == None:
			return True
		else:
			return False

# implements a Queue and my algorithm to solve the given problem. Runs O(n)
def solve(Q, length) -> int:
	complete = False
	s = 0
	while s < length:
		e = 0
		i = s
		while True:
			n = Q.dequeue()
			Q.enqueue(n.give, n.spend)
			e += n.give - n.spend
			i = (i + 1) % length
			if i == s:
				complete = True
				break
			if e < 0:
				s = i
				break
		if complete:
			return s
	return s



# main function that will read in file and call solve
def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        Q = Queue()
        for _ in range(n):
            in_data = f.readline().strip().split()
            give = int(in_data[0])
            spend = int(in_data[1])
            Q.enqueue(give, spend)
        correct = solve(Q, n)
        print(correct)

# this code should work with either python or python3
if __name__ == "__main__":
    driver()

