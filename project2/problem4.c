#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int getParent(i){
	return i / 2;
}

int getLeft(i){
	return 2 * i;
}

int getRight(i){
	return (2 * i) + 1;
}

 void minHeapify(int heap, int heap_size, int i){
 	int l = getLeft(i);
 	int r = getRight(i);
 	int smallest = i;
 	if((l <= heap_size) && (heap[l] < heap[i])){
 		smallest = l;
 	} 
 	if((r <= heap_size) && (heap[r] < heap[i])){
		smallest = r;
	}
	if(smallest != i){
		int var = heap[i];
		heap[i] = heap[smallest];
		heap[smallest] = var;
		minHeapify(heap, heap_size, smallest)
	} 
 }

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
			raise Heap.Underflow("HeapError")
		if self.size == 1:
			self.size = 0
			return self.array[0]
		min = self.array[0]
		self.array = self.array[self.size - 1]
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
		string = ' '.join(str(x) for x in range(0, self.size))
		return string

// main function that will read in file and call solve
int main( int argc, const char* argv[] ){
    if( argc != 2 ) { 
        //checks for the input file name
        printf( "error; no input file name\n" );
        return 1;
    }

    // saves the input file and creates an array titled maze
    FILE *filePointer;
    filePointer = fopen( argv[1], "r" );

    int n;
    fscanf( filePointer, "%d\n", &n);
    int *heap = (int *)malloc(n * sizeof(int));
    int heap_size = 0;

    for(int i = 0; i < n; i++){
    	char action[10];
    	int num;
    	fscanf("%s %d\n", action, num);

    	switch(action){
    		case "insert":
    			insert(heap, heap_size, x);
    			break;
    		case "remove":
    			remove(heap, heap_size);
    			break;
    		case "print":
    			if(is_empty(heap)){
    				printf("Empty");
    			} else {
    				printf("%s\n", to_string(heap, heap_size));
    			}
    		case "size":
    			printf("%d\n", heap_size);
    		case "best":
    			if(is_empty(heap)){
    				printf("HeapError\n");
    			} else {
    				printf("%d\n", look(heap));
    			}
    	}
    }
}