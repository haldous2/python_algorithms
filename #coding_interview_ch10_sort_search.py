"""
Cracking the coding interview
Practice questions
Part 10. Sorting & Searching
"""

import unittest

"""
Helper functions
"""
def binarySearch(arr=[], var=0, lo=0, hi=0):
    """
    binary search sorted array
    """
    if lo > hi:
        return False                            # base case - didn't find it!

    mid = (hi + lo) / 2                         # the binary part of binary search

    if var == arr[mid]:                         # base case - found it!
        return True

    if var < arr[mid]:
        return binarySearch(arr, var, lo, mid - 1)     # going left
    else:
        return binarySearch(arr, var, mid + 1, hi)     # going right

# testing binary search
#print binarySearch([1,2,3,4,5,6,7,8,9,10], 3, 0, 9)

"""
10.1

With two sorted arrays, merge sorted in fasted time possible
Note: first sorted array has extra blank space at end to accomodate the second array space
probably O(kn) - radix / bucket sort

Hints: start from end and work way to start

Initial thoughts (brute force approach - read through each array and compare ints, insert as we go)
If starting from end, can probably find biggest value and place at end of larger array and work to start

How to handle dups ?
"""

def sortMerge(arr01, arr02):
    """
    Iterative approach to combining two sorted arrays into one sorted array
    check if arr01 is larger by len(arr02) before proceeding
    """
    # base - need array 01, 02
    if not arr01 or not arr02:
        return []

    # base - array 02 can fit into array 01
    # [None,None...] == [None,None...]
    end_arr01 = arr01[(len(arr01) - len(arr02)):]
    end_arr02 = [None] * len(arr02)
    if end_arr01 != end_arr02:
        return []

    j = len(arr02) - 1                          # starting end of array 02
    k = len(arr01) - 1                          # next available spot
    s = len(arr01) - len(arr02) - 1             # start comparison index

    for i in range(len(arr_01) - 1, -1, -1):    # backwards through array 02
        if i <= s:                              # found the int end of arr01

            while arr01[i] < arr02[j] and j >= 0:
                arr01[k] = arr02[j]
                j -= 1
                k -= 1

            if i != k:
                arr01[k] = arr01[i]
                k -= 1

            if j < 0:
                break

    print "array 01:", arr01

# arr_01 = [1,3,5,7,9,13,15,20,None,None,None,None]
# arr_02 = [2,8,14,21]
# sortMerge(arr_01, arr_02)
#
# arr_01 = [1,3,5,7,9,13,15,20,None,None,None,None]
# arr_02 = [2,8,21,22]
# sortMerge(arr_01, arr_02)

"""
10.2

"""

def sortAnagram(anagram=[]):
    """
    sorting strings of anagrams
    place each anagram next to each other, not necessairly in order
    anagrams 'cat', 'tac' etc...
    """
    if not anagram:
        return []

    c_hash = {}
    o_anagrams = []

    for i, s in enumerate(anagram):         # each string

        c_count = 0

        for c in s:                         # each char in string
            c_count += ord(c)

        if c_count in c_hash:
            c_hash[c_count].append(i)       # [1,2,i] - add to list
        else:
            c_hash[c_count] = [i]           # [i] - start new list

    for h in c_hash:                        # all hashes with grouped string counts
        for i in c_hash[h]:                 # list of indexes

            # for now just creating a new list of anagrams
            o_anagrams.append(anagram[i])

    return o_anagrams

# arr_anagrams_t01 = ['cat','dog','hydroxydeoxycorticosterones','ant','god','nat','tac','antler','hydroxydesoxycorticosterone','learnt','rental']
# arr_anagrams_t02 = ['cat','dog','ant','god','nat','tac']
# print sortAnagram(arr_anagrams_t02)

# class sortAnagramTest(unittest.TestCase):
#
#     def setUp(self):
#         self.anagram = ['cat','dog','ant','god','nat','tac']
#         self.result = ['cat','tac','dog','god','ant','nat']
#
#     def test_sort_anagram(self):
#         self.assertEqual(sortAnagram(self.anagram), self.result)

"""
10.3

Search a rotated array of n integers. sorted in increasing order.

probably use binary search for a large array, could look for min element and then binary search
with start at index ?

[50....100, 1....49]
looking for 70, less than 100 - binary search 0 to index @ 100 etc...

