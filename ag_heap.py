"""
Heaps - min & max

Methods:
peek - return top (max or min)
pop  - remove top (max or min) and reorganize
push - add value to heap and fload value up until it fits

Note: Tree vs min or max Heap
      Tree is ordered and best for searching @ O(logN) time. Insert time O(logN)
      A Heap is best for finding the min and max value @ O(1)time. Insert time O(logN)

Note: heaps can be defined as arrays - since everything is binary split we can devise
      formulas to find parents and children

      parent   = floor(i/2)
      children = (i * 2), (i * 2) + 1
      max      = heap[1]

Example: Max Heap                 40                   1
                              35      38           2       3
                            33  31  28  22       4   5   6   7
                          27  --

        As Array:         0 40 35 38 33 31 28 22 27 --
                          0 40 35 38 33 31 28

         Min Heap                 22
                              28      27
                            31  33  35  38
                         40 --

        As Array:        0 22 28 27 31 33 35 38 40 --
"""

class maxHeap:

    """
    Max Heap
    note: index starts at 1, need to skip 0 since siblings calculated from index
    """

    def __init__(self):
        self.h = [-9999]

    def peek(self):
        if len(self.h) > 1:
            return self.h[1]
        else:
            return None

    def pop(self):
        if len(self.h) > 1:
            self.h[1] = self.h[-1]
            self.h.pop()
            self.bubble_down(1)

    def push(self, value):
        """
        insert value at end of array (list)
        """
        self.h.append(value)
        self.float_up(len(self.h) - 1)

    def heapify(self, l):
        """
        heapify incoming list l
        """
        if not l:
            return
        self.h = [-9999]
        for i in xrange(0, len(l)):
            self.push(l[i])

    def float_up(self, index=1):
        """
        float value at index up while smaller than parent
        note: to keep 0th index clear, p > 0
        """

        i = index
        p = index // 2

        while self.h[i] > self.h[p] and p > 0:
            self.h[p], self.h[i] = self.h[i], self.h[p]
            i = p
            p = i // 2

    def bubble_down(self, index):

        h_len = len(self.h) - 1

        i = index

        while True:

            child_left = i * 2
            child_right = i * 2 + 1

            if child_left <= h_len:
                if child_right <= h_len:
                    # both within bounds
                    if self.h[child_left] > self.h[child_right]:
                        if self.h[child_left] > self.h[i]:
                            self.h[i], self.h[child_left] = self.h[child_left], self.h[i]
                            i = child_left
                        else:
                            return
                    else:
                        if self.h[child_right] > self.h[i]:
                            self.h[i], self.h[child_right] = self.h[child_right], self.h[i]
                            i = child_right
                        else:
                            return
                else:
                    # only left in bounds
                    if self.h[child_left] > self.h[i]:
                        self.h[i], self.h[child_left] = self.h[child_left], self.h[i]
                        i = child_left
                    else:
                        return
            else:
                # neither one in bounds
                return

maxData = [0,40,35,38,33,31,28,22,27,5]
maxData = [0,40,35,38,33,31,28,22,27,5]
#maxData = [0]
#maxData = [0,40]
#maxData = [0,40,38,35]
#maxData = [0,40,35,38]
#maxData = [0,40,35,38,33]

theMaxHeap = maxHeap()
theMaxHeap.heapify(maxData)
print theMaxHeap.h

#print theMaxHeap.peek()
#theMaxHeap.push(50)
#print "peek:{}".format(theMaxHeap.peek())
#print theMaxHeap.pop()

print theMaxHeap.h

class minHeap:

    """
    Min Heap
    note: index starts at 1, need to skip 0 since siblings calculated from index
    """

    def __init__(self):
        self.h = [-9999]

    def peek(self):
        if len(self.h) > 1:
            return self.h[1]
        else:
            return None

    def pop(self):
        if len(self.h) > 1:
            self.h[1] = self.h[-1]
            self.h.pop()
            self.bubble_down(1)

    def push(self, value):
        """
        insert value at end of array (list)
        """
        self.h.append(value)
        self.float_up(len(self.h) - 1)

    def heapify(self, l):
        """
        heapify incoming list l
        """
        if not l:
            return
        self.h = [-9999]
        for i in xrange(0, len(l)):
            self.push(l[i])

    def float_up(self, index=1):
        """
        float value at index up while smaller than parent
        note: to keep 0th index clear, p > 0
        """
        i = index
        p = index // 2

        while self.h[i] < self.h[p] and p > 0:
            self.h[p], self.h[i] = self.h[i], self.h[p]
            i = p
            p = i // 2

    def bubble_down(self, index=1):

        h_len = len(self.h) - 1

        i = index

        while True:

            child_left = i * 2
            child_right = i * 2 + 1

            if child_left <= h_len:
                if child_right <= h_len:
                    # both within bounds
                    if self.h[child_left] < self.h[child_right]:
                        if self.h[child_left] < self.h[i]:
                            #print "swap left with parent...", self.h[child_left], self.h[i]
                            self.h[i], self.h[child_left] = self.h[child_left], self.h[i]
                            i = child_left
                        else:
                            return
                    else:
                        if self.h[child_right] < self.h[i]:
                            #print "swap right with parent...", self.h[child_right], self.h[i]
                            self.h[i], self.h[child_right] = self.h[child_right], self.h[i]
                            i = child_right
                        else:
                            return
                else:
                    # only left in bounds
                    if self.h[child_left] < self.h[i]:
                        #print "swap left with parent...", self.h[child_left], self.h[i]
                        self.h[i], self.h[child_left] = self.h[child_left], self.h[i]
                        i = child_left
                    else:
                        return
            else:
                # neither one in bounds
                return

minData = [0,22,28,27,33,38,40,31,35] # sorted
#minData = [0,33,22,40,28,38,27,31,35] # scrambled eggs

theMinHeap = minHeap()
theMinHeap.heapify(minData)
print "min data - start:{}".format(theMinHeap.h)

#print "min data - sorted:{}".format(theMinHeap.h)
#print "min:{}".format(theMinHeap.pop())
print "adding 50"
theMinHeap.push(50)
print "adding 18"
theMinHeap.push(18)
print "min data - end:{}".format(theMinHeap.h)
