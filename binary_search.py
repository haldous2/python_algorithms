#!/usr/local/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

import resource

# Print necessary headers.
print "Content-Type: text/html\n\n"

print "Memory MB:{:4d}<br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

class binarySearch(object):

    """
    Binary Search Class

    Assume: input is list it's in order and has some data.
    
    split ordered array of integers into 2 parts (binary) until value found
    O(log n)time, 0(1)space

    PseudoCode:
    1. Let min = 0 and max = n-1.
    2. Compute pivot as the average of max and min, rounded down (so that it is an integer).
       don't forget to add min!
    3. If array[pivot] equals target, then stop. You found it! Return pivot.
    4. If
       value too hi, min = pivot + 1.
       value too lo, max = pivot - 1.
       Go back to step 2.

    """
    def __init__(self, data=[]):
        """
        Return a binary search object
        """
        self.data = data
        self.count = 0
        self.value = ''

    def initSearch(self, value=0):
        self.value = value
        if self.data:
            min = 0
            max = len(self.data) - 1
        return self.search(min, max)

    def search(self, min, max):
        """
        Search data - true if found else false
        find the mid point of min and max
        """

        #print "min: %d(%s) max: %d(%s) <br/>\n" % (min, self.data[min], max, self.data[max])

        if max - min > 1:
            pivot = int((max - min) / 2) + min
            # Got lucky - the pivot is the value
            if self.value == self.data[pivot]:
                #print '3.returning True...'
                print "Done (3) Memory MB:{:4d} <br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
                return True
            # Set new min and max if not found yet
            if self.value < self.data[pivot]:
                return self.search(min, pivot - 1)
            else:
                return self.search(pivot + 1, max)
        elif max - min == 1:
            # Only two elements in the array, any a match ?
            if self.data[min] == self.value or self.data[max] == self.value:
                #print '2.returning True...'
                print "Done (2) Memory MB:{:4d} <br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
                return True
            else:
                #print '2.returning False...'
                return False
        elif max - min == 0:
            # Only one element in the array, is it a match ?
            if self.data[min] == self.value:
                #print '1.returning True...'
                print "Done (1) Memory MB:{:4d} <br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
                return True
            else:
                #print '1.returning False...'
                return False
        else:
            return False


lstTest = [0,2,5,7,9,13,27,30,33,35,38,39,41,45,47,48,49,53,55]
lstTest = [0,2,100]
lstTest = range(99)

bs = binarySearch(lstTest)
print "Data Init Memory MB:{:4d}<br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
print "Result find 32:{}".format(bs.initSearch(32))
#print bs.initSearch(35)
