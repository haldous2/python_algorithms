"""
Cracking the coding interview
Practice questions
Part 8. Recursion
"""

import traceback

"""
8.1

nth step. walking up a step 1, 2 or 3 steps at a time
how many steps to get to the nth step

Brute force:
call a function recursively passing n-1, n-2 and n-3 steps ?

"""

def nth_step_naive(n):

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return nth_step_naive(n-1) + nth_step_naive(n-2) + nth_step_naive(n-3)

#print nth_step_naive(20)

memo_step = {}
def nth_step_memo(n):

    if n < 0:               # went too far
        return 0
    elif n == 0:            # this is the top of the stairs
        return 1
    elif n in memo_step:    # memoized step count
        return memo_step[n]
    else:                   # the meat - where steps are counted in all configurations of
                            # 1 + 2 + 3 steps ... 1 + 1 + 2, 1 + 2 + 1 etc...
                            # building stack frame, returns all 1's added up and returned to caller

        memo_step[n] = nth_step_memo(n-1) + nth_step_memo(n-2) + nth_step_memo(n-3)    # .541 options
        #memo_step[n] = nth_step_memo(n-1) + nth_step_memo(n-2)                          # .618 options
        return memo_step[n]

#print nth_step_memo(20)
#print memo_step

# fun with ratios - not the golden ration, golden for having 3 options to climb stairs
for i in memo_step:
    if i == memo_step.keys()[-2]:
        break
    lo = memo_step[i]
    hi = memo_step[i+1]
    #print float(lo) / float(hi)
    #print float(hi) / float(lo)

"""
8.2

Robot in a grid

Robot starts in top left, object is to move bottom right. can only go down or right. Robot might
encounter blocks that it cannot step on, pick right or down to avoid

Initial thoughts: should the robot run through all scenarios of getting to bottom right before proceeding
so as to not get stuck ?

Grid:

  [R][][][][][][][][ ]
  [ ][][] X[][][][][ ]
  [ ][] X[][][][][][!]

  base case:
   x encountered, return 0
   right encountered, return 0
   bottom encountered, return 0
   bottom right encountered, return 1
"""

memo_grid = {}
paths = []
path = []
def robotGrid(grid, row, col):

    if row > len(grid[0]) - 1:      # out of bounds
        return False
    elif col > len(grid) - 1:       # out of bounds
        return False

    if grid[row][col] == "X":     # invalid space
        return False

    if (row,col) in memo_grid:
        return False

    if grid[row][col] == "!":     # found the end!
        path.append([row,col])
        paths.append(path)
        return True

    if robotGrid(grid, row+1, col) or robotGrid(grid, row, col+1):
        path.append([row,col])
        return True

    memo_grid[row,col] = True
    return False

def robotGridV2(grid, row, col):

    if row > len(grid[0]) - 1:      # out of bounds
        return False
    elif col > len(grid) - 1:       # out of bounds
        return False
    elif (row,col) in memo_grid:    # failed point
        return False
    elif grid[row][col] == "X":     # invalid space
        memo_grid[row,col] = True
        return False
    elif grid[row][col] == "!":     # found the end!
        path.append([row,col])
        paths.append(path)
        return True
    elif robotGrid(grid, row+1, col) or robotGrid(grid, row, col+1):
        path.append([row,col])
        return True
    else:
        return False

grid = {
        0:[0,1,2,3,"X"],
        1:[5,6,7,8,9],
        2:["X",11,"X",13,14],
        3:[15,"X",17,18,19],
        4:[20,21,22,23,"!"]
       }

grid_2 = {
          0:[0,"X","X","X","X"],
          1:[5,6,"X",8,"X"],
          2:["X",11,12,13,14],
          3:[15,"X",17,"X",19],
          4:[20,21,22,23,"!"]
         }

# print "===== ROBOT GRID ====="
# robotGridV2(grid_2, 0, 0)
#
# print "memo_grid:", memo_grid
# for x in paths:
#     print "path:", x
#     for p in x:
#         print "point {},{}:{}".format(p[0],p[1],grid_2[p[0]][p[1]])

"""
8.3

Magic Index

Find the index that matches it's value

Naive approach: scan through, O(n) time O(0) extra space

Better time, O(logn) ? - some kind of binary search ?

Ways to search an array:
  1. walk through O(n)
  2. binary search (sorted array) O(logn)

Assumptions: array is in order - this
"""

def magic_index_naive(arr=None):
    """
    Naive approach - run through and compare index to value - runtime O(n)
    """
    if not arr:
        raise ValueError('missing input array')
    for i in arr:
        if i == arr[i]:
            return True

