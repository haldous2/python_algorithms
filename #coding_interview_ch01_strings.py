"""
Cracking the coding interview
Practice questions
Part 1. Strings
"""

"""
 Helper functions:
"""

# QuickSort O(n log n)
# note python sort is also (n log n).. so, just sayin'
def quickSort(arr):
    if len(arr) > 0:
        quickSort_worker(arr, 0, len(arr) - 1)
        return arr
    else:
        return None

def quickSort_worker(arr, lo, hi):
    if lo < hi: # base condition
        p = quickSort_partition(arr, lo, hi) # pivot
        quickSort_worker(arr, lo, p - 1) # go left
        quickSort_worker(arr, p + 1, hi) # go right

def quickSort_partition(arr, lo, hi):
    i = lo # the wall
    p = arr[hi] # pivot
    for j in range(lo, hi):
        if arr[j] <= p: # less than pivot
            arr[i], arr[j] = arr[j], arr[i] # swap
            i += 1
    arr[hi], arr[i] = arr[i], arr[hi] # swap pivot to wall
    return i # returning new pivot

def get_permutations(str):

    if not str:
        return []

    stack = list(str)
    results = [stack.pop()]
    #print "start-results:{}".format(results)
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                #print "i={} w={} (w[:i]={} c={} w[i:]={}) ({})".format(i, w, w[:i], c, w[i:], w[:i] + c + w[i:])
                new_results.append(w[:i] + c + w[i:])
        results = new_results
        #print results
    return results

"""
 Unique characters in a string
 Note: not using extra space - so no hash table or comparison array etc.
       Time is O(n^2) Space is O(1)
"""
def unique_characters_in_string(str):
    for i in range(0,len(str)):
        # now we'll run through from where we left off comparing
        # note: starting @ i + 1 so we don't compare start to start!
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                # dup found - get out of here
                return False
    return True

"""
 Unique characters in a string: with extra space tracking
 Use additional storage to track which characters have already been used
 Should ask what characters are being used, ascii or unicode
 In this case using ascii 256
 using a dict, no need to know the size ahead of time
 Time O(n) with Space O(n)
"""
def unique_character_in_string_tracker(str):

    # if using ascii, technically size is max 256
    # although if using unicode, size could be 1.4 million - is this helpful at all ?
    if len(str) > 256:
        return False

    # extra space dict
    track = {}
    for c in str:
        if ord(c) in track:
            return False
        else:
            track[ord(c)] = True

    return True

# for fun using a bit vector (extra storage) - also (not a standard package of p2.xx)
def unique_character_in_string_bit(str):
    checker = 0
    checkbit = 0
    ascii = None
    for i in range(0, len(str)):
        """
         bit vector in 32 bit integer
         00000000000000000000000000000000

         where:
         ascii: a(97) to z(122) and A(65) to Z(90)

         e.g., if ascii val 97-122, subtract 96
               if ascii val 65-90,  subtract 64

         then store a-z, A-Z in bit vector 1 thru 26
         example: if a and C already found in list
         10100000000000000000000000000000

        """
        ascii = ord(str[i]) # ascii value of char
        if (ascii >= 97 and ascii <= 122) or (ascii >= 65 and ascii <= 90):
            if (ascii >= 97 and ascii <= 122):
                checkbit = ascii - 96
            else:
                checkbit = ascii - 64

        # None of this can happen witout the bit vector library
        # being installed: python -c 'import bitarray; bitarray.test()'
        if checker and (checkbit << 1):
            return False
        else:
            checker |= (checkbit << 1)

    return True

"""
 String permutations
 check if string 1 is a permutations of string 2
 Easiest and fastest would be to sort strings and compare
 quicksort time: O(n log n)
"""
def is_permutation(str1, str2):

    if str1 is None or str2 is None:
        return False

    if len(str1) != len(str2):
        return False

    #sstr1 = quickSort(list(str1))
    #sstr2 = quickSort(list(str2))
    # Of course, using internal sorted function is also O(n log n)
    sstr1 = sorted(str1)
    sstr2 = sorted(str2)

    if sstr1 == sstr2:
        return True
    else:
        return False

# using a hash table can get time down to O(n)
def is_permutation_hash(str1, str2):
    # first, check if strings are same length - then...
    # add second array to hash table, collisions build linked list
    # lookup time of hash table is O(1) to O(n) if all letters point to same key
    # O(n) time to create hash table (walking array)
    # O(n) time to walk first array, then O(1) to check hash
    # removing elements from hash table as we search and match str1 to str2(hash)
    # keeping track of number of elements in hash, when done walking str1
    #   if hash count is zero at end - we have a permutation
    # total time is O(n) - yay!
    pass

"""
 UrlIfy
 Add %20 spaces to "Mr John Smith      " size 13
 assume that end of string hold enough space for space conversion e.g., ' ' to %20
 in place, time: O(n)
 Hints: read backwards to modify, count spaces before starting
