"""
Cracking the coding interview
Practice questions
Part 05. Bit Manipulation
"""

import unittest

"""
Clear a bit
a = 255
a = a & ~(1 << 2)   # shift 1 over index 3 -> 000000001 to 00000100
                      inverse with ~ to 11111011 as mask
                      & a with mask to get result
                         e.g.: (255) 11111111
                                     00000100
                          inverse:   11111011 &
                                     11111011 = 251

Set a bit
a = a | (1 << 2)    # flip bit at 3rd index to 1

Read a bit
a & (1 << 4), not a & (1 << 4) - bit is or isn't set at 4th index
"""

"""
05.01 - Insertion (bits into bits)

insert int m into n @ point j to i

e.g. insert m:1111 into n:0000000000000000 @ n.index j:6, i:3 -> 0000000001111000

create a 1 mask, shift, invert AND zero out n

with original mask, shift and OR n

"""

def insertBitMtoN(m, n, i, j):
    """
    combine mask m into n @ index i to j
    make sure i and j fall in bounds of 8 byte integer 'n'

    m:mask binary sequence
    n:main binary sequence
    i:start insert index of n
    j:end insert index of n
    """

    # i and j must be insinde 64 bits. 0 to 63
    if i < 0 or i > 63 or j < 0 or j > 63:
        return None

    # len of m(ask) should be lenght of bit index j to i
    if len(m) != j - i + 1:
        return None

    # mask length
    ml = (j - i) + 1
    if ml <= 0:
        return None

    # untouched mask
    mm = int(str(m), 2)
    mm = mm << i

    # create 0's mask to zero out n
    m1 = '0b' + '1' * ml    # mask ones 'string'      '0b1111'
    m1 = int(m1, 2)         # mask integer             0b1111   (15)
    m1 = m1 << i            # mask shifted             0b111100 (60)
    m0 = ~m1                # mask inverted to zeros   0b000011 (-61)

    n = int(str(n), 2)      # n integer

    # and n to zeros where mask will eventually sit
    n = n&m0
    #print "zero mask:", bin(m0), bin(n)

    # and n with mask to place mask
    n = n|mm
    #print "place mask:", bin(mm), bin(n)

    return bin(n)

#print insertBitMtoN('01', '101010', 2, 3)
#print insertBitMtoN('01', '10', 8, 9)

"""
05.02 - Binary to String

Given a real number from 0 to 1 (e.g. .72)
passed in as a double (python default int, 64 bit)
print the binary representation
if binary representation is larger than 32, print "ERROR"

had to look this up. this makes sense

    8 4 2 1 . 2 4 8 16   index value
    0 0 0 0   0 0 0 0    binary space

    1/2 .5 = bin .1
    1/4 .25 = bin .01
    1/8 .125 = bin .001
    1/16 .0625 = bin .0001 etc...

    Example:
    number is .512
    multiply by 2 (1/2 * 2) = 1.024
    bit becomes 1

    number is .25
    multiply by 2 = .5
    bit becomes 0

Hints:

  # how would you do this for integers ?
    int to binary ? divide, if remainder then bin is 1, else 0. divide till less than 0 e.g. (.99)

  # A number .893 (base 10) = 8 * 10^-1 + 9 * 10^-2 + 3 * 10^-3
    translate this to base 2
    8 / 2 = 4 R 0
    4 / 2 = 2 R 0
    2 / 2 = 1 R 0
    2 / 1 = 0 R 1 --> 1000 etc..

"""

def decimalToBinary(dec):
    """
    """
    if not dec or dec < 0 or dec > 1:
        print "ERROR - need decimal from 0 to 1 e.g. .72"
        return

    max = 64    # long
    #max = 32    # int
    bin = ""
    rem = dec
    count = 0

    while rem != 0 and count <= max + 1:

        bin += str(int(rem * 2))
        rem = (rem * 2.0) % 1
        #print rem

        count += 1

    if count > max:
        print "ERROR - larger than {} bits".format(max)
    else:
        print "binary repr of {} is .{} with length {} with int val {}".format(dec, bin, len(bin), int(str(bin), 2))

#decimalToBinary(.5)
#decimalToBinary(.71)
#decimalToBinary(.1) # infinite(ish)
# for i in range(1, 100):
#     dec_i = i * .01
#     decimalToBinary(dec_i)