def magic_index_binary_search_util(arr=None, min=-1, max=-1):
    """
    Binary search approach. array must be sorted

    Test Data: [-1,0,2,7,10,14,17,20]   mid: 4
               [-1,0,2,7                mid: 2
                2 !!! found it!

    Test Data: [0,2,3,4,10,14,17,20]    mid: 4
               [0,2,3,4                 mid: 2
               [0,2                     mid: 1
                1 !!! found it!

    """

    if min > max:
        return -1

    mid = min + ((max - min) / 2)

    print "min:", min, " max:", max, "mid:", mid

    if mid == arr[mid]:                     # mid is the index value
        print "found it! so magical. magic index {}:{}".format(mid, arr[mid])
        return mid

    if mid < arr[mid]:
        # since array is sorted, mid index > array value mid->[0|1][2|2] mid=0, val=1, look left
        return magic_index_binary_search_util(arr, min, mid-1)
    else:
        # since array is sorted, mid index < array value [2|2][3|4]<-mid mid=3, val=4, look right
        return magic_index_binary_search_util(arr, mid+1, max)

def magic_index_binary_search(arr=None):
    """
    Binary Search approach. array must be sorted
    """
    if not arr:
        raise ValueError('missing input array')
    return magic_index_binary_search_util(arr, 0, len(arr))

def magic_index_binary_search_iterative(arr=None):
    """
    Iterative binary search of an array to find magic index
    p.s. this is much easier on my brain
    """
    if not arr:
        return None
    min = 0
    max = len(arr)
    while min <= max:
        mid = min + (max - min) / 2
        if mid == arr[mid]:
            return mid
        if mid < arr[mid]:
            # go left
            max = mid - 1
        else:
            # go right
            min = mid + 1

arr_t01 = [-1,0,2,7,10,14,17,20] # magic index is 2
arr_t02 = [0,2,3,4,10,14,17,20]

#print magic_index_naive(arr_t01)
#print magic_index_binary_search(arr_t02)
#print magic_index_binary_search_iterative(arr_t02)


"""
8.4

Power sets - write a method to return all subsets of a set

Q: are there constraints on subset size, steps, number returned ?

Naive: walk through set, iterate out subsets

Note: set->[1,2,3,4,5] subset->[2,3] .... and there you go
"""

def subsets(my_set):
    """
    Iteratively walk through set and build powersets
    O(2^n) time and O(n2^n) space
    """
    result = [[]]
    count = 0
    for x in my_set:
        #result = result + [y + [x] for y in result]
        for y in result:
            count += 1
            result = result + [y + [x]]
    print "count:", count
    return result

def powersets(my_set):
    """
    Build powerset from subset list builder
    Note: book exercise should be recursive, iterative is easier to implement and understand
    """
    if not my_set:
        return set()
    return set(map(frozenset, subsets(my_set)))

set_t01 = {1,2,3,4,5,6,7,8,9,10}
sub_t01 = {3,4,9,6,7,8}

# subset = sub_t01
# powerset = powersets(subset)
# print "len:", len(powerset), powerset
# print {4,5} in powerset
# s_count = 0
# for s in powerset:
#     s_count += len(s)
# print "space count:", s_count
# n * 2 ^ n-1 -> 4 * 2 ^ 3 -> 4 * 8 = 32
# 1+4 + 1+4 + 1+4 + 1+4

"""
8.5

Recursive multiply withou using * or /

Can use + - and bit shifting ??

  11
x 11
  11
 11
=121

Recursive: Base case(s) - n=0 when passing n-1 from 2nd int - return 1

"""

## iterative approach
def multiply_ints_iterative(i1, i2):
    """
    multiply i1 * i2 without using multiplier operation
    """
    result = 0
    for i in range(0, i2):
        result += i1

    return result

def multiply_ints(i1, n=0):
    """
    multiply i1 * i2 without using multiplier operation
    """
    if not i1:
        return 0
    if n == 0:
        #traceback.print_stack()
        return 0        # base case
    else:
        return multiply_ints(i1, n-1) + i1

memo_products = {}
def ints_product_util(i1, i2):
    """
    i1 and i2 should only be positive ints (assuming this)
    i2 has to be 0-9, i1 can be any int
    if i1 is negative, that can be calculated in the calling function since this is only a sub processor
    added memoization, well - just because this can be dynamic
    """
    if i2 <  0 or i2 > 9:
        raise ValueError("second integer should be between 0 and 9")
    if i2 == 0:
        return 0
    elif i2 in memo_products:
        return memo_products[i2]
    else:
        memo_products[i2] = ints_product_util(i1, i2-1) + i1
        return memo_products[i2]

