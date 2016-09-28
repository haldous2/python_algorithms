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
        max = len(self.data) - 1
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
        # base case min <= max
        if min > max:
            return
        # recurse - narrow down
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

def binarySearch(arr=[], min=None, max=None, find=0):
    """
     Find the first occurance of a value in an array
    """

    if min == None:
        min = 0
    if max == None:
        max = len(arr) - 1

    while min <= max:

        print "min:{} max:{}".format(min, max)
        mid = (min + max) / 2
        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            min = mid + 1
        else:
            max = mid - 1

    return None

def binarySearch_first(arr=[], find=0):
    """
     Find the first occurance of a value in an array
    """
    min = 0
    max = len(arr) - 1
    result = None
    while min <= max:
        mid = (min + max) / 2
        if arr[mid] == find:
            result = mid
            max = mid - 1 # look left for first occurence
        elif arr[mid] < find:
            min = mid + 1
        else:
            max = mid - 1
    return result

def binarySearch_last(arr=[], find=0):
    """
     Find the last occurance of a value in an array
    """
    min = 0
    max = len(arr) - 1
    result = None
    while min <= max:
        mid = (min + max) / 2
        if arr[mid] == find:
            result = mid
            min = mid + 1 # look right for last occurence
        elif arr[mid] < find:
            min = mid + 1
        else:
            max = mid - 1
    return result

def numberOfOccurences(arr=[], find=0):
    """
    How many occurances of a value are in a dataset of integers
    Overall runtime is still O(log n), pretty cool!
    Considering a linear search would be O(n)
     0 1 2 3 4 5 6 7 8 9
    [1,2,5,5,5,5,5,6,7,8]
     5 5's from idx 2 to 6 - max - min + 1
    """
    idxMin = binarySearch_first(arr, find)
    idxMax = binarySearch_last(arr, find)
    if idxMin is not None and idxMax is not None:
        print "number of occurences of {} is {}".format(find, idxMax - idxMin + 1)
    else:
        print "didn't find any occurences of {}".format(find)

def sortedAndRotated(arr=[]):
    """
     How many times is a sorted array with no duplicates rotated ?
     e.g. [8,9,1,2,3,4,5,6,7] <- 2 times in this case. find min, index is the number of times
    """
    min = 0
    max = len(arr) - 1
    n = len(arr)

    while min <= max:

        mid = min + (max - min) / 2

        """
         check to see if we are already sorted
          0 1 2 3 4 5 6 7
         [8,9,1,2,3,4,5,6]
          L     M       H ... M <= H, H = M-1 (looking left, right sorted)
          L M H           ... M >= L, L = M+1 (looking right, left sorted)
              X           ... M=L=H - only one option! L <= H - found minimum!
        """
        if arr[min] <= arr[max]:
            #print "returning min:{} because {} <= {}".format(min, arr[min], arr[max])
            return min # rotated @ index min times

        # check to see if min found at mid - the end goal, base case
        # min @ mid will be <= next and <= previous

        next = (mid + 1) % n
        prev = (mid - 1) % n

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            #print "returning pivot mid:{}={} <= next:{}={} && prev:{}={}".format(mid, arr[mid], next, arr[next], prev, arr[prev])
            return mid # rotated index @ mid times

        # Still looking? check if mid is less than max
        # if so, right is sorted, move max back and keep looking
        if arr[mid] <= arr[max]:
            max = mid - 1

        # Still looking ? check if mid is >= min
        # if so, left is sorted, move min up and keep looking
        if arr[mid] >= arr[min]:
            min = mid + 1

lstTest = [0,2,5,7,9,13,27,30,33,35,38,39,41,45,47,48,49,53,55]
lstTest = [0,2,100]
lstTest = range(42)

#print lstTest
#bs = binarySearch(lstTest)
#print "Result find iterative 32:{}".format(bs.search_iterative(32))
#print "Result find recursive 32:{}".format(bs.search_recursive(32))

#lstTest = [1,2,3,4,5,5,5,5,5,6,7,8,9]
#print lstTest
#numberOfOccurences(lstTest, 5)

lstTest = [8,9,1,2,3,4,5,6]
#lstTest = [1,2,3,4,5,6,7,8,9]
print sortedAndRotated(lstTest)

# find value in sorted and rotated dataset
idxPivot = sortedAndRotated(lstTest)
srcValue = 7

print "idxPivot:{} srcValue:{} lstTest[{}]:{}".format(idxPivot, srcValue, idxPivot, lstTest[idxPivot])
if lstTest[idxPivot] == srcValue:
    print "found value at the pivot!"
else:
    fndValue = binarySearch(lstTest, 0, idxPivot - 1, srcValue)
    if fndValue is None:
        fndValue = binarySearch(lstTest, idxPivot, None, srcValue)
        if fndValue is None:
            print "did not find value"
        else:
            print "found value in right half!"
    else:
        print "found value in left half!"