"""

def rotatedSearch(arr=[], val=0):
    """
    search a rotated array
    need to look for min, track index - do comparison then binary search on correct half
    """
    if not arr:
        return False

    prev_i = None

    #for i,v in enumerate(arr):
    for i in range(0, len(arr)):
        if prev_i and arr[prev_i] > arr[i]:
            # stop, we found the min
            break
        prev_i = i

    if val > arr[0]:
        return binarySearch(arr, val, 0, prev_i)
    else:
        return binarySearch(arr, val, prev_i + 1, len(arr) - 1)

# arr_rotated_t01 = [15,16,19,20,25,1,3,4,5,7,10,14]
# arr_rotated_t02 = [15,16,19,20,25]
# print rotatedSearch(arr_rotated_t01, 20)

# class rotatedSearchTest(unittest.TestCase):
#
#     def setUp(self):
#         self.data = [15,16,19,20,25,1,3,4,5,7,10,14]
#
#     def test_search_rotated_found(self):
#         self.assertEqual(rotatedSearch(self.data, 3), True)
#
#     def test_search_rotated_notfound(self):
#         self.assertEqual(rotatedSearch(self.data, 2), False)


"""
10.4

Find a value in a sorted structure 'Listy' with no known length
0(1) lookups, positive ints in order

Initial thoughts:
 # binary search requires that an end index (hi bound) be known in order to calculate a mid
 # could do random index search by binary searching for index, start at 10k, if -1 then mid that until not -1
        if not -1 then square 10K until -1, then back to binary
 # could check memory size of table and take a guess at how big the table is
 # even just walking through the table would be a worse case of O(n), a billion ints could pose a problem
 # table of 2^2
        2, 4, 8, 16, 32, 64, 128, 256, 512...... 2^32:1 billion(ish)

Hints:
"""

class theListy(object):
    """
    Listy only contains sorted, positive integers
          only contains method to get element at i

    Use class theListy to find the index where a value occurs in the 'list'
    """

    def __init__(self, arr=[]):
        self.arr = arr

    def elementAt(self, i):
        """
        default behavior for listy
        can return a value, if outside of bounds return -1
        """
        if i < 0:
            return None
        if i > (len(self.arr) - 1):
            return -1
        return self.arr[i]

    def findEnd(self):
        """
        find end of listy
        increment end index by powers of 2 that grow very rapidly
        binary search will help us narrow down that elusive end
        """
        powerof2 = 1
        prevIndex = 0
        foundIndex = -1

        while foundIndex < 0:

            nextIndex = 2**powerof2
            #print "foundIndex({},{})".format(prevIndex, nextIndex)
            foundIndex = self.binarySearchEnd(prevIndex, nextIndex)
            prevIndex = nextIndex + 1
            powerof2 += 1

            # special case - if we don't find the end, prevent infinite looping
            if self.elementAt(prevIndex) < 0:
                break

        # returns index of end of listy, -1 if we didn't find it (should always find it!)
        return foundIndex

    def binarySearchEnd(self, lo, hi):
        """
        binary search until [int,-1] found
        """
        if lo > hi:
            return -1                               # base case - didn't find it!

        mid = (hi + lo) / 2                         # the binary part of binary search

        #print "testing... [{},{}] & [{},{}]".format(self.elementAt(mid-1), self.elementAt(mid), self.elementAt(mid), self.elementAt(mid+1))

        if self.elementAt(mid-1) > -1 and self.elementAt(mid) == -1:     # base case - found end of list
            #print "returning mid-1"
            return mid-1
        elif self.elementAt(mid) > -1 and self.elementAt(mid+1) == -1:
            #print "returning mid"
            return mid

        if self.elementAt(mid) < 0:
            return self.binarySearchEnd(lo, mid - 1)     # going left
        else:
            return self.binarySearchEnd(mid + 1, hi)     # going right

    def binarySearchVal(self, lo, hi, val=0):
        """
        binary search until [int,-1] found
        """
        if lo > hi:
            return -1                               # base case - didn't find it!

        mid = (hi + lo) / 2                         # the binary part of binary search

        #print "testing... [{},{}] & [{},{}]".format(self.elementAt(mid-1), self.elementAt(mid), self.elementAt(mid), self.elementAt(mid+1))

        if self.elementAt(mid) == val:              # base case - found it!
            return mid

        if self.elementAt(mid) > val:
            return self.binarySearchVal(lo, mid - 1, val)     # going left
        else:
            return self.binarySearchVal(mid + 1, hi, val)     # going right

def valIndexListy(arr=[], val=0):
    """
    trying out powers of 2 to find the end, then when -1, binary search until [int,-1] found
    """
    if not arr or val < 0:
        return None

    thisListy = theListy(arr)
    endIndex = thisListy.findEnd()
    if endIndex >= 0:
        # not to find the index of the actual value
        return thisListy.binarySearchVal(0, endIndex, val)

# arr_long_t01 = [1,2,3,4,6,6,7,8,9,10]
# print valIndexListy(arr_long_t01, 6)

# class valIndexListyTest(unittest.TestCase):
#
#     def setUp(self):
#         self.data = [1,2,3,4,5,6,7,8,9,10]
#
#     def test_val_index_listy(self):
#         self.assertEqual(5, valIndexListy(self.data, 6))

"""
10.5