"""
def urlify_spaces(str, true_len=0):

    # since we are given the true lengh, this should be defined
    # else return None
    if not true_len:
        return None

    # count spaces
    spaces = 0
    for i in range(0, true_len):
        if str[i] == " ":
            spaces += 1

    # error if not enough room at end
    # note: space is 3 chars - 1 char for space (2)
    hi = len(str) - 1
    #print "hi:{}, true_len:{} + (spaces:{} * 3))".format(hi, true_len, spaces)
    if (true_len + (spaces * 2)) != hi + 1:
        return None

    # modify
    # starting at end move everything to actual lengh
    # insert %20 as space
    # note: since going backwards, actual end index is (true_len - 1)
    #       and since range end doesn't include index defined '0' then
    #       beginning is 0 - 1
    str = list(str)
    for i in range(true_len - 1, 0 - 1, -1):
        if str[i] == " ":

            # More Pythonic - however, easier to understand below
            # remember looking between values when counting index
            # 012345678901234567
            # [Mr John SmitSmith]
            #str[hi - 2:hi + 1] = "%20"
            #hi -= 3

            str[hi] = "0"
            hi -= 1
            str[hi] = "2"
            hi -= 1
            str[hi] = "%"
            hi -= 1

        else:
            str[hi] = str[i]
            hi -= 1

    return ''.join(str)

"""
 Palindrone finder
 Hings: no need to find all letter combinations, use a hash table for O(n) time
 find all palindrones in a string and return results
 store letters in hash table by count e.g., 'a' = 2, 'b' = 4
 note that single letters will be in the center and no more than one single allowed for palindrome
 abcccccba
"""
def find_palindrones(str):

    checker = {} # dictionary
    palindrones = []

    # Blank or 1 character - automatically a palindrome
    if len(str) <= 1:
        return True

    # move letters to hash
    for c in str:
        if c in checker:
            checker[c] += 1
        else:
            checker[c] = 1

    # check for singles
    singles = 0
    for c in checker:
        if checker[c] % 2 == 1: # this is a single!
            singles += 1
        if singles > 1:
            return False

    # rebuild first half of list
    l = []
    single = ''
    for c in checker:
        if checker[c] % 2 == 1:
            # single tracked in variable, not added to list
            single = c
        else:
            # add half characters to list
            # e.g., if 4 'a', add 2 to list ['a','a']
            l.extend([c] * (checker[c] / 2))

    # variations
    lpre = get_permutations(''.join(l))
    for pre in lpre:
        palindrones.append(pre + single + pre[::-1])

    print "all those palindrones:{}".format(palindrones)

    return True # answered the question if this is a palindrone

"""
 String One Off
 compare str2 (test) to str1 (base)
 Note: 3 actions on a string: insert, remove & replace
       [a,b,c,d] [a,b,c,d,s]
       [a,b,c,d] [b,c,d]
       [a,b,c,d] [a,b,c,s]
"""
def string_one_away_same_length(str1, str2):

    count_away = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            #print "no match on str1[i]:{} to str2[i]:{}".format(str1[i], str2[i])
            count_away += 1
        if count_away > 1:
            return False

    if count_away == 1:
        return True
    else:
        return False

def string_one_away_diff_length(str1, str2):

    # compare shorter to longer
    # where s1 is scanned to compare to s2
    if len(str1) < len(str2):
        s1 = list(str1)
        s2 = list(str2)
    else:
        s1 = list(str2)
        s2 = list(str1)

    i=0
    count_away = 0

    while i < len(s1):
        if s1[i] == s2[i]:
            # all is good in the world
            # - increment i
            i += 1
        else:
            # bad things happening
            # - track buggars
            # - pop off bad value for re-comparison
            s2.pop(i)
            count_away += 1
        if count_away > 1:
            return False
    return True

def string_one_away(str1, str2):

    print "test:{} to {}".format(str1, str2)

    if not str1 or not str2:
        return False

    if len(str1) == len(str2):
        # str1 same length as str2
        return string_one_away_same_length(str1, str2)
    if len(str1) + 1 == len(str2) or len(str1) == len(str2) + 1:
        # str1 +1 longer or str2 +1 longer
        return string_one_away_diff_length(str1, str2)
    else:
        # strings cannot be +1 different at the point
        return False

"""
 String compression
 aabbbccccddddd -> a2b3c4d5
 abcd -> abcd... because it's smaller than a1b1c1d1
 beware: concantenating strings over and over ?
