"""
Fun with CodeLab!
"""

def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        print B
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    print B
    return B

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# B = performOps(A)
# for i in xrange(len(B)):
#     for j in xrange(len(B[i])):
#         print B[i][j],

# Util functions
def issetBit(integer, index):
    # check if bit is set
    #print "issetBit int:{} idx:{}".format(integer, index)
    if integer is None or index is None:
        return None
    bit = integer & (1 << index)
    if bit > 0:
        return True
    return False

def setBit(integer, index):
    # set a bit in integer at index(index)
    # note: index range(0 to infinity ?)
    #print "setBit int:{} idx:{}".format(integer, index)
    if integer is None or index is None:
        return None
    integer = integer | (1 << index)
    return integer

def clearBit(integer, index):
    # clear a bit in in at index(index)
    #print "clearBit int:{} idx:{}".format(integer, index)
    if integer is None or index is None:
        return None
    integer = integer & ~(1 << index)
    return integer

def whichBit(integer):
    # which bits are flipped
    # return list of index values
    if integer is None:
        return None
    lst_index = []
    if integer > 0:
        for i in range(0, len(bin(integer))):
            # read bit
            bit = integer & (1 << i)
            if bit > 0:
                lst_index.append(i)
    return lst_index

class singleNumber:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        ret = A[0]
        for i in range(1,len(A)):
            ret ^= A[i]
        return ret

        # Brute Force
        # A = list(A)
        # python .sort time is O(nlogn) - as good as quicksort and mergesort
        # although not sure about space. quicksort = O(logn) and mergesort = O(n)
        # A.sort()
        # check = None
        # for i in A:
        #     if check is None:
        #         check = i
        #     elif check != i:
        #         return check
        #     else:
        #         check = None
        # return 0

        # Using a bit-array
        # lst_bit = {}
        # for i in A:
        #
        #     # setting bits
        #     # note: python ints are big-ints, 8 bytes = 64 bits
        #
        #     # list bit index integer
        #     # e.g. 2 = 2 // 64 = 0
        #     # e.g. 67 = 67 // 64 = 1
        #     lst_index = i // 64
        #
        #     # bit index (sub bit in list)
        #     # e.g. (2 - (64 * 0)) = 2
        #     # e.g. (67 - (64 * 1)) = 3
        #     bit_index = (i - (64 * lst_index))
        #
        #     # set a zero for bit range
        #     if lst_index not in lst_bit:
        #         lst_bit[lst_index] = 0
        #
        #     # set or clear bits
        #     if issetBit(lst_bit[lst_index], bit_index):
        #         lst_bit[lst_index] = clearBit(lst_bit[lst_index], bit_index)
        #     else:
        #         lst_bit[lst_index] = setBit(lst_bit[lst_index], bit_index)
        #
        # # find bits not set
        # lst_singles = []
        # for i in lst_bit:
        #     # loop through returned list of bits flipped
        #     lst_bit_flipped = whichBit(lst_bit[i])
        #
        #     for f in lst_bit_flipped:
        #         bit_flipped = (64 * i) + f
        #
        #         # for test - just return first flipped
        #         return bit_flipped
        #
        #         # for debugging, send to list
        #         lst_singles.append(bit_flipped)
        #
        # # debugging
        # print "\rlist singles:", lst_singles
        # print lst_bit

# 4,4,3,3,2,2,1
# single_number = singleNumber()
# lst_single = [ 723, 256, 668, 723, 140, 360, 597, 233, 128, 845, 737, 804, 986, 701, 906, 512, 845, 510, 510, 227, 430, 701, 366, 946, 464, 619, 946, 627, 209, 771, 424, 555, 959, 711, 530, 937, 716, 261, 505, 658, 706, 140, 511, 277, 396, 233, 819, 196, 475, 906, 583, 261, 147, 658, 517, 197, 196, 702, 944, 711, 128, 555, 149, 483, 530, 291, 716, 258, 430, 464, 601, 749, 149, 415, 802, 573, 627, 771, 660, 601, 360, 986, 291, 51, 415, 51, 227, 258, 937, 366, 923, 669, 33, 517, 417, 702, 475, 706, 110, 417, 275, 804, 500, 473, 746, 973, 669, 275, 973, 147, 817, 657, 277, 923, 144, 660, 197, 511, 793, 893, 944, 505, 322, 817, 586, 512, 322, 668, 33, 424, 962, 597, 144, 746, 345, 753, 345, 269, 819, 483, 368, 802, 573, 962, 583, 615, 208, 209, 269, 749, 256, 657, 619, 893, 959, 473, 753, 299, 396, 299, 500, 368, 586, 110, 793, 737, 615 ]
# #lst_single = [2,2,65,65,63]
# print "single number:", single_number.singleNumber(lst_single)

class numSetBits:
    # @param A : integer
    # @return an integer
    # Write a function that takes an unsigned integer and returns the number of 1 bits it has.
    def numSetBits(self, A):
        num_bits = 0

        while A != 0:
            if A&1:
                num_bits += 1
            A = A>>1

        # bitly way
        # for i in xrange(0, len(bin(A))):
        #     if A & (1<<i) > 0:
        #         num_bits += 1

        # iterate string
        #for i in bin(A):
        #    if i == '1':
        #        num_bits += 1

        return num_bits

# num_set_bits = numSetBits()
# int_test = int('00000000000000000000000000001011', 2)
# print num_set_bits.numSetBits(int_test)

class detectCycle:

    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):

        # track visits - easy peasy  see somebody we know, that's the start of the loop!
        pass

        # using Floyd's cycle - walk, run!
        # w = A
        # r = w
        # while w:
        #     w = w.next
        #     if r and r.next:
        #         r = r.next.next
        #     else:
        #         return None # no loop detected
        #     if w == r:
        #         found_loop = True
        #         break
        #
        # w = A
        # # find start of loop - walk both until a match
        # while w:
        #     w = w.next
        #     r = r.next
        #     if w == r:
        #         return w.val

# num_set_bits = numSetBits()
# int_test = int('00000000000000000000000000001011', 2)
# print num_set_bits.numSetBits(int_test)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

detect_cycle = detectCycle()
# example: run into each other @ 7, start of loop @ 2!
# [1|]->[2|]->[3|]->[4|]
#         |           |
#       [7|]->[6|]->[5|]
# node_test = ListNode(1)
# node_test.next = ListNode(2)
# node_test.next.next = ListNode(3)
# node_test.next.next.next = ListNode(4)
# node_test.next.next.next.next = ListNode(5)
# node_test.next.next.next.next.next = ListNode(6)
# node_test.next.next.next.next.next.next = ListNode(7)
# node_test.next.next.next.next.next.next.next = node_test.next
# print detect_cycle.detectCycle(node_test)

class primeSum:

    # @param A : integer
    # @return a list of integers
    def __init__(self):
        self.dct_primes = {}
        self.lst_primes = []

    def is_prime(self, n):
        # is n prime ?
        if n in self.dct_primes:
            return self.dct_primes[n]
        if n < 2:
            return False
        for i in xrange(2, n-1):
            if n % i == 0:
                self.dct_primes[n] = False
                return False
        # made it this far, must be true!
        self.dct_primes[n] = True
        return True

    def ls_primes(self, n):
        # build range of primes up to n
        # primes are natural numbers greater than 1, divisible by one and itself
        for i in range(2, n):
            if self.is_prime(i):
                self.lst_primes.append(i)

    def sv_primes(self, n):
        """
        Sieve of Eratosthenes
        """
        sieve = [True] * n
        for i in xrange(3, int(n**0.5) + 1, 2):
            if sieve[i]:
                #sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
                # same as:
                # starting at sqare of i, then skip every other
                for j in xrange(i*i, n, 2*i):
                    sieve[j] = False

        return [2] + [i for i in xrange(3, n, 2) if sieve[i]]
        #self.lst_primes = [2] + [i for i in xrange(3,n,2) if sieve[i]]

    def primesum(self, A):

        # primes need to be larger than 1
        if A <= 2:
            return []
        if A % 2 > 0:
            return []

        # build dict of primes
        self.sv_primes(A)

        # now walk the dict of primes
        # start @ 2 - if less than, walk lesser right until greater
        # end - if greater than, walk greater left until lesser
        # do only while lesser less than greater .. savvy ?

        i = 0
        j = len(self.lst_primes) - 1
        lst_match = []
        while i <= j:
            if self.lst_primes[i] + self.lst_primes[j] == A:
                # found a match!
                lst_match.append([self.lst_primes[i], self.lst_primes[j]])
                # now walk i
                i = i + 1
            elif self.lst_primes[i] + self.lst_primes[j] > A:
                # greater than - walk j
                j = j - 1
            else:
                # less than - walk i
                i = i + 1

        #print "lst_primes:", self.lst_primes, " lst_match:", lst_match
        print "min.lst_match:", min(lst_match), " lst_match:", lst_match
        if lst_match:
            return min(lst_match)
        else:
            return []