def ints_product(i1=0, i2=0):
    """
    find the product of two integers
     ** without using multiplication or division - evetrything else is game

     This sub method will (multiply) each number of i2 to i1
     e.g. 10 * 100 -> 10 * 1 + 10 * 0 + 10 * 0 = 10|0|0 = 1000

    Created this version of products because very large ints were crashing recursion
    """
    if type(i1) is not int or type(i2) is not int:
        raise ValueError("inputs must both be integers")

    product = 0
    str_i2 = str(i2)

    for j in range(0, len(str_i2)):
        p_bas = ints_product_util(i1, int(str_i2[j]))
        p_val = int(str(p_bas) + ("0" * (len(str_i2) - j - 1)))
        print p_val
        product += p_val

    return product

# print multiply_ints(11, 10)
# print ints_product(11, 99999)
# print "memo_products:", memo_products


"""
8.6

Towers of Hanoi
Move tower of discs from first stack to 3rd stack. larger discs cannot be stacked on top of smaller

     -    |       |
    ___   |       |
  _______ |       |
  ==========================
  Source   Helper  Target

move the discs via stack frame (recursion)

1 discs: 1 -> Source to Target

2 discs: 1 -> Source to Helper
         2 -> Source to Target
         1 -> Helper to Target

3 discs: 1 -> Source to Target
         2 -> Source to Helper
         1 -> Target to Helper
         3 -> Source to Target
         1 -> Helper to Source
         2 -> Helper to Target
         1 -> Source to Target

Note: order of source, target and helper, target alternates on odd and even number of calls

"""

hanoi_count = 0
def hanoi(n, source, helper, target):

    global hanoi_count
    hanoi_count += 1
    print "===== hanoi( ", n, source, helper, target, " called"

    if n > 0:

        # move tower of size n-1 to helper:
        hanoi(n - 1, source, target, helper)

        if source[0]:
            disk = source[0].pop()
            print "n:" + str(n) + " moving " + str(disk) + " from " + source[1] + " to " + target[1]
            target[0].append(disk)

        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

source = ([3,2,1], "source")
target = ([], "target")
helper = ([], "helper")
# hanoi(len(source[0]),source,helper,target)
# print source, helper, target, hanoi_count

"""
8.7, 8.8

Permutations without duplicates of a string of unique characters


"""

perms = []
perms_count = 0
def strPermutationsRLevelUtil(dstr={}, pstr=[], level=0):
    """
    string permutation utility

    base case: when bottom level reached, add to list of results

    dstr: dict of each char with value count e.g. aaaa -> {'a':4, etc...}
    pstr: empty list of size original string e.g., for 'abcd', pstr = [None] * 4
    level = 0 ... always the default

    """
    global perms
    global perms_count
    perms_count += 1

    if len(pstr) == level:
        # appending a new lsit object of list
        # this will keep the rest of perms from changing on append
        perms.append(list(pstr))
        return

    for c in dstr:

        # base case for loop
        # when 0 encountered, all letters of this group have been used up
        if dstr[c] == 0:
            continue

        # decrement letter count track
        dstr[c] -= 1

        # add next letter to result and recursively build to next
        pstr[level] = c

        # recursively call until last level reached
        strPermutationsRLevelUtil(dstr, pstr, level + 1)

        # add counts back so we can branch off to other letters
        dstr[c] += 1

def strPermutationsRLevel(str=None):
    """
    dstr: dictionary string of string values e.g., 'aabc' = {'a':2,'b':1,'c':1}
    pstr: dictionary of permutations
    level: how deep the recursion has looked - default 0
    """
    if not str:
        print "string not passed"

    # build dstr for utility
    dstr = {}
    for c in str:
        if c in dstr:
            dstr[c] += 1
        else:
            dstr[c] = 1

    strPermutationsRLevelUtil(dstr, [None] * len(str))

    if perms:
        print "permutations found! - there are {} of them in total".format(len(perms))
        for p in perms:
            print p

#strPermutationsRLevel('aab')


"""
8.9

(((Parens balancing)))

"""

## Take 1
##  brute force, find all permutations of n ( & ) - then remove duplicates
def parenBalance(p=[], s=[], count=0):
    """
    return bool if parens are balanced
    counting 1, -1 - if equal zero then balanced
    """

    if not p:                   # base case, looked at all parens
        if not s:               # check counts and return result
            #print "YES!!!"
            return True
        else:
            #print "NOPE"
            return False

    paren = p.pop(0)

    if paren == '(':
        s.append('(')
        return parenBalance(p, s, count+1)
    elif paren == ')':
        if s and s[-1] == '(':
            s.pop()
            return parenBalance(p, s, count-1)
        else:
            return False
    else:
        # not a paren - no change in count
        return parenBalance(p, s, count)

def parenPermutationsBruteForce(n):
    """
    Find all paren permutations of n parens

    Note: reusing string permutation algorithm and checking each result
          against an is_balanced function

    Note: this is a naive approach since we are looking for every combination of
          each type of paren, then throwing away unbalanced combinations
          it works however, it's taking up a lot of processor time
    """
    if not n:
        return None

    # passing dict permutation string
    # e.g. n=2 ->{'(':2, ')':2}
    strPermutationsRLevelUtil({'(':n,')':n}, [None] * n * 2)

    if perms:
        print "permutations found! - there are {} of them in total which took {} time".format(len(perms), perms_count)
        for p in perms:
            if parenBalance(list(p)):
                print p

