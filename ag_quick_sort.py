#!/usr/local/bin/python

# Portions of this code contributed by Mohit Kumra

# Turn on debug mode.
import cgitb
cgitb.enable()

import random
import resource

# Print necessary headers.
print "Content-Type: text/html\n\n"

"""
 QuickSort - recursive

 Sort an array by partitioning

 This quick-sort finds a random value in the array and places it at the end as pivot when partitioning

 Do: Last element is partition, find elements starting from left, less than pivot.
     When less than pivot found, increment low and swap low with current
     When current reaches the pivot, stop and move pivot to low
     Repeat until low increments to end

"""

"""
 qs partition - recursive
"""
def partition(arr,low,high):

	print "Memory Partitioning MB:{:4d}<br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

	i = low

	## pick a random and move to high
	randIdx = random.randrange(low,high + 1)
	arr[randIdx],arr[high] = arr[high],arr[randIdx]

	pivot = arr[high]	 # pivot from high
	#print "(%s,%s,%s) random:%s<br/>" %(arr,low,high,random.randrange(low,high + 1))

	for j in range(low , high):

		# If current element is smaller than or
		# equal to pivot
		if arr[j] <= pivot:

			# swap elements and increment wall
			arr[i],arr[j] = arr[j],arr[i]
			i += 1

	# Move pivot to wall
	arr[i],arr[high] = arr[high],arr[i]
	return ( i )

# Function to do Quick sort
def quickSort(arr,low,high):

	if low < high:

		# pi is partitioning index, arr[p] is now
		# at right place
		pi = partition(arr,low,high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

print "Memory Start MB:{:4d}<br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

lstTest = [4,6,3,2,1,9,7]
lstTest = [9,7,6,4,3,2,1]
lstTest = [1,2,3,4,6,7,9]
lstTest = random.sample(range(1000), 1000)

print "Memory Init Data MB:{:4d}<br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
quickSort(lstTest, 0, len(lstTest) - 1)
print "Memory End MB:{:4d}<br/>\n".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
print "%s<br/>" % lstTest[0:25]
