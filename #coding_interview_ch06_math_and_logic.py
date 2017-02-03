"""
Cracking the coding interview
Practice questions
Part 06. Math & Logic - Primes, Probability
"""

"""
Primes:

    Prime is > 1 and only divisible by itself and 1
    e.g. 2, 3, 5, 7, 9, 11, 15 etc..
    testing if prime algorithm:
        int(a)*int(b) = int(c) e.g. 2 * 4 = 8
        either a or b is <= sqrt(int(c)) otherwise we'll overshoot the result
        when testing if prime, only need to look up to <= sqrt(goal)
           e.g. for i in range(2, sqrt(n)):
                   if i % n == 0:
                       return "Not Prime"

    Other methods up to 100: Sieve of Erathanoeos

Sieve of Eratosthenes:

    in a grid from 1 to n (a list or array substituted)
    starting from 2, mark off every 2nd element (2 * 2)
    then from the next element 3 mark off every third (3 * 2)
    then from the next element n mark off every n (n * 3) until goal reached
    note: using the square-root rule for depth to 'mark-off' applies
       e.g.

Probability:


"""

def primeIsValidUtil(n):
    """
    input n: positive int > 2
    output bool: True is prime, False is not prime

    runtime O(sqrt(n))
    """

    import math

    # housecleaning
    if not n:
        return None
    if type(n) is not int:
        return None
    if n < 2:
        return None

    # is it prime
    # e.g. 4 not prime 4 % 2 = 0
    #      100 not prime 100 % 10 = 0
    sqrt_of_n = int(math.sqrt(n))

    # starting @ 2, therefore 2 and 3 won't be counted
    #   with starting range of (2, 2) since int(sqrt(2 and 3)) = 1
    for i in range(2, sqrt_of_n + 1):
        print i
        if n % i == 0:
            return False
    return True

def primeIsValid(n):
    print "{} is valid prime number:{}".format(n, primeIsValidUtil(n))

# primeIsValid(1)
# primeIsValid(2)
# primeIsValid(3)
# primeIsValid(4)
# primeIsValid(5)
# primeIsValid(6)
# primeIsValid(100)

def primeSieveOfEratosthenesUtil(n):
    """
    input n
    output bool if prime
    this generates a list of primes up to max n
    max n could be the prime we are looking for

    total runtime O(sqrt(n)) + O(nloglogn) or just O(nloglogn)
    """

    import math

    # assume all are prime - setting to ones
    # noting that 0 & 1 wont be included in range
    primes = [1] * (n + 1)

    # only looking up to sqrt of n
    # runtime of first loop O(sqrt(n))
    # [0,1,2,3,4,5,6,7,8,9,10] where n = 10 (max)
    # starting at index with int(sqrt(10)) = 3 .. so look in range to <= 3
    for i in xrange (2, int(math.sqrt(n)) + 1):

        # loop through and mark array
        # 2*2=4, 2*3=6, 2*4=8, 2*5=10 etc..
        # 3*2=6, 3*3=9 etc..
        # n/2+n/3+n/4.... runtime O(nloglogn)

        # n=10 n/2=5, n/3=3, n/4=2, n/5=2etc...
        for j in xrange(2, int(n/i) + 1):
            primes[i*j] = 0

    #print primes

    if primes[n] == 1:
        return True
    else:
        return False

def primeSieveOfEratosthenes(n):
    print "{} is valid prime number:{}".format(n, primeSieveOfEratosthenesUtil(n))

#primeSieveOfEratosthenes(10)
#primeSieveOfEratosthenes(100)
#primeSieveOfEratosthenes(524287)