import unittest

## Take 2
##  going left, then right, then left - no dups to remove!
def parenPermutationsUtil(n=0, results=[], result='', open=0, close=0):
    """
    Building from a left first, then any combination thereafter recursively
    This will build all balanced parens without waste
    """
    print "parenPermutationsUtil(",n,",",results,",",result,",",open,",",close,")"
    if not n:                           # base input - need some n
        return None

    if open == n and close == n:        # base case, end result
        results.append(result)

    if open < n:                        # not enough open brackets yet
        parenPermutationsUtil(n, results, result + '(', open + 1, close)

    if close < open:                    # not enough close brackets yet
        parenPermutationsUtil(n, results, result + ')', open, close + 1)

def parenPermutations(n):
    results = []
    parenPermutationsUtil(3, results)
    return results

#print parenPermutations(3)
#
# class parenPermutationsTest(unittest.TestCase):
#
#     def setUp(self):
#         self.result = ['((()))', '(()())', '(())()', '()(())', '()()()']
#
#     def test_parens(self):
#         self.assertEqual(parenPermutations(3), self.result)

"""
8.10

 Paint Fill: Implement the "paint fill" function that
 one might see on many image editing programs. That is, given
 a screen (represented by a two-dimensional array of colors),
 a point, and a new color, fill in the surrounding area until
 the color changes from the original color.

 Brute Force: recursively call each grid square and paint in ones that don't already have a color

 Will need a class for square, track color, location ?

 Hints: 1. Treat this as a graph (was already going to do this)
        2. Use DFS to search from starting 'node' and paint fill from there

 Setup is key for this solution. Building a graph dict - list, then setting adjacent via pixel(node) class

 grid
  r - 0, 1, 2, 3, 4
  r - 5, 6, 7, 8, 9

  {0: [Node(0, 'white'), Node(1, 'white'), ...
   1: ...
  ...}

  End result - this will be much easier to work it for DFS
  0 white[5, 1] | 1 white[6, 0, 2] | 2 white[7, 1, 3] | 3 white[8, 2, 4] | 4 white[9, 3] |
  5 white[0, 6] | 6 white[1, 5, 7] | 7 white[2, 6, 8] | 8 white[3, 7, 9] | 9 white[4, 8] |

  Note: Holy crap, it works!

"""

pixel_color = ['red','green','black','blue','white','purple','GOLDEN']

class Pixel(object):

    def __init__(self, index=0, color=None):
        self.index = index
        self.color = color
        self.adjacent = []

def colorFillDFS(g=None, n=None, color_to=None, color_from=None, v=[]):
    """
    color fill DFS. recursively fill in color from starting
    'node'. return when color doesn't match
    """
    if color_to is None:               # color to cannot be None - this is the whole point of the algorithm!
        return
    if n is None:                      # base case for recursion
        return

    if not color_from:                 # set initial color 'from'
        color_from = n.color

    if n.color != color_from and n.color != color_to:          # base case for color 'from'
        return                                                 # not sure if this is a good base case yet... :{

    n.color = color_to                 # finally, the actual color change!

    v.append(n)                        # visit tracker - mucho importante!
    #print [x.index for x in v]

    for adjacent in n.adjacent:        # visit adjacent nodes
        if adjacent not in v:
            colorFillDFS(g, adjacent, color_to, color_from, v)

def colorFillPrint(g=None):
    """
    print grid color fill
    """
    print "========= adjacency matrix for print fill =========="
    if not g:
        return None
    for r in g:
        row_grid = ""
        for p in g[r]:
            row_grid += str(p.index) + " " + p.color  + str([x.index for x in p.adjacent]) + " | "
        print row_grid

def colorFillPrintList(g=None):
    """
    outputting a list of colors from grid for comparison in unittest (ordered)
    """
    if not g:
        return None
    colors = []
    for r in g:
        for p in g[r]:
            colors.append(p.color)
    return colors

def colorFillAdjacent(g=None):
    """
    Set adjacent list for each pixel 'node'
    """
    if not g:
        return None
    row_len = len(g[0])     # row length
    for r in g:             # each row in graph
        for p in range(0, len(g[r])):
            # look up
            if r > 0 and g[r-1][p]:
                g[r][p].adjacent.append(g[r-1][p])
            # look down
            if r < len(g) - 1 and g[r+1][p]:
                g[r][p].adjacent.append(g[r+1][p])
            # look left
            if p > 0 and g[r][p-1]:
                g[r][p].adjacent.append(g[r][p-1])
            # look right
            if p < len(g[r]) - 1 and g[r][p+1]:
                g[r][p].adjacent.append(g[r][p+1])