"""
05.03 - Flip bit to win!

input an integer
with integer bineary sequence
   flip only 1 bit to find the longest length of 1's in the sequence

Naive:
    walk through bits, 0 to 63
    keep track of number of 1's uninterrupted.
    encounter a 0
       if 0 not flipped yet (track the flip) - flip and add to count
       if already flipped, restart counter but keep track of largest count

    e.g. 1110100000011111101

Hints:

    # Flipping a 0 to 1 can merge two sequences

"""

def flipABitMax(p_int):

    print "p_int:{} {}".format(p_int, bin(p_int))

    curr_bit = None
    last_bit = None
    last_zro = 0

    nbr_bits = 0
    max_bits = 0

    for i in range(0, 64):

        # read a bit - create a mask and shift i times, then and out
        m = (1<<i)
        curr_bit = p_int & m

        nbr_bits += 1

        #print "nbr_bits:{} max_bits:{} last_zro:{} last_bit:{}".format(nbr_bits, max_bits, last_zro, last_bit)

        if curr_bit == 0:

            # update nbr_bits by last_zero
            nbr_bits -= last_zro

            # tracking index value of last zero
            last_zro = nbr_bits

            if last_bit == 0:
                # too many zeros in a row, reset count
                nbr_bits = 0

        if nbr_bits > max_bits:
            # update max
            max_bits = nbr_bits

        last_bit = curr_bit

    return max_bits

#print flipABitMax(1775)     # book example: maxbits are 8
#print flipABitMax(1590) # test: 1590 11000110110 maxbits should be 5
#print flipABitMax(238)      # test: 238 11101110 maxbits should be 7

"""
5.04 - Next number

Input a positive integer
find the next largest and smallest integer with the same number of 1's bits as the original

Brute Force (not written here)
go int by int starting from input integer (going smaller or larger depending on direction)
  track the number of zeros for each value. stop when matching bits 1's and 0's

Time complexity O(b) where b is max 64

"""

def nextBinSmaller(p_int):
    """
    """
    if not p_int:
        return None
    if type(p_int) is not int:
        return None
    if p_int < 0:
        return None

    first_zero = None

    def swapOneZero(i, j):
        """
        swap bin index i for j
        """
        #print "swap @ i:{} j:{}".format(i, j)

        if p_int & (1<<i) == 0 and p_int & (1<<j) > 0:

            s = p_int | (1<<i)    # set to 1
            s = s & ~(1<<j)     # clear to 0
            return s

        elif p_int & (1<<i) > 0 and p_int & (1<<j) == 0:

            s = p_int | (1<<j)    # set to 1
            s = s & ~(1<<i)     # clear to 0
            return s

        else:

            return p_int

    for i in range(0, 64):

        # read a bit - create a mask and shift i times, then and out
        m = (1<<i)
        curr_bit = p_int & m

        if curr_bit == 0:
            if not first_zero:
                first_zero = i
        else:
            if first_zero is not None:
                p_int = swapOneZero(first_zero, i)

    return p_int

def nextBinLarger(p_int):
    """
    """
    if not p_int:
        return None
    if type(p_int) is not int:
        return None
    if p_int < 0:
        return None

    #print "nextBinLarger p_int:{} bin:{}".format(p_int, bin(p_int))

    last_one = None

    def swapOneZero(i, j):
        """
        swap bin index i for j
        """
        #print "swap @ i:{} j:{}".format(i, j)

        if p_int & (1<<i) == 0 and p_int & (1<<j) > 0:

            s = p_int | (1<<i)    # set to 1
            s = s & ~(1<<j)     # clear to 0
            return s

        elif p_int & (1<<i) > 0 and p_int & (1<<j) == 0:

            s = p_int | (1<<j)    # set to 1
            s = s & ~(1<<i)     # clear to 0
            return s

        else:

            return p_int

    def moveOneFarRight(move_one):
        """
        parm: move_one is binary index of 1 moving
        move 1 to next available 0 position
        e.g. i=4, 110001 -> 100011
        set next avail. zero to 1, clear bit at i
        """

        #print "moveOneFarRight @ {}".format(move_one)

        next_zro = None

        # find next available 0 slot
        for i in range(0, 64):
            if p_int & (1<<i) == 0:
                next_zro = i            # next available zero
                break

        if next_zro is not None and next_zro < move_one:
            s = p_int | (1<<next_zro)   # set next zero to 1
            s = s & ~(1<<move_one)  # clear bit at move_one
            return s
        else:
            return p_int

    for i in range(63, -1, -1):

        m = (1<<i)
        curr_bit = p_int & m

        if curr_bit > 0:
            if last_one is None:
                p_int = swapOneZero(i, i+1)
                last_one = i
            else:
                # push all 1's to front
                p_int = moveOneFarRight(i)

    return p_int