def probabilityGender():
    """
    over a period of births in a family
    calculate the number of boys to girls
    when a girl is born, stop having children
    display results as boys/girls as a ratio

    Note: after running - I'm surprised that the boys to girls ratios are so close
          and that girls outnumber boys. Thinking that G, BG, BBG, BBBG, BBBBG might prevail
    """

    import random

    total_boys = 0
    total_girls = 0

    for i in xrange(0, 1000000):

        sub_boys = 0

        while True:

            if int(random.getrandbits(1)) == 1:    # runs b&g about evenly favoring g
            #if random.randint(0,1) == 1:            # runs b&g about evenly favoring g
                sub_boys += 1
            else:
                total_boys += sub_boys
                total_girls += 1
                break

    if total_boys > total_girls:
        sub_data = " with {} more boys than girls".format(total_boys - total_girls)
    else:
        sub_data = " with {} more girls than boys".format(total_girls - total_boys)

    print "ratio of boys to girls is {}/{} ... {}".format(total_boys, total_girls, sub_data)

#probabilityGender()

"""
Egg drop counter
"""

def countRangeNPlusOne():

    count = 0
    total_count = 0

    for i in xrange(1, 100):

        count = count + 1
        total_count += count
        print count, total_count

        if total_count >= 100:
            break

#countRangeNPlusOne()

"""
Open & close lockers

I'm thinking that all prime numbers will be in 'c:closed' state
"""

def lockersProblem():

    lockers = ['o'] * 101
    lockers[0] = 'x'

    for i in range(2, 101):

        for j in range(i, 101, i):

            #print j

            if lockers[j] == 'o':
                lockers[j] = 'c'
            else:
                lockers[j] = 'o'

    # note that squares of 1, 2, 3, 4 etc.. are the open lockers
    for i in range(1, 101):
        if lockers[i] == 'o':
            print "{} is open".format(i)

    print "number of open lockers:", lockers.count('o')
    #print lockers

#lockersProblem()

"""
1000 bottles - can't drink any of them

Find the poisioned bottle

Store as bits in strips
e.g.

            bottle:    1  2  3  4  5  6  7  8  9  10

  strips  1:(bit 1)    1     1     1     1     1
          2:(bit 2)       1  1        1  1        1
          3:(bit 4)             1  1  1  1
          4:(bit 8)                         1  1  1
          5:(bit 16)
          6:(bit 32)
          7:(bit 64)
          8:(bit 128)
          9:(bit 256)
         10:(bit 512)

I am personally blown away by the results. One test, 7 days - set everything up as binary
and there isn't any duplication. Just match binary results up to strips variation and done

"""
def bottlesFindOne(n):
    """
    where n: is the bottle that is poisioned (of course finding something that we already know is kind of ridiculous)
    """

    # 10 strips with lists to hold bits pertaining to bottles
    strips = [[] for x in range(0, 10)]

    bottles = 1000

    def in_strips(bottle_test):
        """
        bottle_test: bottle number in range 1 to bottles (positive int)
        """
        strips_positive = []
        if bottle_test:
            # need all bits of bottle_test
            for j in range(0, 10):
                bit = bottle_test & (1<<j)
                if bit > 0:
                    strips_positive.append(j)

        # return sorted list of strips
        return strips_positive

    # visual representation of bottles (drops) to test strips
    # for i in range(1, bottles + 1):
    #
    #     # walk through first 10 bits - store in proper strips
    #     for j in range(0, 10):
    #
    #         # mask to extract which bits exist in i.bit
    #         bit = i & (1<<j)
    #
    #         if bit > 0:
    #
    #             strips[j].append(i)

    # for i in range(0, 10):
    #     print "strips[{}].count:{}".format(i, len(strips[i]))

    strips_positive_known = in_strips(n)
    # print strips_positive_known

    # look for all bottles that might match up to strips positive
    number_of_matches = 0
    for i in range(1, bottles + 1):
        strips_compare = in_strips(i)
        if strips_compare == strips_positive_known:
            number_of_matches += 1
            if number_of_matches > 1:
                print "WE HAVE A PROBLEM HOUSTON!!!"
            print "could be bottle:{} in:{} match:{}".format(i, strips_compare, strips_positive_known)

# for i in range(1, 100):
#     bottlesFindOne(i)