# test to change white
# node @ any node
g_pixel_01 = {
              0:[Pixel(0, 'white'), Pixel(1, 'white'), Pixel(2, 'white'), Pixel(3, 'white'), Pixel(4, 'white')],
              1:[Pixel(5, 'white'), Pixel(6, 'white'), Pixel(7, 'white'), Pixel(8, 'white'), Pixel(9, 'white')],
              2:[Pixel(10, 'white'), Pixel(11, 'white'), Pixel(12, 'white'), Pixel(13, 'white'), Pixel(14, 'white')],
              3:[Pixel(15, 'white'), Pixel(16, 'white'), Pixel(17, 'white'), Pixel(18, 'white'), Pixel(19, 'white')],
              4:[Pixel(20, 'white'), Pixel(21, 'white'), Pixel(22, 'white'), Pixel(23, 'white'), Pixel(24, 'white')],
              5:[Pixel(25, 'white'), Pixel(26, 'white'), Pixel(27, 'white'), Pixel(28, 'white'), Pixel(29, 'white')]
             }

# test to change blue
# node @ [2][2]
g_pixel_02 = {
              0:[Pixel(0, 'white'), Pixel(1, 'white'), Pixel(2, 'blue'), Pixel(3, 'white'), Pixel(4, 'white')],
              1:[Pixel(5, 'white'), Pixel(6, 'blue'), Pixel(7, 'blue'), Pixel(8, 'blue'), Pixel(9, 'white')],
              2:[Pixel(10, 'white'), Pixel(11, 'blue'), Pixel(12, 'blue'), Pixel(13, 'blue'), Pixel(14, 'white')],
              3:[Pixel(15, 'white'), Pixel(16, 'blue'), Pixel(17, 'blue'), Pixel(18, 'blue'), Pixel(19, 'white')],
              4:[Pixel(20, 'white'), Pixel(21, 'white'), Pixel(22, 'white'), Pixel(23, 'white'), Pixel(24, 'white')],
              5:[Pixel(25, 'white'), Pixel(26, 'white'), Pixel(27, 'white'), Pixel(28, 'white'), Pixel(29, 'white')]
             }

# colorFillAdjacent(g_pixel_02)
# colorFillPrint(g_pixel_02)
# colorFillDFS(g_pixel_02, g_pixel_02[2][2], pixel_color[6])
# colorFillPrint(g_pixel_02)

# class TestColorFill(unittest.TestCase):
#
#     def setUp(self):
#         self.g_pixel_02 = {
#                            0:[Pixel(0, 'white'), Pixel(1, 'white'), Pixel(2, 'GOLDEN'), Pixel(3, 'white'), Pixel(4, 'white')],
#                            1:[Pixel(5, 'white'), Pixel(6, 'GOLDEN'), Pixel(7, 'GOLDEN'), Pixel(8, 'GOLDEN'), Pixel(9, 'white')],
#                            2:[Pixel(10, 'white'), Pixel(11, 'GOLDEN'), Pixel(12, 'GOLDEN'), Pixel(13, 'GOLDEN'), Pixel(14, 'white')],
#                            3:[Pixel(15, 'white'), Pixel(16, 'GOLDEN'), Pixel(17, 'GOLDEN'), Pixel(18, 'GOLDEN'), Pixel(19, 'white')],
#                            4:[Pixel(20, 'white'), Pixel(21, 'white'), Pixel(22, 'white'), Pixel(23, 'white'), Pixel(24, 'white')],
#                            5:[Pixel(25, 'white'), Pixel(26, 'white'), Pixel(27, 'white'), Pixel(28, 'white'), Pixel(29, 'white')]
#                           }
#         colorFillAdjacent(self.g_pixel_02)
#         self.compare_pixels = colorFillPrintList(self.g_pixel_02)
#
#     def test_color_change(self):
#
#         g_pixel_02 = {
#                       0:[Pixel(0, 'white'), Pixel(1, 'white'), Pixel(2, 'blue'), Pixel(3, 'white'), Pixel(4, 'white')],
#                       1:[Pixel(5, 'white'), Pixel(6, 'blue'), Pixel(7, 'blue'), Pixel(8, 'blue'), Pixel(9, 'white')],
#                       2:[Pixel(10, 'white'), Pixel(11, 'blue'), Pixel(12, 'blue'), Pixel(13, 'blue'), Pixel(14, 'white')],
#                       3:[Pixel(15, 'white'), Pixel(16, 'blue'), Pixel(17, 'blue'), Pixel(18, 'blue'), Pixel(19, 'white')],
#                       4:[Pixel(20, 'white'), Pixel(21, 'white'), Pixel(22, 'white'), Pixel(23, 'white'), Pixel(24, 'white')],
#                       5:[Pixel(25, 'white'), Pixel(26, 'white'), Pixel(27, 'white'), Pixel(28, 'white'), Pixel(29, 'white')]
#                      }
#         colorFillAdjacent(g_pixel_02)
#         colorFillDFS(g_pixel_02, g_pixel_02[2][2], 'GOLDEN')
#         compare_pixels = colorFillPrintList(g_pixel_02)
#
#         self.assertEqual(compare_pixels, self.compare_pixels)

