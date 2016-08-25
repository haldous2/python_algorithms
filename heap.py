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

Example: Max Heap                 40
                              35      38
                            33  31  28  22
                          27  --

        As Array:         0 40 35 38 33 31 28 22 27 --
                          0 40 35 38 33 31 28

         Min Heap                 22
                              28      27
                            31  33  35  38
                         40 --

        As Array:        0 22 28 27 31 33 35 38 40 --
"""

class maxHeap(object):

    def __init__(self, data):
        self.data = data

    def viewData(self):
        return self.data

    def peek(self):
        # just peeking! - nothing removed
        if len(self.data) > 1:
            return self.data[1]
        else:
            return False

    def pop(self):

        # pop - remove, return and reorganize
        # swap top and bottom values
        # bubble down top swapping with largest child node, if child node is larger than parent

        # store value of max for return
        i_val = self.peek()

        # swap first and last element
        self.__swap(1, len(self.data) - 1)

        # remove last
        self.data.pop()

        # bubble down max to it's new home
        #self.__bubbleDown(1)
        self.__rBubbleDown(1)

        return i_val

    def push(self, v):
        # insert at the end, regorganize
        self.data.append(v)
        i = len(self.data) - 1
        self.__floatUp(i)

    def initData(self):
        # organize data into high to low
        heap = []
        for i in self.data:
            heap.append(i)
            self.__floatUp(len(heap) - 1)
        self.data = heap

    def __swap(self, i, j):
        if i == j:
            return
        if len(self.data) <= 1:
            return
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def __floatUp(self, i):

        # iterative float up
        # i is child index, not value

        parent = i / 2 // 1 # floor of i/2

        #print "parent [{}]:{} i [{}]:{}".format(parent, self.data[parent], i, self.data[i])

        while True:
            print "parent [{}]:{} i [{}]:{}".format(parent, self.data[parent], i, self.data[i])
            if parent <= 0:
                break
            if self.data[parent] > self.data[i]:
                break
            self.__swap(i, parent)
            i = parent
            parent = i / 2 // 1

    def __rFloatUp(self, i):

        # recursive float up
        # i is child index, not value

        parent = i / 2 // 1 # floor of i/2

        if parent <= 0:
            return
        if self.data[parent] > self.data[i]:
            return
        self.__swap(i, parent)
        i = parent
        self.__rFloatUp(i)

    def __bubbleDown(self, i):

        # bubble down when largest child is more than parent i
        # i is parent index, not value

        data_len = len(self.data) - 1

        if data_len < 2:
            return

        if data_len == 2:

            child_left = i * 2

            if self.data[child_left] > self.data[i]:
                self.__swap(i, child_left)

        else:

            child_left = i * 2
            child_right = i * 2 + 1

            #while self.data[i] < (self.data[child_left] or self.data[child_right]):
            while True:

                if child_left <= data_len:
                    if child_right <= data_len:
                        # both within bounds
                        if self.data[child_left] > self.data[child_right]:
                            self.__swap(i, child_left)
                            i = child_left
                        else:
                            self.__swap(i, child_right)
                            i = child_right
                    else:
                        # only left in bounds
                        self.__swap(i, child_left)
                        i = child_left
                else:
                    # neither one in bounds
                    break

                child_left = i * 2
                child_right = i * 2 + 1

                if (child_left or child_right) >= data_len:
                    break

    def __rBubbleDown(self, i):

        # bubble down when largest child is more than parent i
        # i is parent index, not value

        data_len = len(self.data) - 1

        if data_len < 2:
            return

        if data_len == 2:

            child_left = i * 2

            if self.data[child_left] > self.data[i]:
                self.__swap(i, child_left)

        else:

            child_left = i * 2
            child_right = i * 2 + 1

            if child_left <= data_len:
                if child_right <= data_len:
                    # both within bounds
                    if self.data[child_left] > self.data[child_right]:
                        self.__swap(i, child_left)
                        i = child_left
                    else:
                        self.__swap(i, child_right)
                        i = child_right
                else:
                    # only left in bounds
                    self.__swap(i, child_left)
                    i = child_left
            else:
                # neither one in bounds
                return

            self.__rBubbleDown(i)

maxData = [0,40,35,38,33,31,28,22,27,5]
maxData = [0,40,35,38,33,31,28,22,27,5]
#maxData = [0]
#maxData = [0,40]
#maxData = [0,40,38,35]
#maxData = [0,40,35,38]
#maxData = [0,40,35,38,33]

minData = [0,22,28,27,31,33,35,38,40]

theMaxHeap = maxHeap(maxData)
print theMaxHeap.viewData()

#print theMaxHeap.peek()
#theMaxHeap.push(50)
#print "peek:{}".format(theMaxHeap.peek())
print theMaxHeap.pop()
#theMaxHeap.initData()

print theMaxHeap.viewData()