# prime_sum = primeSum()
# prime_sum.primesum(100)

class power2:

    def power2(self, A):

        """
        Find an exponent situation where
        a >= 1, p >= 2 note: a >= 2 makes more sense.. 1**1, 1**10000 = 1
        and where
        a ^ p = n
        e.g., 2^3 = 8 .. a=2, p=8

        also note: 2**31 possibilities of ints .. about 2.1 billion!
        square root of that is 46,341 - actually not bad to loop through (at least once)

        returns True if exponent match found

        Initital thoughts:
          brute force up to square root of n range(1, int(n**.5) + 1)
          Runtime will be O(n^2)

        Also thinking logs might work where log(base p) = (a) a=2, p=3 -> 2^3 = 8 log(8)=2 -> 3
        To find the exponential limit.. e.g., 2**31, 31 is upper exponent... base 5 is 13 etc..
        """

        ## This works, however - it's time complexity is O(n**2)
        # for p in xrange(2,32):
        #     for A in xrange(2, int(n**(1.0 / p)) + 2):
        #         if A**p == n:
        #             return True

        # tracking bound n**(1.0/i)
        # since 2**31 is the largest exponent that'll be the range
        # starting @ 2 since p(exponent) >= 2
        for i in range(2, 32):

            # boundary taking the root of n till very small
            b = A**(1.0/i)
            print i, b

            # base case, less than 2
            #if b < 2:
            #    return False

            # natural numbers
            # fix the float, int so we can subtract
            flt_b = float(str(b))
            int_b = int(float(str(b)))
            if flt_b - int_b == 0:
                return True

        return False

# power_of = power2()
# #print power_of.power2(823543)
# print power_of.power2(1073741824)

class moveIt:

    def move_it(self, X, Y):
        """
        L: list of points to move to
        can move by 1 in any direction - that counts as 1 move (which we'll return)
        not sure how to handle points that are further than 1 away ? - need to test data in 'expected output'
        I'm assuming for now that we'll need to move a number of times to get to the next point,
          regardless if it's only 1 away.. just keep track of moves
        """

        if not X and not Y:
            return 0
        if len(X) != len(Y):
            return 0

        moves = 0
        prv_point = None

        for i in range(0, len(X)):
            # iterate through points
            # per rules, we can move 1 in each direction x or y
            if not prv_point:
                prv_point = [X[i], Y[i]] # X[0],Y[0]
            else:
                # compare current point with previous point
                # take the largest of difference of X and Y
                diff_X = abs(prv_point[0] - X[i])
                diff_Y = abs(prv_point[1] - Y[i])
                print diff_X, diff_Y

                if diff_X >= diff_Y:
                    moves += diff_X
                else:
                    moves += diff_Y

                prv_point = [X[i], Y[i]]

        return moves


# move_it = moveIt()
# #print move_it.move_it([-7, -13], [1, -5])
# print move_it.move_it([4, 8, -7, -5, -13, 9, -7, 8], [4, -15, -10, -3, -13, 12, 8, -8])

# X: -7 -13
# Y: 1 -5

# X: 4 8 -7 -5 -13 9 -7 8
# Y: 4 -15 -10 -3 -13 12 8 -8

def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in xrange(len(A)):
        B[i] = A[i]
        print (len(A) - i) % len(A)
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B

# A = [5,10,2,1]
# B = performOps(A)
# for i in xrange(len(B)):
#     print B[i],

class nMatrix:

    """
	@param a : list of list of integers
	@return a list of list of integers
	"""
    def n_matrix(self, a):

        if len(a) == 1:
            return [0,0]

        rev_diagonal = []
        org_diagonal = []
        cur_count = 1
        cur_start = True

        while cur_count > 0:

            tmp_diagonal = []

            for i in range(0, cur_count):
                if cur_start:
                    tmp_diagonal.append([i, cur_count -1 - i])
                else:
                    down_x = rev_diagonal[cur_count - 1][i][0] + (len(a) - cur_count)
                    down_y = rev_diagonal[cur_count - 1][i][1] + (len(a) - cur_count)
                    tmp_diagonal.append([down_x, down_y])

            rev_diagonal.append(tmp_diagonal)
            #print rev_diagonal

            if cur_count == len(a):
                cur_start = False

            if cur_start:
                cur_count += 1
            else:
                cur_count -= 1

        ## ---------------------

        for i in rev_diagonal:
            tmp_diagonal = []
            for j in i:
                #print "a:", a[j[0]][j[1]]
                tmp_diagonal.append([a[j[0]][j[1]]])
            org_diagonal.append(tmp_diagonal)

        #print org_diagonal
        return org_diagonal


# n_matrix = nMatrix()
# m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# #m = [[1,2],[3,4]]
# n_matrix.n_matrix(m)

class diagonalMatrix:
    """
    Second shot at diagonal matrix... using clues, discovered less brain twisting way to do it
    matrix is (nxn); e.g.
      1 2
      3 4
    """
    def diagonal_matrix(self, a):

        if len(a) == 1:
            return [a[0]]

        q = [[[0,0]]]
        l = [[a[0][0]]]

        while q:

            cur = q.pop(0)
            tmp = []            # temp sub-list for q
            t = []

            for i in cur:

                if i[1] + 1 < len(a) and [i[0], i[1] + 1] not in tmp:
                    tmp.append([i[0], i[1] + 1])
                    t.append(a[i[0]][i[1] + 1])

                if i[0] + 1 < len(a) and [i[0] + 1, i[1]] not in tmp:
                    tmp.append([i[0] + 1, i[1]])
                    t.append(a[i[0] + 1][i[1]])

            if tmp:
                q.append(tmp)
            if t:
                l.append(t)

        return l

# diagonal_matrix = diagonalMatrix()
# m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print diagonal_matrix.diagonal_matrix(m)

class steppingNumber:

    """
    A stepping number is a number where each digit (in the number) is one number away to the next number
	range n to m -
    step number "10", "12"
    not a step number "11" (1 not one step to 1), "13" (1 not one step to 3)
	"""

    def permutateStepNums(self, max):
        """
        permutate step numbers
        start with 10 up to n
        e.g. 10, 12, 21, 23
        10,20..
        """

        int_len = len(str(abs(int(max))))
        range_len = int_len

        ret_build = [0,1,2,3,4,5,6,7,8,9] # range(10)
        lst_build = ret_build
        for i in range(0, range_len - 1):
            tmp_build = []
            for j in lst_build:
                if j > 0:
                    chk_dig = j % 10
                    if chk_dig > 0:
                        str_num = str(j) + str(chk_dig - 1)
                        the_num = int(str_num)
                        tmp_build.append(the_num)
                    if chk_dig < 9:
                        str_num = str(j) + str(chk_dig + 1)
                        the_num = int(str_num)
                        tmp_build.append(the_num)

            lst_build = tmp_build
            ret_build += tmp_build

        return ret_build

    def stepping_number(self, n, m):

        lst_stepnums = self.permutateStepNums(m)
        print "lst_stepnums:", lst_stepnums
        ret_stepnums = []
        for i in lst_stepnums:
            if i >= n and i <= m:
                ret_stepnums.append(i)

        return ret_stepnums