"""
def string_compressor_concat(chr, chr_count):

    # Returns output integer in front of all letters regardless of size
    # e.g. a = a1, aa = a2, bbb = b3

    str_out = ""

    str_out = "{}{}".format(chr, chr_count)

    return str_out

def string_compressor_concat_sized(chr, chr_count):

    # returns only when sequence of letters is > 2
    # e.g., a = a, aa = aa, bbb = b3
    # why? because aa and a2 are the same size

    str_out = ""

    if chr_count > 2:
        str_out = "{}{}".format(chr, chr_count)
    else:
        str_out = chr * chr_count

    return str_out

def string_compressor(str):

    print "string_compressor({})".format(str)

    if not str:
        return None

    str_out = ""
    chr_count = 1
    chr = str[0]

    for i in range(1, len(str)):

        if str[i] == chr:
            chr_count += 1
        else:

            str_out += string_compressor_concat(chr, chr_count)

            chr = str[i]
            chr_count = 1

    str_out += string_compressor_concat(chr, chr_count)

    # return shortest of two strings
    if len(str) < len(str_out):
        return str
    else:
        return str_out

"""
 NxN Matrix rotator
 a d g
 b e h
 c f i

 Rotate edges 90deg - top=right, right=bottom, bottom=left, left=top

 Try to do in place without extra space in O(e) Time
"""
nxn = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]

def matrix_create(n):

    # create matrix of size n

    m = []
    count = 0

    for i in range(n):
        m.append([j for j in range((n*i)+1,(n*(i+1))+1)])

    return m

def matrix_print(matrix):

    # matrix width and height might be different
    # assuming all heights are the same
    # print [0][0], [1][0], [2][0]
    # Runtime: O(n^2)

    str_out = []

    i = 0
    imax = len(matrix) - 1
    j = 0
    jmax = len(matrix[0]) - 1

    while True:

        str_out.append(matrix[i][j])

        if i == imax:
            i = 0
            j += 1
            print ' '.join(str(x).rjust(4,' ') for x in str_out)
            str_out = []
        else:
            i += 1

        if j >= len(matrix[i]):
            return

# First go at this - made sense on paper
# Note: this only does outside edge, not for multi-layers (maybe a future version)
# Runtime O(3n) or O(n)? since it runs n + n-1 + n-2
def matrix_rotate_left(m):

    if not m or len(m) != len(m[0]):
        return False;

    # Original
    print "----------------------------------"
    matrix_print(m)
    print

    """
     rotate - swap one by one all edges 90 deg counter-clockwise
    """
    levels = len(m) / 2
    mmax = len(m) - 1

    for l in range(levels):

        #print "level:{} mmax:{}".format(l,mmax)

        for i in range(l, mmax):

            #print "swap [{}][{}] for [{}][{}]".format(l,i,i,mmax)
            m[l][i], m[i][mmax] = m[i][mmax], m[l][i]
            #print "swap [{}][{}] for [{}][{}]".format(l,i,mmax,mmax-i+l)
            m[l][i], m[mmax][mmax - i + l] = m[mmax][mmax - i + l], m[l][i]
            #print "swap [{}][{}] for [{}][{}]".format(l,i,mmax-i+l,l)
            m[l][i], m[mmax - i + l][l] = m[mmax - i + l][l], m[l][i]

        mmax -= 1

    matrix_print(m)

def matrix_rotate_right(m):

    if not m or len(m) != len(m[0]):
        return False;

    # Original
    print "----------------------------------"
    matrix_print(m)
    print

    """
     rotate - swap one by one all edges 90 deg clockwise
    """
    levels = len(m) / 2
    mmax = len(m) - 1

    for l in range(levels):

        for i in range(l, mmax):

            m[i][l], m[mmax][i] = m[mmax][i], m[i][l]
            m[i][l], m[mmax - i + l][mmax] = m[mmax - i + l][mmax], m[i][l]
            m[i][l], m[l][mmax - i + l] = m[l][mmax - i + l], m[i][l]

        mmax -= 1

    matrix_print(m)

def matrix_zero_col(m,c,i=0):
    # columns example: m[i][0] = [1,0],[1,1],[1,2]...
    for j in len(i, m[c][0]):
        m[c][j] = 0

def matrix_zero_row(m,r,i=0):
    # rows example: m[0][i] = [0,1][1,1][2,1]...
    for j in len(i, m[0][r]):
        m[j][r] = 0

def matrix_zero_out(m):

    """
     Zero out rows and columns where zeros found in matrix

     x,x,x,x    x,x,0,x
     x,x,0,x -> 0,0,0,0
     x,x,x,x    x x,0,x
    """

    # defined is nxm matrix
    if not m:
        return

    print "----------------------------------"
    matrix_print(m)

    trkRowZero = False
    trkColZero = False

    # set bool for tracking row and column
    # column
    for i in range(len(m[0])):
        if m[0][i] == 0:
            trkColZero = True
            break

    # row
    for i in range(len(m)):
        if m[i][0] == 0:
            trkRowZero = True
            break

    #print "trkColZero:{} trkRowZero:{}".format(trkColZero, trkRowZero)

    # find those zeros
    # storing in tracking column and row as zeros
    for i in range(1,len(m)):
        for j in range(1,len(m[i])):
            if m[i][j] == 0:
                # found a zero - store at edges
                # left edge - [0][j]
                # top edge  - [i][0]
                m[0][j] = 0
                m[i][0] = 0

    # zero out cols (skip col 0 for now)
    for i in range(1,len(m)):
        if m[i][0] == 0:
            for j in range(len(m[i])):
                m[i][j] = 0

    # zero out rows
    # [0,1][1,1][2,1][3,1]
    for i in range(1,len(m[0])):
        if m[0][i] == 0:
            for j in range(len(m)):
                m[j][i] = 0

    # zero out tracking column
    if trkColZero is True:
        for i in range(len(m[0])):
            m[0][i] = 0

    # zero out tracking row
    if trkRowZero is True:
        for i in range(len(m)):
            m[i][0] = 0

    print "----------------------------------"
    matrix_print(m)

"""
 Is substring
 input string 1, string 2
 Runtime O(n) assuming python 'in' is O(A+B)