Sparse search - search an array of sorted strings, sprinkled with empty spots

Thoughts:
 # probably emphasizing that the array is sorted, why the empty spots ?
 # binary search, possible since strings are sorted - although > < on space would impede outcome
 # can't get rid of spaces since we need to track index - could store in a hash then search, assuming no dups
   this would increase time O(n) in moving to hash, then run binary search @ O(logn)

Example: ball in ("at","","","","ball","","","car","","","dad","","") = 4

Going for the hashed, binary search option - here we go!

"""

def valIndexSparseList(arr=[], val=''):
    """
    find value in sparse list of sorted strings
    moving all strings to hash, tracking indexes - removing blank spaces
    hash is a O(1) search - no need to binary search it, return val will be index!
    I'm sure it's got to be harder than this, this a first go
    ** very much assuming there aren't any duplicate strings
    ** runtime O(n) - not great
    """
    if not arr or not val:
        return None

    hash_strings = {}

    #for i,v in enumerate(arr):
    for i in range(0, len(arr)):
        hash_strings[arr[i]] = i

    # now find the value in hash and return it's index
    if val in hash_strings:
        return hash_strings[val]


#arr_strings_t01 = ["at","","","","ball","","","car","","","dad","",""]
#print valIndexSparseList(arr_strings_t01, "ball")

# class valIndexSparseListTest(unittest.TestCase):
#
#     def setUp(self):
#         self.data = ["at","","","","ball","","","car","","","dad","",""]
#
#     def test_val_in_sparse_list(self):
#         self.assertEqual(4, valIndexSparseList(self.data, 'ball'))

"""
10.6

Sort a 20GB file consisting of one string per line

Explain how to go about sorting

Thoughts: consider how long each string is per line. if smallish then possibly store all

How many list items for 20GB of strings that are
20GB = 21,000,000,000 bytes
1 char is 8 bits (1 byte)
10 chars per line = 2,100,000,000 lines (that's 2.1 BILLION lines ... holy spa-kolee)

Any chance to sort the file in place ? ... like
"""

import os
import random
def create1GBIntFile():
    """
    generate file to gb_goal size
    """
    file_name = 'file_of_ints.txt'
    gb_bytes = 1073741824                   # number of bytes (per st_size) in a GB
    gb_goal = 1                             # number of GB to generate

    if not os.path.isfile(file_name):       # only create the file once

        file_conn = open(file_name, 'w')

        file_size = os.stat(file_name).st_size
        file_gb = file_size / gb_bytes
        while file_gb < gb_goal:

            file_size = os.stat(file_name).st_size
            file_gb = file_size / gb_bytes

            file_conn.write("{}\n".format(random.randint(0, 1000000000)))

import heapq
import contextlib
def mergeFiles(inFiles=[]):
    """
    merge multiple sorted files using a pythong heap library
    """
    files = [open(fn) for fn in inFiles]
    with contextlib.nested(*files):
        with open('output', 'w') as f:
            f.writelines(heapq.merge(*files))

def externalSort(f=None):
    """
    read file in chunks, process with quicksort, write back go on until done
    at the end combine all chunks
    """
    if not f:
        return None
    pass

#create1GBIntFile()

"""
10.7

a) find missing int in 4 billion non-negative ints with 1gb ram

Note: pip install bitstring then
      'from bitstring import BitArray, BitString'
      creating bit vector 'vector = BitArray(2**31)'
      then manipulate the array of bits from there

b) find missing int in 1 billion non-negative unique ints with 10mb ram