# stepping_number = steppingNumber()
# print "steps:", stepping_number.stepping_number(10, 200)

class prefixString:

    def prefix_string(self, A):

        """
        Trie!
        Input:  'zeb', 'zub'
        Output: [2, {'z': [2, {'u': [1, {'b': [1, {}]}], 'e': [1, {'b': [1, {}]}]}]}]
        """

        # whole word: tree[dup count, whole word, subnodes]
        tree = [0, False, {}]
        for s in A:
            node = tree
            node[0] += 1  # number of words
            for c in s:
                node = node[2].setdefault(c, [0, False, {}])
                node[0] += 1
            else:
                node[1] = True

        l = []
        for s in A:
            prefix = ''
            node = tree # start at top of tree
            for c in s:
                prefix += c
                node = node[2][c]
                if node[1] == True: # whole word found!
                    l.append(prefix)

        return l

        # duplicate count: tree[dup count, subnodes]
        # tree = [0, {}]
        # for s in A:
        #     node = tree
        #     node[0] += 1  # number of words
        #     for c in s:
        #         node = node[1].setdefault(c, [0, {}])
        #         node[0] += 1

        # l = []
        # for s in A:
        #     prefix = ''
        #     node = tree # start at top of tree
        #     for c in s:
        #         if node[0] <= 1: # if only one word or smallest prefix
        #             l.append(prefix)
        #             break
        #         prefix += c
        #         node = node[1][c]
        #     #else:
        #     #    l.append(s)
        # return l

# prefix_string = prefixString()
# print prefix_string.prefix_string(['zeb','zub'])
# print prefix_string.prefix_string([' '])
#print prefix_string.prefix_string(['zebra', 'dog', 'duck', 'dove'])
#print prefix_string.prefix_string(["fwkho", "kmcoqhnw", "kuewhsqmgb", "uqcljj", "vsw", "dkqtbxi"])

class colorfulNumber:
    """
    @param A : integer
    @return an integer

    A number can be broken into different contiguous sub-subsequence parts.
    Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
    And this number is a COLORFUL number, since product of every digit of a
    contiguous subsequence is different

    N = 23
    2 3 23
    2 -> 2
    3 -> 3
    23 -> 6
    this number is a COLORFUL number since product of every digit of a sub-sequence are different.

    Output : 1

    Thoughts: number cannot be longer than 8 digits since it can't contain the
    same digit, else it won't be colorful
    e.g., the largest number would be: 98765432
    so that narrows down how much time/space we're gonna need
    Also, anything next to a 0,1 won't count since 0=0 & 0*5=0; 5=5 & 1*5=5 etc..
    although,

    Initially, look to see if number has duplicate digits

    could probably store results in a hash, if any collisions then it's not colorful

    1234
    1,2,3,4,12,23,34,123,234,1234
    """

    from functools import reduce
    import operator

    def multiplyList(self, n):
        """
        product of list n
        product([1,2,3]) -> 6
        """
        if not n:
            return 0
        if type(n) is not list:
            return 0
        return reduce(self.operator.mul, n, 1)

    def colorful_number(self, A):

        if type(A) is not int:
            #print "Error - number is not an int"
            return False
        if len(str(abs(A))) > 8:
            #print "Error - number too large"
            return False

        i = A
        p = [] # list of products
        d = [] # list of digits

        # single digit, build list for easy access
        while i:
            digit = i % 10
            # if digit == 0:
            #     #print "Error - has a 0 in it"
            #     return False
            # if digit == 1:
            #     #print "Error - has a 1 in it"
            #     return False
            i = i / 10
            if digit in p:
                #print "Error - duplicate.", p
                return False
            else:
                p.append(digit)
                d.append(digit)

        # multiple digits
        look = 2
        t = [] # tracking the rest of combined digits.. for fun?
        while look <= len(d):
            for i in range(0, len(d)):
                r_s = i # range: start
                r_e = i + look  # range: end
                if r_e <= len(d):
                    # get product of range, add to hash (if possible)
                    digit = d[r_s:r_e]
                    digit_product = self.multiplyList(digit)
                    if digit_product in p:
                        #print "Error - duplicate.", p
                        return False
                    else:
                        p.append(digit_product)
                        t.append(digit)
                else:
                    break
            look += 1

        # print "p:", p
        # print "d:", d
        # print "t:", t

        return True

# colorful_number = colorfulNumber()
# print colorful_number.colorful_number(2342)

## Square of 2
## binary 001 = 1, 010 = 2
## 100 = 4 & 011 = 3 = 0 = True
class powerOf2:

    def power_of_2(self, A):
        """
        @param A : string
        @return an integer

        devise a way a number is a power of 2

        could use log base 2 math.log(128, 2) - would return float
        would then need to compare with float - int however precision is lacking
        so the results will be wacky

        could divide number by 2 until less or equal to 2 (or whatever number you fancy)


        using binary: this will only work for powers of 2
        since this is only a power of 2 could use binary. num will have to larger than 2
        since binary is represented as 1,2,4,8,16 etc..
        with 128=10000000 and 127=01111111, doing an & op would result in 0 if a power of 2
        """
        try:
            A_int = int(A)
        except:
            return 0
        if A_int < 2:
            return 0

        # Binary Method
        # if not A_int & (A_int - 1):
        #     return 1
        # return 0

        ## Division method
        while A_int >= 2:
            if A_int == 2:
                return 1
            A_int /= 2
        return 0

# power_of_2 = powerOf2()
# print power_of_2.power_of_2("127")

class gcd:
    def gcd(self, m, n):
        """
        Find greatest common divisor of m and n
        The largest int that divides into n and m

        e.g. m=6, n=9: gcd is 3

        Initial thoughts:

           find smallest of n and m
           if smallest is even, divide by 2 then check other
           if smallest is odd, divide by 3 then check other
           Note: this won't work at all.. 5/3 = 1.66666 - no good

           Primary numbers involved somehow ?
           2,3,5,7,11,13...

           5, 10 = 5
           2, 8 = 2
           15, 21 = 3  ->
           11, 22 = 11 -> 22 % 11 = 0 .. 11

        """
class gcd:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def sv_primes(self,n):
        """
        find primes up to n and return list
        """
        sv = [True] * (n+1)
        for i in xrange(3, int(n**0.5) + 1, 2):
            if sv[i]:
                for j in xrange(i*i, n, 2*i):
                    sv[j] = False
        return [2] + [i for i in xrange(3, n+1, 2) if sv[i]]

    def gcd(self, A, B):

        """
         Streamlined solution

            m = g * m1
            n = g * m2

            m - n = g * (m1 - m2)

            gcd (m, n) = gcd(m-n, n)
        """
        print A, B
        # if (B == 0):
		#     return A
        # else:
		#     return self.gcd(B, A%B)

        while A != B:
            if A > B:
                if B == 0:
                    break
                A = A - B
            else:
                if A == 0:
                    A = B
                    break
                B = B - A
        return A

        ## Brute Force
        if A == 0:
            return B
        if B == 0:
            return A
        gcd = []
        for i in xrange(1, min([A, B]) + 1):
            if not A % i and not B % i:
                gcd.append(i)
        if gcd:
            return max(gcd)
        else:
            return 0

        ## Using Primes - I don't think this is the way to go
        # gcd = [1]
        # tst = [A, B]
        #
        # if A == 1 or B == 1:
        #     return 1
        #
        # if A == B:
        #     return A
        #
        # # find primes of smaller number
        # primes = self.sv_primes(min(tst))
        # #print "primes of {}:{}".format(min(tst), primes)
        #
        # for p in primes:
        #     if A % p == 0 and B % p == 0:
        #         gcd.append(p)
        #
        # #print "gcd:{}".format(gcd)
        # if gcd:
        #     return(max(gcd))
        # else:
        #     return 0

