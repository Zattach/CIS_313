import sys

# creates a Hashtable class to store my data in the form of a hash table
class Hashtable:

# initializes the hashtable
    def __init__(self, x):
        self.size = x + 1
        self.lock = [None] * self.size

# adds data to the hashtable through the hash functioon
    def put(self, word):
        key = self.stringToKey(word)
        key = self.function(key)
        while self.lock[key] != None:
            key = self.rehash(key)
        self.lock[key] = word

# finds the data in the hash function by finding the key through the hash function
    def get(self, word):
        start = self.stringToKey(word)
        key = self.function(start)
        data = None
        stop = False
        while self.lock[key] != None and not stop:
            if self.lock[key] == word:
                data = self.lock[key]
                self.lock[key] = None
                stop = True
            else:
                key = self.rehash(key)
                if key == start:
                    stop = True
        return data

# converts a string into a usable key through the sum method
    def stringToKey(self, word):
        s = 0
        for i in range(0, len(word)):
            s = s + ord(word[i])
        return s

# a very basic hash function that simply takes the remainder of the key / size
    def function(self, key):
        return key % self.size

# produces a new key when there is already data stored at the key
    def rehash(self, key):
        return (key + 1) % self.size

# a driver that will take in the file and read the inputs. This driver returns
# if the information works or not
def driver():
    with open(sys.argv[1]) as f:
        in_data = f.readline().strip().split()
        numIn = int(in_data[0])
        numOut = int(in_data[1])
        itWorks = True
        h = Hashtable(numIn)
        in_data = f.readline().strip().split()
        for x in range(0, numIn):
            h.put(in_data[x])
        in_data = f.readline().strip().split()
        for x in range(0, numOut):
            testVar = h.get(in_data[x])
            if testVar == None:
                itWorks = False
        if itWorks:
            print("YES\n")
        else:
            print("NO\n")

# this code should work with either python or python3
if __name__ == "__main__":
    driver()