"""
8.11

Make some change
n change to be specific.
Using .25, .10, .5 and .1
n could = 1.00

Base case would be where total >= n

"""

def spareChangeV1Util(n, opt=[], qt=0, dm=0, nk=0, pn=0, sum=0):
    """
    Find all variations of change to be made from n where n is in cents

    opt is a list of ways that change can be made
        format of opt it [q,d,n,p] e.g., [0,2,1,1] = 31 cents
    """

    #print "qt:{}, dm:{}, nk:{}, pn:{}".format(qt, dm, nk, pn)

    if not n:
        return None

    if sum == n:
        str_option = "{},{},{},{}".format(qt,dm,nk,pn)
        opt.append(str_option)
    if sum > n:
        return

    #if qt <= int(n / .25):
    str_option = "{},{},{},{}".format(qt+1,dm,nk,pn)
    if str_option not in opt:
        spareChangeV1Util(n, opt, qt + 1, dm, nk, pn, sum + .25)

    #if dm <= int(n / .10):
    str_option = "{},{},{},{}".format(qt,dm+1,nk,pn)
    if str_option not in opt:
        spareChangeV1Util(n, opt, qt, dm + 1, nk, pn, sum + .10)

    #if nk <= int(n / .05):
    str_option = "{},{},{},{}".format(qt,dm,nk+1,pn)
    if str_option not in opt:
        spareChangeV1Util(n, opt, qt, dm, nk + 1, pn, sum + .05)

    #if pn <= int(n / .01):
    str_option = "{},{},{},{}".format(qt,dm,nk,pn+1)
    if str_option not in opt:
        spareChangeV1Util(n, opt, qt, dm, nk, pn + 1, sum + .01)

def spareChangeV1(n):

    if not n:
        return None

    options = []

    spareChangeV1Util(n, options)

    if options:
        print "number of options found:{}".format(len(options))
        for o in options:
            print o

def spareChangeUtil(n, coins=[], coin=0, results=[], memo_coin={}):
    """
    finding change in .10
    10
    5, 5
    5, 1, 1, 1, 1, 1
    1 ... 1

    recursively decrement n, base out at zero
    """
    if n in memo_coin:
        if memo_coin[n][coin] >= 0:
            return memo_coin[n][coin]   # already calculated this amount and coin

    if coin == 3:           # base for - it worked! - made it to pennies
        results.append(1)   # note: added results tracker to count results found
        return 1            # we can stop looking because it'll eventually get to the result with pennies
                            # note: order of coins should be 25,10,5,1

    elif n < 0:             # base for - it didn't work, went past our goal
        return 0

    # meat of the algorithm
    inc = spareChangeUtil(n - coins[coin], coins, coin, results, memo_coin) # all variations of a coin
    dec = spareChangeUtil(n, coins, coin + 1, results, memo_coin)           # increment through all coins

    count = inc + dec

    if n in memo_coin:
        memo_coin[n][coin] = count
    else:
        memo_coin[n] = [-1] * len(coins)
    print memo_coin

    return count                                        # returning number of ways when base not hit

def spareChange(n):
    """
    make some change up to n
    """
    coins = [25,10,5,1]
    results = []
    print spareChangeUtil(n, coins, 0, results)
    print "results:", results

#spareChange(10)

"""
8.12

8x8 chess board - set 8 queens on board so that no row, column or diagonal is shared by each piece

checking row, col, each diagonal of each piece as it is placed

Initial thoughts:
checking rows and columns is easiest (assuming) for collisions
checking diagonals will take some doing. recursively look from a point in all directions X out

"""

def queens(num_queens):
    results = []
    grid_size = num_queens
    columns = [None]*num_queens         # instead of an actual grid, just store col of queen placement in a row
    n_ways(columns, 0, results, grid_size)
    return results

def n_ways(columns, row, results, grid_size):

    if row == grid_size:
        results.append(columns)
        return

    for col in range(0, grid_size):
        if is_valid(columns, row, col, grid_size):
            cols_copy = columns[:]
            cols_copy[row] = col
            n_ways(cols_copy, row+1, results, grid_size)

def is_valid(columns, row1, col1, grid_size):

    if col1 in columns:
        return False

    for row2, col2 in enumerate(columns):
        if col2 is not None:
            if abs(col1 - col2) == abs(row1 - row2):
                return False

    return True