# gcd = gcd()
# print gcd.gcd(114, 671) ## 1
# print gcd.gcd(672, 114) ## 6
# print gcd.gcd(2, 8)     ## 2
# print gcd.gcd(0, 1)     ## 1

class wave:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):

        # sort the array
        A.sort()

        ret = []

        for i in xrange(0, len(A), 2):

            # swap first and second
            print i + 1
            # e.g. [1,2,3,4,5] - if i+1(5) < len(5) "i is 1,2,3 or 4"
            #       0 1 2 3 4
            if i + 1 < len(A):
                ret.append(A[i + 1])
            ret.append(A[i])

        return ret

# wave = wave()
# wave.wave([5,4,3,2,1])

class maxSet:

    def max_set(self, A):

        tmp = []
        sub = []

        for i in A:
            if i >= 0:
                tmp.append(i)
            else:
                if tmp:
                    sub.append(tmp)
                    tmp = []
        if tmp:
            sub.append(tmp)

        print sub

# max_set = maxSet()
# print max_set.max_set([1,5,7,8,-9,2,1,-5,3])
# print max_set.max_set([1,2,5,-1,2,5,1])

class squareSum:
    """
    param A : integer
    return a list of list of integers
    """
    def square_sum(self, A):
        # check A validity - per rules
        if A < 0 or A > 100000:
            return [0,0]

        ans = []
        a = 0
        while a * a < A:
            # a <= b therefore b starts at a
            b = a
            while b * b < A:
                print a, b
                if a * a + b * b == A:
                    newEntry = [a, b]
                    ans.append(newEntry)
                b += 1
            a += 1
        return ans

# square_sum = squareSum()
# print square_sum.square_sum(8)

class node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class traverseZigZag:

    def build_tree(self):
        """
        Test Tree:
            3
           / \
          9  20
            /  \
           15   7
        """
        root = node(3)
        root.left = node(9)
        root.right = node(20)
        root.right.left = node(15)
        root.right.right = node(7)
        return root

    def build_tree_2(self):
        root = node(1)
        root.left = node(1)
        return root

    def traverse_zig_zag(self, A):
        """
        A is the root note

        zig zag appears to be a 'stack' left & right
        then visit right, left children
        to flip order queue and visit sub-left&right
        """
        ret = []
        mode = "queue"
        queue = [A]
        next_nodes = []
        visited = []

        while queue:

            node = queue.pop(0)
            visited.append(node.val)

            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

            # queue is empty, refill!
            if not queue:

                # last minute cleanup
                if mode == "stack":
                    ret.append([visited[i] for i in xrange(len(visited) - 1, -1, -1)])
                else:
                    ret.append([i for i in visited])
                visited = []

                queue += next_nodes
                next_nodes = []

                # zig when you should zag
                if mode == "stack":
                    mode = "queue"
                else:
                    mode = "stack"

        return ret

# traverse_zig_zag = traverseZigZag()
# root = traverse_zig_zag.build_tree()
# print traverse_zig_zag.traverse_zig_zag(root)

class symmetricTree:

    def build_tree_1(self):
        """
        Test Tree: is symmetrical
                1
               / \
              2   2
             / \ / \
            3  4 4  3
        """
        root = node(1)
        root.left = node(2)
        root.right = node(2)
        root.left.left = node(3)
        root.left.right = node(4)
        root.right.left = node(4)
        root.right.right = node(3)
        return root

    def build_tree_2(self):
        """
        Test Tree: is NOT symmetrical
                1
               / \
              2   2
               \   \
                3   3
        """
        root = node(1)
        root.left = node(2)
        root.right = node(2)
        root.left.right = node(3)
        root.right.right = node(3)
        return root

    def in_order_traverse(self, n, l):
        if n is not None:
            self.in_order_traverse(n.left, l)
            l += [n.val]
            self.in_order_traverse(n.right, l)

    def symmetric_tree(self, A):
        """
        Symmetric - same for both left and right side
        start @ left and right node - traverse down and compare
        using a bfs via queue to go wide
        """

        if not A:
            return 0

        ll = []
        lr = []

        # base case, only root node
        if not A.left and not A.right:
            return 1

        # start two tree comparison
        if A.left:
            self.in_order_traverse(A.left, ll)
        if A.right:
            self.in_order_traverse(A.right, lr)

        if len(ll) != len(lr):
            return 0
        for i in range(0, len(ll)):
            if ll[i] != lr[(len(ll) - 1) - i]:
                return 0
        return 1

# symmetric_tree = symmetricTree()
# root = symmetric_tree.build_tree_1()
# print symmetric_tree.symmetric_tree(root)
# root = symmetric_tree.build_tree_2()
# print symmetric_tree.symmetric_tree(root)

class leafPaths:

    def build_tree_1(self):
        """
        Test Tree: [12+13]%1003 = 25
                1
               / \
              2   3
        """
        root = node(1)
        root.left = node(2)
        root.right = node(3)
        return root

    def build_tree_2(self):
        """
        Test Tree: [12+1345]=1357%1003=354
                1
               / \
              2   3
                 /
                4
                 \
                  5
        """
        root = node(1)
        root.left = node(2)
        root.right = node(3)
        root.right.left = node(4)
        root.right.left.right = node(5)
        return root

    def build_tree_3(self):
        """
        Test Tree: [12]=12%1003=12
                1
                 \
                  2
        """
        root = node(1)
        root.right = node(2)
        return root

    def leaf_paths_utility(self, node, ans=0):
        digit,num = node
        num = num*10 + digit.val
        if (digit.left):
            ans = self.leaf_paths_utility([digit.left, num], ans)
        if (digit.right):
            ans = self.leaf_paths_utility([digit.right, num], ans)
        if (not digit.left and not digit.right):
            ans += num%1003
        return ans%1003

    def leaf_paths(self, A):
        if A == None:
            return 0
        stack = [A, 0]
        return self.leaf_paths_utility(stack)

    # def leaf_paths(self, A):
    #
    #     if root == None:
    #         return 0
    #     sum = 0
    #     ans = 0
    #     stack = [[root,0]]
    #     while(stack):
    #         digit,num = stack.pop()
    #         num = num*10 + digit.val
    #         if (digit.left):
    #             stack.append([digit.left,num])
    #         if (digit.right):
    #             stack.append([digit.right,num])
    #         if (not digit.left and not digit.right):
    #           ans += num%1003
    #     return ans%1003

        # """
        # find paths to leafs
        # each path will become a number e.g., [0,1,2,3] -> 123
        # sum paths numbers and mod with 1003 ?
        # assuming numbers are 0 to 9 only
        #
        # example:
        # The root-to-leaf path 1->2 represents the number 12.
        # The root-to-leaf path 1->3 represents the number 13.
        #
        # Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
        # Note: not sure why it's modding a modded sum ? - perhaps will have to mod * number of paths ?
        # """
        #
        # # Using DFS to find paths, iteratively
        # root = A
        # stack = [[A]] # stack, stored as path(s)
        # node = None
        # path = []
        # paths = []
        #
        # while stack:
        #
        #     path = stack.pop()
        #     node = path[-1]
        #
        #     if path and node.left is None and node.right is None:
        #         paths.append(path)
        #
        #     if node.left:
        #         new_path = list(path)
        #         new_path.append(node.left)
        #         stack.append(new_path)
        #
        #     if node.right:
        #         new_path = list(path)
        #         new_path.append(node.right)
        #         stack.append(new_path)
        #
        # # so.. now, we need to make numbers out of those paths
        # # lets make a list of numbers.. why not indeed
        # num = '' # it's a string - can't concat integers 'easily'
        # nums = []
        # for i in paths:
        #     for j in i:
        #         num += str(j.val)
        #     nums.append(int(num))
        #     num = ''
        #
        # print "sum of nums {} is {} mod 1003 is {}".format(nums, sum(nums), sum(nums)%1003)
        #
        # return sum(nums)%1003


# leaf_paths = leafPaths()
# root = leaf_paths.build_tree_3()
# print leaf_paths.leaf_paths(root)