"""
def is_string_rotation(str1, str2):

    # concat strings (string 2 is the rotated string)
    # example: terwa + terwa = terwaterwa

    if not str1 or not str2:
        return False

    if len(str1) != len(str2):
        return False

    str_test = str2 + str2
    if str1 in str_test:
        return True

    return False

## Run Tests
# ================================================================================

# Unique Characters
#print unique_characters_in_string('abcdefghijklmnop') # answer:True
#print unique_characters_in_string('abccdefghijklmnop') # answer:False
#print unique_character_in_string_tracker('abcdefghijklmnop') # answer: True
#print unique_character_in_string_tracker('abccdefghijklmnop') # answer: False
##print unique_character_in_string_bit('abcdefghijklmnop') # answer:True
##print unique_character_in_string_bit('abccdefghijklmnop') # answer:False

# String permutation
#print is_permutation('abcde', 'edcba') # answer:True
#print is_permutation('abcde', 'edxba') # answer:False

# URL-ify
#print "'{}'".format(urlify_spaces('Mr John Smith    ', 13))

# Palindrones
#print find_palindrones('tacocat')

# One Away
#print string_one_away('abcd','abcd') # answer: False
#print string_one_away('abcd','ebcd') # answer: True
#print string_one_away('abcd','eecd') # answer: False
#print string_one_away('xx','x')
#print string_one_away('abcd','xabcd') # answer: True
#print string_one_away('abcd','axbcd') # answer: True
#print string_one_away('abcd','abcdx') # answer: True

# String Compression
#print string_compressor('')
#print string_compressor('a')
#print string_compressor('ab')
#print string_compressor('abbcccddddeeeee')
#print string_compressor('abbcccddddeeeeeffffffffffffffffffffffffffffffffffffffffffffffffff')

# N Matrix rotator (patater)
#matrix_rotate_left(matrix_create(4))
#matrix_rotate_right(matrix_create(4))

# 0 Matrix - zero out rows/cols with zeros
#zm = [[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
#matrix_zero_out(zm)

# String is substring
print is_string_rotation('waterbottle', 'erbottlewat') # answer: True
print is_string_rotation('shuzbut', 'nanonano') # answer: False