#print len(queens(8))

## approach using a grid (method above seems a bit more obvious)
## =============================================================================
def gridCheckValid(g={}, q=[0,0]):
    """
    Check queen placement validity

    walk through grid columns checking if other QEEN(s) in row, col or diag
    return True or False
    """
    for c in g:         # each column (index)

        # check column where q is slated to live
        if c == q[0]:
            # walk the row looking for queens
            if "QEEN" in g[c]:
                #print "oops - found QEEN in col {}".format(c)
                #gridQueensPrint(g)
                return False

        # check row for queens
        # c is current column - q[1] is the row for queen placement
        # looking through rows as we walk columns
        if g[c][q[1]] == "QEEN":
            #print "oops - found QEEN in row {}".format(q[1])
            #gridQueensPrint(g)
            return False

        # diagonal
        for row, val in enumerate(g[c]):
            if val is not None:
                if abs(q[0] - c) == abs(q[1] - row):
                    #print "oops - found QEEN in diag"
                    #gridQueensPrint(g)
                    return False

    return True

def gridFindPlacesUtil(g={}, col=0, result=[], results=[]):
    """
    Recursively loop through each row, find an open spot etc...

    g = graph
    col = index down
    row = index across

    """

    if col == 8:
        print result
        # track result
        results.append(list(result))
        return

    for row in range(0, 8):

        if gridCheckValid(g, [col,row]) is True:

            g[col][row] = "QEEN"
            result.append([col,row])

            gridFindPlacesUtil(g, col + 1, result, results)

            # on the way back, reset column
            g[col] = [None]*8
            result.pop()

def gridFindPlaces(g={}):
    """
    Find all places that a queen can go in an 8x8 grid
    queens cannot lie on same horizontal or vertical line, or diagonals for that matter
    """
    results = []
    gridFindPlacesUtil(dict(g), 0, [], results)
    print len(results)

def gridQueensPrint(g):
    print "========== grid-queens =========="
    if not g:
        print "Nope"
    for r in g:
        g_row = ""
        for c in g[r]:
            g_row += str(c) + " | "
        print g_row

queens = {  0:[None]*8,
            1:[None]*8,
            2:[None]*8,
            3:[None]*8,
            4:[None]*8,
            5:[None]*8,
            6:[None]*8,
            7:[None]*8
        }

#gridQueensPrint(queens)
#gridFindPlaces(queens)

"""
8.13

Stack n boxes, smaller on larger
boxes are larger when width, height and depth are larger
if boxes have equal numbers of larger parts then order doesn't matter
width:w, height:h, depth:d
cannot rotate boxes
calculate height of stack from height:h and number of boxes stacked

thoughts: thinking this is a 'what if' problem where boxes are theoretical and don't
          actually have a width, heighth or depth. will need to design algorithm
          where width & depth are larger than previous width and depth

epiphany: since the boxes cannot be rotated, should be easy enough to just add all the heights
          knowing that the boxes will eventually all be stacked one way or another. Since
          we just need the height, doesn't matter if they are in order or not.. just add the
          heights... which would be: for each box, add height until all boxes accounted for
          Is it really that easy ? - no, probably not... or is it ?

hints:  sort boxes first

        use a stack[] to keep track of largest boxes (recursive ?)
"""
class box(object):

    def __init__(self, width=0, height=0, depth=0):
        self.width = width
        self.height = height
        self.depth = depth
        self.used = False

def sortBoxesAll(boxes=[], height=0):        # sort list of box objects by width and height
    """
    box 3x2 larger than 2x2
    how do you sort something that doesn't have any values associated?
    """
    if not boxes:
        return height

    box = boxes.pop()
    if box.used is False:
        height += box.height
        box.used = True
    return sortBoxes(boxes, height)

def boxesSortHeight(boxes=[]):
    """
    sort list of boxes
    using lambda, internal hidden function is faster and cleaner
    sort big to small height
    """
    if not boxes:
        return []
    boxes.sort(key=lambda x: x.height, reverse = True)

def boxesCanStack(box1, box2):
    """
    compare box1(base) to box2(stacker)
    box1 should be larger in all dimensions
    """
    if not box1 or not box2:
        return None
    if (box1.width > box2.width and
        box1.depth > box2.depth and
        box1.height > box2.height):
        return True
    return False

def boxesPrint(boxes):
    print "========== boxes =========="
    if not boxes:
        print "No boxes to print"
    for b in boxes:
        print "box w:{} d:{} h:{}".format(b.width, b.depth, b.height)