class valInRange:

    def bs_min(self, a, val):
        if not a or not val:
            return -1
        min = 0
        max = len(a) - 1
        res = -1
        while min <= max:
            mid = (min + max) // 2
            if a[mid] == val:
                res = mid
                max = mid - 1 # [<--]
            elif a[mid] < val:
                min = mid + 1
            else:
                max = mid - 1
        return res

    def bs_max(self, a, val):
        if not a or not val:
            return -1
        min = 0
        max = len(a) - 1
        res = -1
        while min <= max:
            mid = (min + max) // 2
            if a[mid] == val:
                res = mid
                min = mid + 1 # [-->]
            elif a[mid] < val:
                min = mid + 1
            else:
                max = mid - 1
        return res

    def val_in_range(self, A, B):
        """
        find min and max index of value in a sorted array in logn time
        note: use binary search to find a min and max index
        if value not found, return [-1,-1] else [idx, idx]
        """
        min_idx = self.bs_min(A, B)
        max_idx = self.bs_max(A, B)
        return [min_idx, max_idx]

# val_in_range = valInRange()
# print val_in_range.val_in_range([1,5,6,8,8,8,9,10,20,21], 8) # should be [3, 5]
# print val_in_range.val_in_range([1,5,6,8,8,8,9,10,20,21], 7) # not found! [-1, -1]

class flipBits:

    def flip_bits(self, A):
        """
        unsigned int, 2^31 bits (2147483648 numbers)
        remember in python that ints are big-ints, 64 bit
        """

        i = 31
        ret = 0
        while i >= 0:
            temp = ((A & 1<<i) >> i)&1
            print temp
            ret = ret | temp << (31-i)
            print bin(ret)
            i -= 1
        return ret

        # Try # 2 - just loop through and write out mirrored number
        # num = ''
        # for i in xrange(0, 32):
        #     if A & (1<<i) > 0:
        #         num += '1'
        #     else:
        #         num += '0'
        # return int(num, 2)

        # # get index of largest 1
        # hi_idx = None
        # for i in xrange(0, 32):
        #     if A & (1<<i) > 0:
        #         hi_idx = i
        #
        # # grab only first 32 in case number is larger than 2**31
        # num = ''
        # for i in xrange(31, -1, -1):
        #     if A & (1<<i) > 0:
        #         num += '1'
        #     else:
        #         num += '0'
        # num_A = int(num, 2)
        #
        # if hi_idx is not None:
        #     # xor 1's up to hi_idx
        #     # subtract result to create mirror
        #     # shift to end - hi_idx
        #     mask = int('1' * (hi_idx + 1), 2)   # 1101 mask is 1111
        #     xor = num_A^mask                    # 1101^1111 -> 0010(2)
        #     rev = num_A - xor                   # 13-2=11 -> 1011
        #     mirror = rev<<31-hi_idx
        #
        #     print "hi_idx:{}".format(hi_idx)
        #     print "num_A:", num_A, " ", bin(num_A)
        #     print "mask:", mask, " ", bin(mask)
        #     print "xor:", xor, " ", bin(xor)
        #     print "rev:", rev, " ", bin(rev)
        #     print "mirror:", mirror, " ", bin(mirror)
        #     return mirror
        # else:
        #     print "mirror: 0"
        #     return 0

#flip_bits = flipBits()
# print flip_bits.flip_bits(0)
#print flip_bits.flip_bits(13) # 1101
# print flip_bits.flip_bits(1)
#print flip_bits.flip_bits(4294967294)

class versionNumber:

    def version_number(self, A, B):
        """
        Compare two version numbers version1 and version2.

        If version1 > version2 return 1,
        If version1 < version2 return -1,
        otherwise return 0.
        You may assume that the version strings are non-empty and contain only digits and the . character.
        The . character does not represent a decimal point and is used to separate number sequences.
        For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

        Here is an example of version numbers ordering:

        0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

        Initial thoughts:
        split by <, then . - put each sub split into sub-lists [[],[]] then compare sums

        would this really just be a min heap ? - time would be O(logn) to insert elements
        """
        if not A:
            return 0

        sub_a = []
        for j in A.split("."): # a list of numbers in a version
            sub_a.append(int(j))

        sub_b = []
        for j in B.split("."): # a list of numbers in a version
            sub_b.append(int(j))

        # case when 1.0 == 1 !! - this one isn't working
        # case when 2.0 > 1.094784728929874987
        # case when 13.0 < 13.08

        # remove end zeros
        while True:
            if sub_a[-1] == 0:
                sub_a.pop()
            else:
                break
        while True:
            if sub_b[-1] == 0:
                sub_a.pop()
            else:
                break

        # compare versions
        if sub_a > sub_b:
            return 1
        elif sub_a < sub_b:
            return -1
        else:
            return 0

# version_number = versionNumber()
# print version_number.version_number("13.0", "13.0.8"), "'-1'"
# print version_number.version_number("1.0", "1"), "'0'"
# print version_number.version_number("643443896946", "2.487969654569425698"), "'1'"

class ipAddress:

    def ip_address(self, A):
        """
        Given a string containing only digits, restore it by returning all possible valid IP address combinations.

        A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

        Example:

        Given "25525511135"

        return ["255.255.11.135", "255.255.111.35"]. (Make sure the returned strings are sorted in order)

        thoughts:

        first number can only start with 1 or 2 if 3 long
                                         1,2,3,4,5 if less then 3 long
        last two numbers can only be max of 5
        """
        # opt = []
        # for i in xrange(0, len(A)):
        #     # @ digit
        #     sub = []
        #     for j in xrange(1, 4):
        #         # loopin' 3 times
        #         # no zeros as prefix
        #         # e.g. 01 but not just 0 hence j greater than 1
        #         if j > 1 and A[i] == '0':
        #             continue
        #         num = int(A[i:i+j])
        #         # number less than 255
        #         if num <= 255:
        #             sub.append([A[i:i+j]])
        #     opt.append(sub)
        #
        # for i in xrange(0, len(opt)):
        #     # each sub number
        #     #print i, opt[i]
        #     pass

        # try 2 .. four for loops
        # time is crap for this O(n^4) however, only dealing with 12 numbers
        # 80 total loops.. I mean, unless this ip was approaching infinity then we'd have an issue
        print "len.A:", len(A)
        opt = []
        tmp = ''
        for i in xrange(1, 4):
            for j in xrange(1, 4):
                for k in range(1, 4):
                    for l in range(1, 4):

                        # convert to int, this will remove leading zeros
                        oct1 = A[0:i]
                        oct2 = A[i:i+j]
                        oct3 = A[i+j:i+j+k]
                        oct4 = A[i+j+k:i+j+k+l]

                        if oct1 and oct2 and oct3 and oct4:
                            oct1 = int(oct1)
                            oct2 = int(oct2)
                            oct3 = int(oct3)
                            oct4 = int(oct4)
                        else:
                            continue

                        if oct1 > 255 or oct2 > 255 or oct3 > 255 or oct4 > 255:
                            continue

                        tmp = str(oct1) + "." + str(oct2) + "." + str(oct3) + "." + str(oct4)
                        print tmp

                        # compare lengths
                        if len(tmp) == len(A) + 3 and tmp not in opt:
                            opt.append(tmp)

        print opt

# ip_address = ipAddress()
# #print ip_address.ip_address("25525511135")
# print ip_address.ip_address("127001")

class zigZagText:

    def zig_zag_text(self, A, B):
        """
        Runtime O(n), Space O(n)

        ABCDE, 2 -> ACEBD
        A   C   E
          B   D

        ABCDEF, 3 -> ADBEC
        A     D
          B     E
            C

        PAYPALISHIRING, 2 -> PYAIHRN APLSIIG
        P   Y   A   I   H   R   N
          A   P   L   S   I   I   G

        PAYPALISHIRING, 3 -> PAHN APLSIIG YIR
        P       A       H       N
          A   P   L   S   I   I   G
            Y       I       R

        PPIINAASRGYLHI
        """
        skip = B
        if skip == 0:
            return ''
        if skip == 1:
            return A

        sub = []
        for i in xrange(0, skip):
            sub.append([])

        idx = 0
        dir = 1
        for i in xrange(0, len(A)):
            sub[idx].append(A[i])
            if idx == skip - 1:
                dir = -1
            if idx == 0:
                dir = 1
            idx += dir

        ret = ''
        for i in sub:
            for j in i:
                ret += j

        return ret