#print nextBinSmaller(14)
#print nextBinLarger(14)

class nextBinTest(unittest.TestCase):

    def setUp(self):
        self.p_int = 14

    def test_next_larger(self):
        self.assertEqual(13, nextBinSmaller(self.p_int))

    def test_next_smaller(self):
        self.assertEqual(19, nextBinLarger(self.p_int))

"""
5.5 - Debugger

What does ((n & (n-1)) == 0) do ?

e.g. n=4  100      n=7  111     n=8  1000
          011 &         110 &        0111 &
          000           110          0000

It appears that 0 only happens when 1 bit is flipped

This piece of code checks to see if only one bit is flipped

"""

def debuggerCode():
    """
    running through integers 1 to 16 - output results based on debugger code

    as defined by book:
     ((n & (n-1)) == 0)

    running this proves that only one bit is flipped when anded result is 0
    """

    for i in range(1, 17):

        print "result of {}:{} = {}".format(i, bin(i), i & (i-1))

#debuggerCode()

"""
5.6 - Conversion

how many bits to flip to turn int A into int B

e.g. 29 (11101) -> 15 (01111) -> 2 flips

Brute Force: walk through 0 to 64, match B to A and keep track of non-matching bits
   Time complexity O(b) where b is max 64 bits

"""

def bitsConversion(intA, intB):
    """
    assume intA, intB are both non-negative integers

    """
    if not intA or not intB:
        return None
    if type(intA) is not int or type(intB) is not int:
        return None
    if intA < 0 or intB < 0:
        return None

    need_to_flip = 0

    # now that we have that out of the way, let's do some walking
    for i in range(0, 64):

        if intA & (1<<i) != intB & (1<<i):

            need_to_flip += 1

    return need_to_flip

#print bitsConversion(29, 15)
#print bitsConversion(2202112, 220212020)

"""
5.7 - Pairwise Swap

swap odd and even bits
in as little code as possible
e.g. 0 and 1 swap, 2 and 3 swap, 4 and 5 etc...

Naive approach... time: O(b)
Initial thoughts range(0, 63, 2) - skip two on each step (of the walk)
   then swap i with i+1

And then I thought...

    if bit 0 is 0, shift 1 right
    if bit 0 is 1, shift 1 left

    0110 -> 1001
    0101 -> 1010

    however, looking at this example it won't work

    Hmmm....
    this was almost right - masking with 0101, 1010 on odds and even, shifting and then or-ing
    should do the trick

"""

def binaryPairwiseSwapUtilNaive(p_int):
    """
    swapping two at a time - this isn't a whole lot of code, there is
    a faster way using a mask though - this is here for sh**s and giggles
    """
    if not p_int:
        return None
    if type(p_int) is not int:
        return None
    if p_int < 0:
        return None

    def setBit(i, v):
        """
        clear and set bit at index i
        """
        s = p_int & ~(1<<i)                   # clear bit
        if v > 1:
            s = s | (1<<i)                    # set bit
        return s

    for i in range(0, 64, 2):

        t_int = p_int & (1<<i)                # temp store value bit 0
        p_int = setBit(i, p_int & (1<<i+1))   # value of bit 0 = bit 1
        p_int = setBit(i+1, t_int)            # value of bit 1 = bit 0

    return p_int

def binaryPairwiseSwapUtil(p_int):
    """
    build and masks for odd and even bits
    shift masks even:left and odd:right
    or masks back together for pairwise swap result
    """
    if not p_int:
        return None
    if type(p_int) is not int:
        return None
    if p_int < 0:
        return None

    """
    masks
       odd: 1010
       evn: 0101
    """
    m_odd = 0xaaaaaaaaaaaaaaaa  # 1010
    m_evn = ~m_odd              # 0101

    """
    ands
       evn: 1100
            0101 &
            0100
       odd: 1100
            1010 &
            1000
    """
    m_odd_and = p_int & m_odd
    m_odd_and = m_odd_and >> 1  # shift right (the swap)
    m_evn_and = p_int & m_evn
    m_evn_and = m_evn_and << 1  # shift left (the swap)

    """
    put it all back together
    """
    r_int = m_odd_and | m_evn_and

    return r_int

def binaryPairwiseSwap(p_int):

    #int_swap = binaryPairwiseSwapUtilNaive(p_int)
    int_swap = binaryPairwiseSwapUtil(p_int)

    if int_swap is None:
        int_swap_bin = "None"
    else:
        int_swap_bin = bin(int_swap)

    print "swapping int:{} result:{}".format(bin(p_int), int_swap_bin)

