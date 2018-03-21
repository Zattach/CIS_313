import sys
from minheap import *
from maxheap import *

def driver():
	with open(sys.argv[1]) as f:
		n = int(f.readline().strip())
		min = MinHeap()				# creates a minheap and a maxheap to store both sets of data 
		max = MaxHeap()
		median = 0
		for _ in range(n):
			value = int(f.readline())
			if value < median:		# determines which heap to send the data to
				max.insert(value)
			else:
				min.insert(value)
			if min.size() is max.size():		# if heaps are even we take the average of their roots
				median = (min.look() + max.look()) / 2
			elif min.size() > max.size():
				if min.size() > (max.size() + 1):		# rearranges heaps if min is too big
					max.insert(min.remove())			# then returns the average
					median = (min.look() + max.look()) / 2
				else:
					median = min.look()					# returns the root of min if min > max
			else:
				if max.size() > (min.size() + 1):		# rearranges heaps if max is too big
					min.insert(max.remove())			# then returns the average
					median = (min.look() + max.look()) / 2
				else:
					median = max.look()					# returns the root of max if min < max
			print(median)

if __name__ == "__main__":
	driver()