# zig_zag_text = zigZagText()
# print zig_zag_text.zig_zag_text(['A','B','C','D','E'], 2)
# print zig_zag_text.zig_zag_text(['A','B','C','D','E','F'], 2)
# print zig_zag_text.zig_zag_text(['A','B','C','D','E'], 3)
# print zig_zag_text.zig_zag_text(['A','B','C','D','E','F'], 3)

# print zig_zag_text.zig_zag_text("PAYPALISHIRING", 3)
# print zig_zag_text.zig_zag_text("PAYPALISHIRING", 2)

# print zig_zag_text.zig_zag_text("0123456", 1)
# print zig_zag_text.zig_zag_text("0123456", 2)
# print zig_zag_text.zig_zag_text("0123456", 3)
# print zig_zag_text.zig_zag_text("0123456789", 4)

# Test 5

class lastWord:

    def last_word(self, A):
        """
        Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

        If the last word does not exist, return 0.

        Note: A word is defined as a character sequence consists of non-space characters only.

        Example:

        Given s = "Hello World",

        return 5 as length("World") = 5.

        Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.
        """
        count = 0
        space = False
        for c in A:
            if c == ' ':
                space = True
            else:
                if space:
                    count = 1
                    space = False
                else:
                    count += 1
        return count

# last_word = lastWord()
# print last_word.last_word("")
# print last_word.last_word("a")
# print last_word.last_word("Hello World")
# print last_word.last_word("supercalifragilisticexpialidocious")

class fileJSON:

    def file_json(self):
        """
        Read a file (json in this case)

        The with statement handles opening and closing the file,
        including if an exception is raised in the inner block.

        The for line in f treats the file object f as an iterable,
        which automatically uses buffered IO and memory management
        so you don't have to worry about large files.
        """

        import json
        from pprint import pprint

        with open('data.json') as data_file:
            # for line in data_file:
            #     print line
            # decode file like object, stream etc..
            data = json.load(data_file)

        pprint(data)

        data["maps"][0]["id"]
        data["masks"]["id"]
        data["om_points"]

        ## decode string
        data = json.loads('{"a":1, "b":2}')
        print data["a"], data["b"]

# file_json = fileJSON();
# file_json.file_json()

class removeElemInArray:

    def remove_elem_in_array(self, A, B):
        """
        Remove Element

        Given an array and a value, remove all the instances of that value in the array.
        Also return the number of elements left in the array after the operation.
        It does not matter what is left beyond the expected length.

        Example:
        If array A is [4, 1, 1, 2, 1, 3]
        and value elem is 1,
        then new length is 3, and A is now [4, 2, 3]
        Try to do it in less than linear additional space complexity.

        going to swap positions, keep track of two pointers
        not sure what it means 'does not matter what is left beyond expected length.. ? does this factor into design ?'
        """

        # # less than linear extra space, ret will be all values less B
        # ret = []
        #
        # for i in xrange(0, len(A)):
        #     if A[i] != B:
        #         ret.append(A[i])
        #
        # return ret

        # j = -1
        # i = 0
        #
        # while True:
        #
        #     if i == len(A):
        #         break
        #
        #     # set swap index
        #     if A[i] == B and j == -1:
        #         j = i
        #
        #     # need to swap where B not found
        #     if A[i] != B and j != -1:
        #         A[j], A[i] = A[i], A[j]
        #         i = j
        #         j = -1
        #
        #     i += 1
        #
        # for i in xrange(0, len(A)):
        #     if A[-1] == B:
        #         A.pop()
        #     else:
        #         break

        # [2,1,0,3,2]
        # [1,2,0,3,2]
        j = 0
        for i in xrange(0, len(A)):
            #print A
            if A[i] != B:
                A[i], A[j] = A[j], A[i]
                j += 1

        print "len:", j, "A:", A[:j]

# remove_elem_in_array = removeElemInArray()
# test = [2,0,1,2,0,3,2,2,2,1,0,0,0,1,0,0,2,2,2,3,2,3,1,2,1,2,2,3,2,3,0,3,0,2,1,2,0,0,3,2,3,0,3,0,2,3,2,2,3,1,3,3,0,3,3,0,3,3,2,0,0,0,0,1,3,0,3,1,3,1,0,2,3,3,3,2,3,3,2,2,3,3,3,1,3,2,1,0,0,0,1,0,3,2,1,0,2,3,0,2,1,1,3,2,0,1,1,3,3,0,1,2,1,2,2,3,1,1,3,0,2,2,2,2,1,0,2,2,2,1,3,1,3,1,1,0,2,2,0,2,3,0,1,2,1,1,3,0,2,3,2,3,2,0,2,2,3,2,2,0,2,1,3,0,2,0,2,1,3,1,1,0,0,3,0,1,2,2,1,2,0,1,0,0,0,1,1,0,3,2,3,0,1,3,0,0,1,0,1,0,0,0,0,3,2,2,0,0,1,2,0,3,0,3,3,3,0,3,3,1,0,1,2,1,0,0,2,3,1,1,3,2]
# test = [2,1,0,3,2]
# test = [1,2,0,3,2]
# test = [2,0,1,2,0,3,2,2,2,1,0,0,0,1,0,0,2,2,2,3,2,3]
# print remove_elem_in_array.remove_elem_in_array(test, 2)

class removeDupsArray:

    def remove_dups_array(self, A):
        """
        Remove Duplicates from Sorted Array

        Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

        Do not allocate extra space for another array, you must do this in place with constant memory.

        Note that even though we want you to return the new length, make sure to change the original array as well in place

        For example,
        Given input array A = [1,1,1,2],
                              [1,1,1,2,2,3,3,3,4]

        Your function should return length = 3, and A is now [1,1,2]

        There will be a lot of shifting elems to the end and tracking how many to remove
        """

        if not A:
            return None

        cur_val = None
        cur_cnt = 0
        j = 0

        ## This works, O(n) time = good
        for i in xrange(0, len(A)):

            if cur_val == A[i]:
                cur_cnt += 1
            else:
                cur_val = A[i]
                cur_cnt = 1

            # swap when i and j are out of sync
            if i > j:
                A[i], A[j] = A[j], A[i]

            if cur_cnt <= 2:
                j += 1

            #print "i:", i, "j:", j, " cur_cnt:", cur_cnt, A

        self.pop_end(A, j - 1)

        return A

        ## This works, O(n^2) = bad
        # i = 0
        # cur_val = None
        # cur_val_count = 0
        #
        # while i < len(A):
        #
        #     print i, A
        #
        #     # base case
        #     # in: [0,1,1,2,3,1,1] when 1 < 3 break @ idx:5
        #     # when second to last, if equal to end break out or loop will occur
        #     if (A[i] < cur_val or
        #         ((i == len(A) - 2) and A[i] == A[-1])):
        #         break
        #
        #     # keeping track of times value exists
        #     if A[i] == cur_val:
        #         cur_val_count += 1
        #     else:
        #         cur_val = A[i]
        #         cur_val_count = 1
        #
        #     # increment counter
        #     if cur_val_count > 2:
        #         self.push_to_end(A, i)
        #     else:
        #         i += 1
        #
        # self.pop_end(A, i - 1)
        #
        # return A

    def push_to_end(self, A, i):
        """
        push index i to end of array A
        [1,2,3,3,3,4,5,6]
        """
        while i + 1 <= len(A) - 1:
            A[i], A[i + 1] = A[i + 1], A[i]
            i += 1
        return A

    def pop_end(self, A, B):
        """
        Since array is sorted, we can remove all values less than prev
        e.g. 1,2,3,4,1,2,2 .. everything right of index 4 in this case
        """
        # remove end up to pop-index minus length
        # for 1,1,1,1,1,1 - pop-index is 1, range 0,4 -> 0,1,2,3 = 4 pops
        for i in xrange(0, (len(A) - 1) - B):
            # if all numbers the same, save the last two!
            if len(A) >= 2:
                A.pop()
        return A

