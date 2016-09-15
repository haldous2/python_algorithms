"""
 Sort: Bubble Sort

 Time: O(n^2) Space: O(n)

 Example:

 [4,3,2,1] first loop j = index(1 to 3) -> [3,2,1] 'number of times the outer executes, n-1 times will be sorted'

 inner loop - i = index(0 to 4 - j:1) -> [4,3,2]
 i = 0, bubble up 4 - compare to neighbor ... is 4 > 3? Yes - swap 4x3
 [3,4,2,1]
 i = 1, bubble up 4 - 4 > 2? Yes - swap 4x2
 [3,2,4,1]
 i = 2, bubble up 4 - 4 > 1? Yes - swap 4x1
 [3,2,1,4]

 increment j - now i = index(0 to 4 - j:2) ->[3,2] since last element is already sorted [4]
 i = 0, bubble up 3 - 3 > 2? Yes - swap 3x2
 [2,3,1,4]
 i = 1, bubble up 3 - 3 > 1? Yes - swap 3x1
 [2,1,3,4]

 increment j - now i = index(0 to 4 - j:3) -> [2] since last elements are already sorted [3,4]
 i = 0, bubble up 2 - 2 > 1 ? Yes - swap 2x1
 [1,2,3,4]

 increment j - now i = index(0 to 4 - j:4) -> [] since last elements are already sorted [2,3,4]
 i doesn't loop - nothing swapped - sorted flag not set to true, break out of loop .. we're done!


"""

def bubbleSort(arr=[]):
    for j in range (1,len(arr)):
        print "j:{}".format(j)
        bubbleUp = False
        for i in range (0,len(arr)-j):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                bubbleUp = True
        if not bubbleUp:
            return

l = [4,3,2,1]
#l = [1,2,3,4]
#l = [1]
#l = [2,1]
bubbleSort(l)
print l