"""

# part 1, missing in 4 billion random positive ints (not necessairly unique)

import numpy as np
from bitstring import BitArray  # need to use a BitArray to store bits as ints to save space
import random
import sys
import time

def gen4BillIntsImports():
    """
    going to generate 4 billion random ints and put them directly into the bitstring bit vector
    this is a pseudo read from file thing, to save space and time in generating and then reading a very large file
    """
    time_start = time.time()

    # bit_vector = BitArray(4000000000)

    # going to need to loop 4 billion times - this might take a minute or two
    # Note: 8 seconds for 1 million
    # Speed on a mac - a million rows @ 6 sec * 2000 (to get to 2 billion) = 3.33 hours to complete = no bueno
    #                  how can this be sped up?
    # for i in xrange(0, 2**31):
    #     if i % 1000000 == 0:
    #         print "{} @ {} seconds".format(i, time.time() - time_start)
    #     bit_vector[random.randint(0, (2**31 - 1))] = 1

    ## iterating through bit_vector - even slower
    # for i, b in enumerate(bit_vector):
    #     if i % 1000000 == 0:
    #         print "{} @ {} seconds".format(i, time.time() - time_start)
    #     bit_vector[i] = random.randint(0, 1)

    # print "size of bit_vector:", sys.getsizeof(bit_vector)
    # for i in range(0, 100):
    #     print bit_vector[i]

    ## numpy

    # numpy_bits = np.random.randint(256, size=(1000000000//8,)).astype(np.uint8)
    #
    # def get_bools(a, i):
    #     b = i // 8
    #     o = i % 8
    #     mask = 1 << o
    #     return (a[b] & mask) != 0
    #
    # for i in range(999999500, 1000000000):
    #     print get_bools(numpy_bits, i)
    #
    # time_end = time.time()
    # print("--- %s seconds ---" % (time_end - time_start))

def findMissingInt1GB():
    """
    using bytes as 32 bit containers
    need 4 billion bits as ints (depicted by index // 32) e.g. a[0][1]....[31] is one int storing 32 placeholders
    4 billion / 32 = 125000000 ints = 4 bytes * 125 million bytes = .12 GB
    Note: not reading in 4 billion ints, not looping 125 million times - this test shows working method
          should produce file that is .93 GB when running full steam
    """
    #bit_vector = range(125000000)          # large enough to hold 4 billion bits
    bit_vector = range(31250)               # large enough to hold 1 million bits - TESTING
    for i in bit_vector:
        # assigning random number to each index, this will be random integer by bits
        bit_vector[i] = random.randint(2147483647, 2**31)    # all positive ints

    print "generated 1 billion ints with size:{}... yikes... now look for missing int".format(sys.getsizeof(bit_vector))

    for i in range(0, len(bit_vector)):
        next_bit = bit_vector[i]
        for j in range(0, 32):
            if (next_bit >> j == 0):
                int_missing = (i * 32) + j
                print "missing int {} @ bit_vector[{}]:{} {}... done and done!".format(int_missing, i, next_bit, bin(next_bit))
                return

def findMissingInt10MB():
    """
    Note:
       1 billion non-negative, unique, integers

    data:
       Need space for bit_bucket, how many bits is that when a bit represents an int
       bytes in 1MB is 2**20, in 10MB is 2**20 * 9 (for wiggle room)
       1 billion / (2**20 * 9MB * 8bits) = 75 Million bits
       1 billion / 75 Million bits = 15 buckets

    bit vector
       size is 75 million bits / 8 bits per byte / 4 bytes per int = 2.5 million ints (2343750) to be exact

    """

    # buckets
    bit_bucket = {}
    bit_bucket_count = 0
    for i in range(0, 15):

        bit_bucket_count += 75000000

        if bit_bucket_count <= 1000000000:
            bit_bucket_size = 75000000
        else:
            bit_bucket_size = 1000000000 - (bit_bucket_count - 75000000)

        bit_bucket[i] = [bit_bucket_size ,0]

        if bit_bucket_count >= 1000000000:
            break

    # open file for reading and read 80 million lines - real, real slow like
    # fill those bucket counts bucket [0](0 to 79999999 million), [1](80000000 to 159999999 million) etc...

    with open('file_of_14712434_ints.txt', 'r') as f:

        for line in f:

            up_int = line                       # integer
            up_bucket = int(up_int) // 75000000      # bucket
            bit_bucket[up_bucket][1] += 1       # increment bucket count

    f.close()

    # now find the missing int using bit vector logic with a zero bit
    bit_bucket_missing = None
    for i in range(0, len(bit_bucket)):
        print "comparing bit_bucket {} < {}".format(bit_bucket[i][1], bit_bucket[i][0])
        if bit_bucket[i][1] < bit_bucket[i][0]:         # counts don't savvy
            bit_bucket_missing = i
            break

    # build then read bits into vector
    if bit_bucket_missing is not None:
        bit_bucket_range = bit_bucket[i][0] / 32
        bit_vector = range(bit_bucket_range)
    else:
        print "no integers missing!"
        return

    # read the file again, this time filling in bits in this range
    with open('file_of_14712434_ints.txt', 'r') as f:

        for line in f:

            up_int = int(line)

            bit_index = up_int // 75000000

            if bit_index == bit_bucket_missing:

                bit_block = (up_int - (75000000 * bit_index)) / 32

                bit_shift = (up_int - (75000000 * bit_index)) - (32 * bit_block)

                bit_vector[bit_block] |= 1 << bit_shift
                #print "up_int:", up_int, "bit_index:", bit_index, " bit_block:", bit_block, " bit_shift:", bit_shift
                #print "set bit_vector[{}] |= 1 << {}".format(bit_block, bit_shift)

    f.close()

    # Test view first 100 integers (binary parts)
    #for i in range(0, 100):
    #    print bin(bit_vector[i])

    # find first zero in binary parts of bit_vectors
    for i in range(0, len(bit_vector)):
        next_bit = bit_vector[i]
        for j in range(0, 32):
            if (next_bit >> j == 0):
                bit_integer_missing = bit_bucket_missing * 75000000 + (i * 32) + j
                print "missing int {} @ bit_vector[{}]:{} {}... done and done!".format(bit_integer_missing, i, next_bit, bin(next_bit))
                return

def fillBits():
    """
    Test to OR bits to 1 on command
    """
    bit_array = [0]

    for i in range(0,32):
        bit_array[0] |= 1 << i
        print i, bin(bit_array[0]), bit_array

#fillBits()
#findMissingInt1GB()
#findMissingInt10MB()

"""
10.8

Find and print all duplicate ints where n is 1 to max 32,000
This must be done in 4kB

4kB = 2^10 * 4 bytes = 4096 bytes
an int is 4 bytes - 4kB of ints is 4096 / 4 ints = 1024 ints

fudge room - make it 1000 ints at a time
although, using bits as ints could squeeze 4096 bytes * 8 bits = 32768 bits

so... using a bit vector, could store all 32K and check for bit shift that is already set to 1
"""

# exercise: bit_vector class
class BitVector(object):
    """
    bit vector class
    load read, write and test if already set (isset)
    """
    def __init__(self, size=0):
        """
        input size of data
        size is based on 32 bits per int in 4 bytes, although python uses bit int which is 64 bits in 8 bytes
        data will be a list of ints based on input bit size
        """
        self.size = size
        self.int_index = 0
        self.bit_index = 0

        if size % 64 != 0:
            raise ValueError('input size must be an incremental size of 64')

        self.data = range(size // 64)

    def bit_r(self, idx):
        """
        read a bit, parm: integer in range
        """
        self.bit_inrange(idx)

        return self.data[self.int_index] >> self.bit_index

    def bit_w(self, idx):
        """
        write a bit, parm: integer in range
        """
        self.bit_inrange(idx)

        self.data[self.int_index] |= 1 << self.bit_index

    def bit_isset(self, idx):
        """
        return True or False if bit might have already been set
        """
        self.bit_inrange(idx)

        if self.data[self.int_index] >> self.bit_index == 1:
            return True
        else:
            return False

    def bit_inrange(self, idx=None):
        """
        evaluate if integer is in range of bit vector

        int should be in range 0 to 64 * int .. e.g., bit = (32000 / 64) - 1 = 500
        """
        if idx is None or type(idx) is not int:
            raise ValueError('an integer must be passed in order to execute this bit class. passed in {}'.format(idx))

        # idx - 1 because range starts at 1 where bit starts at zero
        ##
        # test: 64. int_index (64 - 1) // 64 = 0  (should be zero)
        #           bit_index (64 - 1) - (0 * 64) (should be 63)
        self.int_index = (idx - 1) // 64
        self.bit_index = (idx - 1) - (self.int_index * 64)

        # TEST - Errors
        # if self.int_index < 0:
        #     print "error self.int_index:", self.int_index
        # if self.bit_index < 0 or self.bit_index > 63:
        #     print "error: self.bit_index:", self.bit_index

        if self.int_index <= self.size:
            return True
        else:
            raise ValueError('integer outside of bounds of bit vector. range should be 0 to {}'.format(64 * self.size))

# part 1 - build the randomized test list 1 to random n up to 32K
def findDupIntGen():
    """
    generate list of ints 1 to max 32,000
    return list
    note: not counting this as part of the memory,
          the meat of the program could be reading this as a text file etc...
    note: list can be of any length, that wasn't specified
    """
    list_ints = []
    for i in range(10000):
        list_ints.append(random.randint(1, 32000))

    return list_ints

# part 2 - find any duplicates in the randomized list
def findDupIntUtil(a=[]):
    """
    find duplicate int in a
    use a bit vector to store 4kB
    bit_vector = 1 int = 4 bytes * 8 bits = 1000 ints

    Note: on mac an int is 8 bytes (big int - 64 bits) in size therefore only need 500 ints
    """
    if not a:
        return []

    int_duplicate = []

    bits = BitVector(32000)

    for i in a:
        if bits.bit_isset(i):
            int_duplicate.append(i)
        else:
            bits.bit_w(i)

    # bit_vector = range(500)     # should be 4072 bytes / 2^10 = 3.97kB .. perfecto!

    # for i in a:
    #
    #     int_index = (i // 64)               # which int in the vector: e.g., 63 // 64 = 0, 64 // 64 = 2, 128 // 64 = 2 etc...
    #     bit_index = i - (int_index * 64)    # which bit in the int: e.g. 63 - (0 * 64) = 63, 64 - (1 * 64) = 1, 128 - (2 * 64) = 0
    #
    #     if bit_vector[int_index] >> bit_index == 1:
    #         int_duplicate.append(i)
    #     else:
    #         bit_vector[int_index] |= 1 << bit_index

    return int_duplicate

def findDupInt():

    print "duplicate integers found:", findDupIntUtil(findDupIntGen())

#findDupInt()

# part 3 - take a break, you earned it buddy!
def takeABreak():
    coffee = "triple shot americano"
    scone = "blueberry"
    newspaper_pages = "funnies"
    print "I am drinking a {} while eating a {} and reading the {} in the newspaper".format(coffee, scone, newspaper_pages)

"""
10.9

Find a value in an MxN matrix best time complexity
"""

def matrixSectionUtil(m, v=None, p1=[None, None], p2=[None, None]):
    """
    Break grid into sections until value found / not found
    half grid each time until width or height is 1
    assume m, v, p1, p2 passed from caller
    m:matrix
    v:value
    p1:point 1
    p2:point 2

    example call matrixSection(m, 22, [0,0], [10,10])

    0,0
    0,1
    0,2        10,9
    ...........10,10

    time best O(1), average O(n) n/4 + n/4 ... O(n)

    """

    #print "matrixSectionUtil p1:{}:{} p2:{}:{}".format(p1, m[p1[0]][p1[1]], p2, m[p2[0]][p2[1]])

    # in range - not necessairly always in this block though
    if v >= m[p1[0]][p1[1]] and v <= m[p2[0]][p2[1]]:

        # note: matrix stored as [v:down, h:right]
        # find mid point - horizontal & vertical
        h_mid = (p2[1] - p1[1]) // 2
        v_mid = (p2[0] - p1[0]) // 2
        h_len = len(m[0]) - 1
        v_len = len(m) - 1

        # corner(s) check
        # could be 2x2, 1x1 square - easier to just check these options first
        if p1[0] <= v_len and p1[1] <= h_len:
            if v == m[p1[0]][p1[1]]:    # upper left pixel
                return [p1[0], p1[1]]

        if p1[0] <= v_len and p2[1] <= h_len:
            if v == m[p1[0]][p2[1]]:    # upper right pixel
                return [p1[0], p2[1]]

        if p2[0] <= v_len and p1[1] <= h_len:
            if v == m[p2[0]][p1[1]]:    # lower left pixel
                return [p2[0], p1[1]]

        if p2[0] <= v_len and p2[1] <= h_len:
            if v == m[p2[0]][p2[1]]:    # lower right pixel
                return [p2[0], p2[1]]

        # block in 2x2. if value not found, return None to prevent recursion overload
        if p2[0] - p1[0] <= 1 and p2[1] - p1[1] <= 1:
            return None

        # upper left
        qp1 = [p1[0], p1[1]]
        qp2 = [p2[0] - h_mid, p2[1] - v_mid]
        pv = matrixSectionUtil(m, v, qp1, qp2)
        if pv is not None:
            return pv

        # upper right
        qp1 = [p1[0], p1[1] + h_mid]
        qp2 = [p2[0] - v_mid, p2[1]]
        pv = matrixSectionUtil(m, v, qp1, qp2)
        if pv is not None:
            return pv

        # lower left
        qp1 = [p1[0] + h_mid, p1[1]]
        qp2 = [p2[0], p2[1] - v_mid]
        pv = matrixSectionUtil(m, v, qp1, qp2)
        if pv is not None:
            return pv

        # lower right
        qp1 = [p1[0] + h_mid, p1[1] + v_mid]
        qp2 = [p2[0], p2[1]]
        pv = matrixSectionUtil(m, v, qp1, qp2)
        if pv is not None:
            return pv

    else:
        return None

def matrixSection(m, v):
    """
    Calling matrix section utility
    matrixSectionUtil(matrix, value to find, upper left point p1, lower right point p2)
    """
    print "matrixSection: found {} @ {}".format(v, matrixSectionUtil(m, v, [0,0], [len(m)-1, len(m[0])-1]))

#mn = [[120]]

# mn = [[118],
#       [120]]

mn = [[5,20,70,85],
      [20,35,80,95],
      [30,55,95,105],
      [40,81,100,120],
      [50,86,102,125]]

# matrixSection(mn, 5)
# matrixSection(mn, 85)
# matrixSection(mn, 125)
# matrixSection(mn, 50)
# matrixSection(mn, 81)

def matrixStepUtil(m, v):
    """
    search matrix using the step method
    start upper right
    is value larger, go left
    if value smaller, go down
    time avg less than O(m+n), worst O(m+n)
    """
    upper_right_index = len(m[0]) - 1
    h_index = 0
    v_index = upper_right_index

    while h_index >= 0 and v_index <= len(m) - 1:

        if v == m[h_index][v_index]:
            return [h_index, v_index]

        elif m[h_index][v_index] > v:
            # go left
            v_index -= 1

        else:
            # go down
            h_index += 1

def matrixStep(m, v):
    print "matrixStep find:{} result:{}".format(v, matrixStepUtil(m, v))

#matrixStep(mn, 100)

# class matrixStepTest(unittest.TestCase):
#
#     def setUp(self):
#         self.mn = [[5,20,70,85],
#                   [20,35,80,95],
#                   [30,55,95,105],
#                   [40,81,100,120],
#                   [50,86,102,125]]
#
#     def test_matrix_step(self):
#         self.assertEqual(matrixStepUtil(self.mn, 100), [3, 2])
#
#     def test_matrix_section(self):
#         self.assertEqual(matrixSectionUtil(self.mn, 100, [0,0], [len(self.mn)-1, len(self.mn[0])-1]), [3, 2])

"""
10.10

Stream of integers, find rank of number in stream (number of values less than queried)

stream: 5, 1, 4, 4, 5, 9, 7, 13, 3
 order: 1, 3, 4, 4, 5, 5, 7, 9, 13

getRankOfNumber(1) = 0
getRankOfNumber(3) = 1
getRankOfNumber(4) = 3

naive approach: sort (radix) for O(kn) complexity, then return index of last occurance of value

solution: binary search tree. keep track of how many nodes at root in left sub-tree
          time complexity of self.bst is O(logn) for insert, find
          will need to keep track of the number of nodes inserted under another node

test: won't go into re-creating a BST insert, just assume that all nodes already set

"""

def bstSize(n):
    """
    count number of nodes in defined n
    breadth first traversal - queue
    time complexity O(n) - visits every node
    """
    if not n:
        return 0

    count = 1
    queue = []

    # not counting root node, queue up left and right from root
    if n.left:
        queue.append(n.left)
    if n.right:
        queue.append(n.right)

    while queue:

        current = queue.pop()

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        count += 1

    return count

def bstGetRankOfUtil(n, v):
    """
    get rank of v(value)
    using bst best practices, value greater go right, else go left

    value found: add all left from value to count and return
    value left: go left - nothing added to count
    value right: go right, add 1 + all lefts passed

    """
    count_rank = 0
    current = n

    while current is not None:

        if current.data == v:

            # increment rank with skipped left
            size_left = bstSize(current.left)
            #print "size_left of {} is {}".format(current.data, size_left)
            count_rank += size_left

            return count_rank

        elif v > current.data:

            # increment rank with skipped left
            size_left = bstSize(current.left)
            #print "size_left of {} is {}".format(current.data, size_left)
            count_rank += 1 + size_left

            # go right
            current = current.right

        else:
            # go left
            current = current.left

class node(object):
    """
    node object, store data, left, right,
    """
    def __init__(self, data=None, right=None, left=None):
        self.data = data
        self.left = left
        self.right = right

# test node v1
# stream: 3,1,2,4,4,5,5
# in ord: 1,2,3,4,4,5,5
bst = node(3)
bst.left = node(1)
bst.left.right = node(2)
bst.right = node(4)
bst.right.left = node(4)
bst.right.right = node(5)
bst.right.right.left = node(5)

# test node v2
# stream: 5,1,4,4,5,9,7,13,3
# in ord: 1,3,4,4,5,5,7,9,13
bst = node(5)
bst.left = node(1)
bst.left.right = node(4)
bst.left.right.left = node(4)
bst.left.right.left.left = node(3)
bst.left.right.right = node(5)
bst.right = node(9)
bst.right.left = node(7)
bst.right.right = node(13)

def bstGetRankOf(n, v):
    """
    calling program to util
    """
    print "bstGetRankOf value:{} result:{}".format(v, bstGetRankOfUtil(n, v))

# bstGetRankOf(bst, 1)
# bstGetRankOf(bst, 3)
# bstGetRankOf(bst, 4)
# bstGetRankOf(bst, 5)
# bstGetRankOf(bst, 13)

# class bstGetRankOfTest(unittest.TestCase):
#
#     def setUp(self):
#         """
#         Test Node:
#                   (5)5
#           (0)1                 (7)9
#                (3)4       (6)7     (8)13
#            (2)4    (4)5
#         (1)3
#         """
#         self.bst = node(5)
#         self.bst.left = node(1)
#         self.bst.left.right = node(4)
#         self.bst.left.right.left = node(4)
#         self.bst.left.right.left.left = node(3)
#         self.bst.left.right.right = node(5)
#         self.bst.right = node(9)
#         self.bst.right.left = node(7)
#         self.bst.right.right = node(13)
#
#     def test_ranks(self):
#         self.assertEqual(bstGetRankOfUtil(self.bst, 1), 0)
#         self.assertEqual(bstGetRankOfUtil(self.bst, 3), 1)
#         self.assertEqual(bstGetRankOfUtil(self.bst, 7), 6)
#         self.assertEqual(bstGetRankOfUtil(self.bst, 5), 5)

"""
10.11

Peaks and Valley in array of ints
peak when adjacent are smaller
valley when adjacent are larger

brute force approach:
  O(n) walk through array
  when the next value is greater (keep last value in storage), the stored value is valley
  when the next value is lesser (......), the stored value is a peak
  store peaks and valleys in extra space, all others in extra space
  at the end tie the two extras into one and return
"""

def pandvBF(a):
    """
    peaks and valleys Brute Force
    time complexity O(n), extra space O(n) - don't see it getting faster than that
    issues with this method - not peak then valley, can be valley then peak
    """
    if not a:
        return []

    curr_int = a[0]     # first in in array
    curr_dir = None     # lt, gt
    p_and_v = []        # peak and valley storage
    the_rest = []       # everything else storage

    #print "curr_int:{} curr_dir:{}".format(curr_int, curr_dir)

    for i in range(1, len(a)):

        if a[i] == curr_int:

            #print "a[i]:{} == curr_int:{}".format(a[i], curr_int)

            # no change - at to the regular pile
            #print "   append all the rest {}".format(curr_int)
            the_rest.append(a[i])

        elif a[i] > curr_int:

            #print "a[i]:{} 'gt' curr_int:{}".format(a[i], curr_int)

            if curr_dir is None or curr_dir == "lt":
                # switching from less to greater - curr_int is peak
                #print "   re-direction append {} to p_and_v".format(curr_int)
                p_and_v.append(curr_int)
            else:
                #print "   append all the rest {}".format(curr_int)
                the_rest.append(curr_int)

            curr_dir = "gt"
            curr_int = a[i]

        else:

            #print "a[i]:{} 'lt' curr_int:{}".format(a[i], curr_int)

            if curr_dir is None or curr_dir == "gt":
                # switching from greater to less - curr_int is valley
                #print "   re-direction append {} to p_and_v".format(curr_int)
                p_and_v.append(curr_int)
            else:
                #print "   append all the rest {}".format(curr_int)
                the_rest.append(curr_int)

            curr_dir = "lt"
            curr_int = a[i]

        #print "curr_int:{} curr_dir:{} a[i]:{}".format(curr_int, curr_dir, a[i])

    #print "p_and_v:", p_and_v, " the_rest:", the_rest

    p_and_v = p_and_v + the_rest
    p_and_v.append(a[-1])           # last element in array, since looking 1 behind need to tack on

    return p_and_v

def pandvSwap(a):
    """
    peak and valley swapper
    walk through array, if p or v out of order (defined peak(larger), then valley(smaller))
       swap from adjacent elements, or however many are left to the end of the array
       e.g. [1,3,2] - 1 is a valley, from None <- 1 -> 3 - switch with 3 ==> [3,1,2]

       runtime O(n), no extra space
    """
    if not a:
        return []

    def swap(i, y):
        """
        swap value @ index i for y
        """
        print "it's swap time! {} for {}".format(a[i], a[y])

        if (i < 0 or i > len(a) - 1) and (y < 0 or y > len(a) - 1):
            return

        temp = a[i]
        a[i] = a[y]
        a[y] = temp

    prev_i = 0
    curr_d = "v" # peaks first!
    for i in range(1, len(a)):   # loop through, skip 2

        if curr_d == "p":
            # peaks
            if a[prev_i] > a[i]:
                # need to swap
                swap(prev_i, i)
            curr_d = "v"
        else:
            # valleys
            if a[prev_i] < a[i]:
                # need to swap
                swap(prev_i, i)
            curr_d = "p"

        prev_i = i

    return a

l01 = [5,8,6,2,3,4,6] # where [8,6] are peaks and [5,2] are valleys
l02 = [5,3,1,2,3] # p:5 v:1 -> [5,1,3,2,3]
#print pandvBF(l01)
print pandvSwap(l01)

######## unit test ########
if __name__ == '__main__':
    unittest.main()