# remove_dups_array = removeDupsArray()
# print remove_dups_array.remove_dups_array([0])
# print remove_dups_array.remove_dups_array([1,1,1,2])
# print remove_dups_array.remove_dups_array([0, 1, 1, 2, 2, 3, 3, 3, 3])
# print remove_dups_array.remove_dups_array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])
# print remove_dups_array.remove_dups_array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])
# print remove_dups_array.remove_dups_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])

class chessBoard:

    ## FB Interview question #2

    mem_point = {}
    mem_collide = {}
    mem_outofrange = {}     # memoized: points out of range
    mem_visited = {}        # places we've already moved to

    def get_moves(self, point=(-1,-1), pawns=[]):
        """
        return all moves a piece can make
        """
        points = {}
        x = point[0]
        y = point[1]

        if (x, y) in self.mem_point:
            #print "hit mem_point @ {}".format((x, y))
            for i in xrange(0, 8):
                points[i] = self.mem_point[(x, y)][i] # Points (x,y),(x,y) etc..
            return points

        points[0] = (x+2, y+1)
        points[1] = (x+2, y-1)
        points[2] = (x-2, y+1)
        points[3] = (x-2, y-1)
        points[4] = (x+1, y+2)
        points[5] = (x-1, y+2)
        points[6] = (x+1, y-2)
        points[7] = (x-1, y-2)

        # memoize
        self.mem_point[(x, y)] = [points[i] for i in points]

        return points

    def move_collision(self, start, end, pawns=[]):
        """
        Check if path plows through pawns somehow
        return True or False

        Note: no need to check end move (the hook)
              since returned from get_move will be the end move
              and that is checked in the main function
        """
        x_1 = start[0]
        y_1 = start[1]
        x_2 = end[0]
        y_2 = end[1]

        if (x_1, y_1, x_2, y_2) in self.mem_collide:
            #print "hit mem_collide @ points {}, {}".format((x_1, y_1), (x_2, y_2))
            return self.mem_collide[(x_1, y_1, x_2, y_2)] # True or False

        ret = None # track True or False to end for memoization
        if abs(x_2 - x_1) > abs(y_2 - y_1):
            # x is larger - move x first
            # (1,1) -> (3,2)
            # (3,2) -> (1,1)
            if x_1 > x_2:
                if (x_1 - 1, y_1) in pawns:
                    ret = True
                if (x_1 - 2, y_1) in pawns:
                    ret = True
            else:
                if (x_1 + 1, y_1) in pawns:
                    ret = True
                if (x_1 + 2, y_1) in pawns:
                    ret = True
        else:
            # y is larger - move y first
            if y_1 > y_2:
                if (x_1, y_1 - 1) in pawns:
                    ret = True
                if (x_1, y_1 - 2) in pawns:
                    ret = True
            else:
                if (x_1, y_1 + 1) in pawns:
                    ret = True
                if (x_1, y_1 + 2) in pawns:
                    ret = True

        if ret:
            self.mem_collide[(x_1, y_1, x_2, y_2)] = True
            return True
        self.mem_collide[(x_1, y_1, x_2, y_2)] = False
        return False

    def move_out_of_range(self, start, target, point):
        """
        Checking to see if point is getting too far out of range
        range will be a distance multipled from start to target (arbitrary)
        ** note: there might be an actual way to calculate the best out of range.. for now, this is it

        start = original start
        target = original target
        point = point being tested - the 'move'
        """

        distance_multiplier = 2

        # calculate four corners of 'box'

        # x, y of points
        x_1 = start[0]
        y_1 = start[1]
        x_2 = target[0]
        y_2 = target[1]
        x_p = point[0]
        y_p = point[1]

        if (x_p, y_p) in self.mem_outofrange:
            #print "hit mem_collide @ points {}, {}".format((x_1, y_1), (x_2, y_2))
            return self.mem_outofrange[(x_p, y_p)] # True or False

        # distance x, y .. start to target
        # calculating 1/4th extra padding for all sides
        d_x = abs(x_1 - x_2) * distance_multiplier // 4
        d_y = abs(y_2 - y_2) * distance_multiplier // 4

        if x_1 > x_2:
            x_l = x_2 - d_x
            x_r = x_1 + d_x
        else:
            x_l = x_1 - d_x
            x_r = x_2 + d_x

        if y_1 > y_2:
            y_t = y_1 + d_y
            y_b = y_2 - d_y
        else:
            y_t = y_2 + d_y
            y_b = y_1 - d_y

        ret = None

        if x_p < x_l or x_p > x_r:
            ret = True
        if y_p < y_b or y_p > y_t:
            ret = True

        # if ret:
        #     print "point:({},{}) target:({},{}) NOT in bounds of ({},{}),({},{}),({},{}),({},{})".format(x_p, y_p, x_2, y_2, x_l, y_t, x_r, y_t, x_l, y_b, x_r, y_b)
        # else:
        #     print "point:({},{}) target:({},{}) in bounds of ({},{}),({},{}),({},{}),({},{})".format(x_p, y_p, x_2, y_2, x_l, y_t, x_r, y_t, x_l, y_b, x_r, y_b)

        if ret:
            self.mem_outofrange[(x_p, y_p)] = True
            return True
        self.mem_outofrange[(x_p, y_p)] = False
        return False

    def chess_board(self, start, target, pawns=[]):
        """
        basic dfs for a grid'like' structure
        find path from start to target, this class does not allow to jump over pawns
        start = point(x,y)
        target = point(x,y) - goal
        pawns = list of points(x,y)
        """

        q = [[start]]
        path = []
        paths = []

        while q:

            path = q.pop(0)
            point = path[-1]
            #print q

            if point == target:
                paths.append(path)
                # only need to find one path, break out.. otherwise keep looking
                break

            # get moves
            # returning dict {0:(1,2),1:(2,2),etc..}
            moves = self.get_moves((point[0], point[1]))

            for move in [moves[i] for i in moves]:

                # skip adding to path when:
                # move has already been visited
                # move is a pawn
                # point to move travels over a pawn spot
                if (move in self.mem_visited or
                    move in pawns or
                    self.move_collision(point, move, pawns) or
                    self.move_out_of_range(start, target, move)):
                    continue

                self.mem_visited[move] = True

                new_path = list(path)
                new_path.append(move)
                q.append(new_path)

        if paths:
            print "paths:", paths, "length:", len(paths[0])
            print "points:{} collisions:{} outofrange:{} visited:{}".format(len(self.mem_point), len(self.mem_collide), len(self.mem_outofrange), len(self.mem_visited))
        else:
            print "no paths found"

# chess_board = chessBoard()
# chess_board.chess_board((5,5), (10,10), [])
# chess_board.chess_board((5,5), (12,22), [])
# chess_board.chess_board((-20,-20), (500,500), [(10,11),(10,9),(9,10),(10,12),(10,13),(10,8),(10,7)])

class maxArea:

    def remove_element(self, A, i):
        pass

    def max_area(self, A):

        # O(n^2), no bueno
        # per the **hint, get rid of min value in a1-an
        del(A[A.index(min(A))])
        max = 0
        for i in xrange(0, len(A)):
            mult = 0
            for j in xrange(i + 1, len(A)):
                mult += 1
                next = min(A[i], A[j]) * mult
                if next > max:
                    max = next
        return max

# max_area = maxArea()
# print "max area:", max_area.max_area([0]) # 0
# print "max area:", max_area.max_area([1]) # 0
# print "max area:", max_area.max_area([1,5,4,3]) # 6
# print "max area:", max_area.max_area([9,9,1,1]) # 9
# print "max area:", max_area.max_area([9,1,9,1]) # 18
# print "max area:", max_area.max_area([9,1,1,9]) # 27