def boxesStackUtil(boxes=[], baseBox=None, boxHeight=0):
    """
    stack boxes utility
    test if stackable based on last stacked box
    boxes should be in order according to height at this point
    on back side of recursion add up heights and return
    """
    if not boxes:               # base case - no more boxes
        return boxHeight

    if not boxHeight:
        boxHeight = baseBox.height

    if boxesCanStack(baseBox, boxes[0]):
        # stackable, add those heights
        boxHeight += boxes[0].height
        baseBox = boxes.pop(0)
    else:
        boxes.pop(0)

    return boxesStackUtil(boxes, baseBox, boxHeight)

def get_stackable_boxes(box, boxes):
    for i, top_box in enumerate(boxes):
        if boxesCanStack(box, top_box):
            return boxes[i:]
    return None

def boxesStackR(boxes, memo_boxes={}):

    print "boxesStackR boxes:", [x.height for x in boxes]

    if len(boxes) == 1:
        return boxes[0].height

    # set base, create stackable_boxes that can stack on base
    # from: [5,4,3,2,1], base: 5 & stackable_boxes: [4,3,2,1]
    #       [4,3,2,1]    base: 4 & ..           ..: [3,2,1] etc...
    current_box = boxes[0]
    if current_box in memo_boxes:
        #print "found box {} in memo ... returning {}".format(current_box.height, memo_boxes[current_box])
        return memo_boxes[current_box]
    stackable_boxes = get_stackable_boxes(current_box, boxes[1:])

    if stackable_boxes:
        current_height = current_box.height + boxesStackR(stackable_boxes, memo_boxes)
    else:
        current_height = current_box.height

    memo_boxes[current_box] = current_height

    # now look at sub stacks e.g. [5,4,3,2,1] -> next up [4,3,2,1]
    max_height = max(current_height, boxesStackR(boxes[1:], memo_boxes))
    return max_height

def boxesStack(boxes=[]):
    """
    stack boxes
    sort box classes by height
    naive approach - forgot to take into account all sub boxes that might not stack on first base
    """
    if not boxes:
        print "no boxes to stack"

    # get to stacking
    boxesSortHeight(boxes)
    maxHeight = boxesStackR(boxes)
    print "boxes height:", maxHeight

def boxesStackIterative(boxes=[]):
    """
    Iterative comparison for stacking boxes
    this seems a lot easier to understand - O(n^2), which I believe the recursive also runs at
    """
    if not boxes:
        print "no boxes to stack!"
    if len(boxes) == 1:
        print "box stack height:", boxes[0].height

    # sort by height
    boxesSortHeight(boxes)

    max_height = 0
    for i, b in enumerate(boxes):
        height = b.height
        for j in range(i + 1, len(boxes)):
            base = boxes[j-1]
            #print "({},{},{}) - ({},{},{})".format(base.width, base.height, base.depth, boxes[j].width, boxes[j].height, boxes[j].depth)
            if boxesCanStack(base, boxes[j]):
                #print "height({}) + {}".format(height, boxes[j].height)
                height += boxes[j].height
        max_height = max(max_height, height)

    print "box max height:", max_height

# create some boxes
boxes_b1 = [box(4,4,4)]
boxes_b1.append(box(1,1,1))
boxes_b1.append(box(3,4,3))
boxes_b1.append(box(5,5,5))
boxes_b1.append(box(2,2,2))

boxes_b2 = [box(1,1,1)]
boxes_b2.append(box(2,2,2))
boxes_b2.append(box(3,3,3))
boxes_b2.append(box(4,4,4))
boxes_b2.append(box(5,5,5))

#print sortBoxes(boxes)
#boxesPrint(boxes_b1)
boxesStack(boxes_b1)
boxesStackIterative(boxes_b1)

"""
8.14

Boolean Evaluations
"""

def bool_eval(expr, result):

    if expr == "1":
        if result:
            # it's true that it's true
            return 1
        return 0
    if expr == "0":
        if not result:
            # it's true that it's false
            return 1
        return 0

    subways = 0

    for i in xrange(1,len(expr),2):

        operator = expr[i]
        left = expr[0:i]
        right = expr[i+1:]

        left_true = bool_eval(left, True)
        left_false = bool_eval(left, False)
        right_true = bool_eval(right, True)
        right_false = bool_eval(right, False)

        # total ways 0 (0*0)(1*0)(0*1), 1 (1*1)
        total_ways = (left_true + left_false) * (right_true + right_false)
        true_ways = 0

        if operator == "&":
            true_ways += left_true*right_true
        elif operator == "|":
            true_ways += (
                (left_true*right_true)
                + (left_true*right_false)
                + (left_false*right_true)
            )
        elif operator == "^":
            true_ways += (left_true*right_false) + (left_false*right_true)

        if result:
            subways += true_ways
        else:
            subways += total_ways - true_ways

    return subways

print "number of paren ways:", bool_eval("1^0|0|0", True)

#####
# Unit Test
#####

if __name__ == '__main__':
    unittest.main()
