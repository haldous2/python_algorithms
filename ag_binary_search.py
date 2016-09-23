#!/usr/local/bin/python

class binarySearch(object):

    """
    Binary Search Class

    Assume: input is list it's in order and has some data.

    split ordered array of integers into 2 parts (binary) until value found
    O(log n)time, 0(1)space

    PseudoCode:
    1. Let min = 0 and max = n-1.
    2. Compute mid as the average of max and min
    3. If array[mid] equals target, then stop. You found it! Return pivot.
    4. If
       value too hi, min = mid + 1.
       value too lo, max = mid - 1.
       repeat - step 2 while lo <= hi

    """

    def __init__(self, data=[]):
        """
        Return a binary search object
        """
        self.data = data
        self.count = 0
        self.value = ''

    def search_iterative(self, find):
        min = 0
        max = len(self.data)
        while min <= max:
            mid = (min + max) / 2
            if self.data[mid] == find:
                return True
            elif self.data[mid] < find:
                min = mid + 1
            else:
                max = mid - 1
        return False

    def search_recursive(self, value=0):
        self.value = value
        if self.data:
            min = 0
            max = len(self.data) - 1
        return self.search_recursive_worker(min, max)

    def search_recursive_worker(self, min, max):
        # base case
        if min > max:
            return
        # recurse
        mid = (min + max) / 2
        if self.data[mid] == self.value:
            return True
        elif self.data[mid] < self.value:
            min = mid + 1
            return self.search_recursive_worker(min, max)
        elif self.data[mid] > self.value:
            max = mid - 1
            return self.search_recursive_worker(min, max)
        else:
            return False


lstTest = [0,2,5,7,9,13,27,30,33,35,38,39,41,45,47,48,49,53,55]
lstTest = [0,2,100]
lstTest = range(99)

bs = binarySearch(lstTest)
print "Result find iterative 32:{}".format(bs.search_iterative(32))
print "Result find recursive 32:{}".format(bs.search_recursive(32))
#print bs.initSearch(35)