class arrPtr:
    """
    This problem was confusing to me - the instructions were vague as to what it was
    actually looking for .. or I just didn't get it. Solution was given

    You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

    Find i, j, k such that :
    max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
    Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

    **abs(x) is absolute value of x and is implemented in the following manner : **

          if (x < 0) return -x;
          else return x;
    Example :

    Input :
            A : [1, 4, 10]
            B : [2, 15, 20]
            C : [10, 12]

    Output : 5
             With 10 from A, 15 from B and 10 from C.
    """

    def minimize(self, A, B, C):

        i = 0
        j = 0
        k = 0
        l = len(A)
        m = len(B)
        n = len(C)
        ret = 2**31-1
        while i < l and j < m and k < n:
            tempMin = min(A[i],B[j],C[k])
            tempMax = max(A[i],B[j],C[k])
            ret = min(ret, tempMax-tempMin)
            if ret == 0:
                return ret
            if tempMin == A[i]:
                i += 1
            elif tempMin == B[j]:
                j += 1
            else:
                k += 1
        return ret

class remDup:

    def rem_dup(self, A):

        """
        sorted array - remove duplicates
        """

        t = 0

        for i in range(1, len(A)):

            if A[i] != A[t]:
                if t + 1 != i:
                    A[i], A[t + 1] = A[t + 1], A[i]
                t += 1

        A = A[:t + 1]
        return len(A)

# rem_dup = remDup()
# print rem_dup.rem_dup([1,2,2,2,2,3,4,4,5])
# print rem_dup.rem_dup([1,1,1])
# print rem_dup.rem_dup([1])

class diffK:

    hs = {}
    def build_hs(self, a):
        self.hs = {}
        for i in xrange(0, len(a)):
            if a[i] in self.hs:
                self.hs[a[i]].append(i)
            else:
                self.hs[a[i]] = [i]
        print self.hs

    def ls(self, a, val, idx=-1):
        if val in self.hs:
            # make sure i not equal to j
            if idx in self.hs[val]: # found matching i
                if len(self.hs[val]) > 1: # other j's available
                    return True
            else:
                return True
        return False

    def diff_k(self, A, B):
        """
        Find k from A[j] - A[i] in an ordered list of positive integers

        Thoughts:
          Store contents of list as hash, track number of items for each hashed 'collision'
          For each i, calculate val=i-k - then search in hash
          Since A[i] - A[j] = k then A[i] - k = A[j]
        """
        self.build_hs(A)

        for i in range(0, len(A)):
            """
             linear search for i-k
            """
            num = A[i] - B
            if num < 0:
                continue
            ans = self.ls(A, num, i)
            if ans:
                return True
        return False

diff_k = diffK()
#print diff_k.diff_k([0], 0) # False
# print diff_k.diff_k([1,2,2,3,4], 0)
#print diff_k.diff_k([1,5,4,1,2], 0)
#print diff_k.diff_k([77,28,19,21,67,15,53,25,82,52,8,94,50,30,37,39,9,43,35,48,82,53,16,20,13,95,18,67,77,12,93,0], 53) # True
# print diff_k.diff_k([11,85,100,44,3,32,96,72,93,76,67,93,63,5,10,45,99,35,13], 60) # True
# print diff_k.diff_k([1,3,2], 0) # False
# print diff_k.diff_k([1,5,4,1,2], 0) # True

class grayCode:

    base = [[0],[1]]

    def permutate(self, l=[]):
        """
        Thought permutations might work for gray codes
        keeping it here as an easy recursive permutation function for reference
        aint it purdy!
        """
        if len(l) == 0:
            return []
        if len(l) == 1:
            return [l]
        sub = []
        for i in xrange(0, len(l)):
            m = l[i]
            rem = l[:i] + l[i+1:]
            for p in self.permutate(rem):
                sub.append([m] + p)
        return sub

    def concat(self, l=[]):
        """
        Add 0 & 1 prefix to entire list and return
        e.g., lst = [[0,1],[1,0]]
          concat 0's [[0,0,1],[0,1,0]]
          contat 1's [[1,0,1],[1,1,0]] (reversed - reflected)
          return lst [[0,0,1],[0,1,0],[1,0,1],[1,1,0]]
        and so on...
        """
        ret = []
        for i in xrange(0, len(l)):
            ret.append([0] + l[i])
        for i in xrange(len(l) - 1, -1, -1):
            ret.append([1] + l[i])
        return ret

    def get_number(self, b):
        """
        where b is an int representing a binary string
        will need to convert to string and calculate the number
        """
        return int(''.join(str(s) for s in b), 2)

    def gray_code(self, A=1):

        # given answer
        #
        ans=[]
        for i in xrange(2**A):
            """
            Works, time O(n)
            note: xor flips bits where different
             i:0 0000 >> 0001 = 0000 xor 0000 = 0000 0
             i:1 0001 >> 0001 = 0000 xor 0001 = 0001 1
             i:2 0010 >> 0001 = 0001 xor 0010 = 0011 3
             i:3 0011 >> 0001 = 0001 xor 0011 = 0010 2
            etc...
            """
            ans.append((i>>1)^i)
        #print ans
        return ans

        """
        This works; however, time is O(n^2) - above is way more efficient
        """
        # if A is None or A < 1:
        #     return []
        # if A == 1:
        #     return [0,1]
        # # base sub list
        # sub = self.base
        # for i in xrange(1, A):
        #     # get options
        #     opt = self.concat(sub)
        #     sub = []
        #     # build sub list
        #     for j in xrange(0, len(opt)):
        #         sub.append(opt[j])
        #     print "len sub:", len(sub)
        #
        # cod = []
        # for i in xrange(0, len(sub)):
        #     if len(sub[i]) == A:
        #         cod.append(self.get_number(sub[i]))
        # return cod

# gray_code = grayCode()
# print gray_code.gray_code(2)

class combinations:

    def combinations(self, n, k):
        """
        in list of numbers 1 to n
        find combinations k in length
        e.g., n=4, k=2
          [1,2,3,4]
          [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]
        also, return sorted sub and list of combination
        e.g., [2,1] is not a sub sorted combination
              [1,3],[1,2] is not a sorted combination

        Pattern: in k=2
          for: 1,2,3,4 n=4, k=3
          [1,2],[1,3],[1,4]
          [2,3],[2,4]
          [3,4]
          then riffing on the last element of each sub list
          [2,3],[2,4]
          [3,4]
          putting it all together
          [1,2,3],[1,2,4],[1,3,4],[2,3,4]

        note: assume k <= n; if equal only one combo
        """

        if n == k:
            return [[i for i in xrange(1, n+1)]]

        if n < k or k == 0:
            return []

        bas = []

        # build first k=1 layer
        for i in xrange(1, n + 1):
            bas.append([i])

        # build the rest of the layers
        for c in xrange(1, k):
            tmp = []
            for i in xrange(0, len(bas)):
                base = bas[i][-1]
                for j in xrange(base + 1, n + 1):
                    tmp.append(bas[i] + [j])
            bas = list(tmp)

        return bas

#combinations = combinations()
#print combinations.combinations(10, 3)
#print combinations.combinations(1, 1)
#print combinations.combinations(2, 1)
#print combinations.combinations(4, 3)


class permutate:

    def permutate(self, l=[]):
        """
        Thought permutations might work for gray codes
        keeping it here as an easy recursive permutation function for reference
        aint it purdy!
        """
        if len(l) == 0:
            return []
        if len(l) == 1:
            return [l]
        sub = []
        for i in xrange(0, len(l)):
            m = l[i]
            rem = l[:i] + l[i+1:]
            for p in self.permutate(rem):
                #print "appending:{}+{}:{}".format([m], p, [m]+p)
                if [m] + p not in sub:
                    sub.append([m] + p)
        return sub

permutate = permutate()
print permutate.permutate([1,2,2,1,3,4,5])