#binaryPairwiseSwap(3426)

class binaryPairwiseSwap(unittest.TestCase):

    """
    Test case: parameter in: 3426 binary(0b110101100010)
                        out: 3729 binary(0b111010010001)
    """

    def setUp(self):
        self.p_int = 3426

    def test_pairwise_swap_naive(self):
        self.assertEqual(3729, binaryPairwiseSwapUtilNaive(self.p_int))

    def test_pairwise_swap_shift(self):
        self.assertEqual(3729, binaryPairwiseSwapUtil(self.p_int))

"""
5.8 - Draw line

monochrome monitor stored as single array of bits
allow 8 consecutive pixels to be stored in one byte (1 byte = 8 bits, 4 bytes for int, 8 bytes for python int)
screen has width w, where w is divisible by 8
height can be derived from length of array / width w
draw a line such that (x1, y), (x2, y)

example drawLine(byte[] screen, int width, int x1, int x2, int y)

   screen could be setup: byte
                          byte
                          byte
                          byte

    where screen is 4 bytes long, (width is 8 bits - 1 byte) ... height would be 4 bytes / 1 byte = 4 lines

    example: input byte screen [0,0,0,0,0,0,0,0,0] - width = 2

    need to verify all bytes fill screen based on width
    then calculate which line each bytes lives on in order to write 1 bits

"""

def drawLine(screen=[], width=0, x1=0, x2=0, y=0):
    """
    parameters:
    assume y=0 is top line, x1 & x2 = 0 is extreme left col
    """
    if not screen:
        return None
    if type(screen) is not list:
        return None
    if not width:
        return None
    if type(width) is not int:
        return None
    if width <= 0:
        return None

    # verify number of bytes to width
    # no remainder if they all fit evenly
    if len(screen) % width > 0:
        return None

    # make sure x's fit inside width
    # width * 8 = number of possible bytes across
    if x1 < 0 or x1 >= width * 8 or x2 < 0 or x2 >= width * 8:
        return None

    if x1 > x2:
        return None

    # height
    height = len(screen) / width

    if y > height or y < 0:
        return None

    # calculate which byte(s) is row y
    # didna get used - keep for historical sake
    # s_byte = y * width
    # e_byte = y * width + width - 1

    ## FUN with masks method - build a mask, or it to all those juicy zeros
    for j in range(0, width):

        # for y = 2, bytes 4, 5
        # for x1 = 2, x2 = 15 - build mask accordingly 0^0=0, 0^1=1
        s_bit_range = 8 * j
        e_bit_range = (8 * (j + 1)) - 1

        # mask start bits - build start mask
        if x1 > s_bit_range:
            m_s_bits = x1 - s_bit_range
        else:
            m_s_bits = 0

        # mask end bits - build end mask
        if x2 < e_bit_range:
            m_e_bits = e_bit_range - x2
        else:
            m_e_bits = 0

        # in the middle
        m_mid_bits = 8 - m_s_bits - m_e_bits

        # mask building
        m_string = '0b' + '0' * m_s_bits + '1' * m_mid_bits + '0' * m_e_bits

        mask = int(str(m_string), 2)
        test = 0

        #print "mask:", mask, " m_string:", m_string, " test:", test ^ mask
        screen[j + y * width] = screen[j + y * width] ^ mask

    # print 'screen'
    # for i in range(0, height):
    #     str_screen = ""
    #     for j in range(0, width):
    #         pix_screen = screen[i * width + j]
    #         for b in range(7, -1, -1):
    #             if pix_screen & (1<<b) == 0:
    #                 pix_bit = 0
    #             else:
    #                 pix_bit = 1
    #             str_screen += str(pix_bit)
    #         str_screen += " "
    #     print str_screen

    return screen


# drawline(screen, width, x1, x2, y)
#drawLine([0,0,0,0,0,0,0,0,0,0], 2, 2, 12, 2)

class drawLineTest(unittest.TestCase):

    def setUp(self):
        self.in_screen = [0,0,0,0,0,0,0,0]
        self.out_screen = [0,0,0,0,63,248,0,0]

    def test_draw(self):
        #                                 drawline(screen, width, x1, x2, y)
        # byte 1, row 2: 0b00111111
        self.assertEqual(self.out_screen, drawLine(self.in_screen, 2, 2, 12, 2))

######## unit test ########
if __name__ == '__main__':
    unittest.main()
