"""
 Merge Sort

 Divide and conquer: split array in half down to one element then recurse back 'merge (sort)' each piece of array

 Runtime: average - O(nlogn) worst O(nlogn) Space: O(n)

 """

def merge(arr=[],left=[],right=[]):
    nL = len(left)
    nR = len(right)
    i=0
    j=0
    k=0
    while i < nL and j < nR:
        if left[i] < right[j]:
            arr[k] = left[i]
            i+=1
            k+=1
        else:
            arr[k] = right[j]
            j+=1
            k+=1
    # cycle through what's remaining, either right OR left will have some stragglers
    while i < nL:
        arr[k] = left[i]
        i+=1
        k+=1
    while j < nR:
        arr[k] = right[j]
        j+=1
        k+=1

def mergesort(arr=[]):
    #print "mergesort arr:{}".format(arr)
    if len(arr) < 2:
        return
    mid = int(len(arr) / 2)
    """
     l=[1,2,3,4,5], mid=2 aL = l[0:2]->[1,2] aR = l[2:]->[3,4,5]

     breakdown: since indices point between characters - 0 to 2 returns 1,2... 2 to 5 returns 3,4,5
     slice[start:end]
     [|1|2|3|4|5|]
      0 1 2 3 4 5
    """
    aL = arr[0:mid]
    aR = arr[mid:]
    mergesort(aL)
    mergesort(aR)
    merge(arr,aL,aR)

    return arr

l = [7,5,2,1,3,4,6,9,10,8]
print l
print mergesort(l)
