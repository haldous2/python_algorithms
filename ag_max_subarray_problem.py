"""

 Max subarray (problems)

 ** find max value from a subset of continuous values added together in an array

"""

import sys

"""
 Recursively break problem into smaller bits and compare max back up the chain
 Time: O(nlog n)
"""
def max_subarray(arr=[]):

    print arr

    # base case - return this as max for this level
    if len(arr) == 1:
        return arr[0]

    # begin divide and conquer
    m = len(arr)/2
    left_max_sum = max_subarray(arr[0:m])
    right_max_sum = max_subarray(arr[m:])

    #print "{} left_max_sum:{} right_max_sum:{}".format(arr,left_max_sum, right_max_sum)

    left_sum = -sys.maxint
    right_sum = -sys.maxint

    # right half - find max
    sum = 0
    for i in range(m, len(arr)):
        sum += arr[i]
        right_sum = max(right_sum, sum)

    # left half - find max
    # note: since range is end - 1, and since we need to go to zero end is -1 (0 + -1)
    sum = 0
    for i in range(m-1, -1, -1):
        sum += arr[i]
        left_sum = max(left_sum, sum)

    # returning combined sub, sub max all the way up the chain
    ans = max(left_max_sum, right_max_sum)
    result = max(ans, left_sum + right_sum)
    print "=== result:{} ===".format(result)
    return result

"""
 Kadane method
 Run through array, add each element to the list until less than zero. Keep going to the end
 keep track of max value along the way - easy peasy
 Time: O(n)
"""
def max_subarray_kadane(arr=[]):
	max = 0
	currentMax = 0
	for i in range(len(arr)):
		currentMax += arr[i]
		if currentMax < 0:
			currentMax = 0
		if max < currentMax:
			max = currentMax
	return max

# Test
l = [10,5,3,-10,9,6,-8,2,11,-1,1] #
#l = [1,-3,2,-5,7,6,-1,-4,11,-23] # answer:19
print "max:{}".format(max_subarray_kadane(l))
print "max:{}".format(max_subarray(l))
