"""
 String permutations (exhaustive) - runtime O(n * n!)

 runtime - O(n * n!) to O(n^2 * n!) e.g. @ 3 = O(3 * 6) = 18 to O(9 * 6) = 54 ? (actual tested time is 15)

 Test: ABC

       A BC - AB C - ABC
              AC B - ACB
 ABC - B AC - BA C - BAC
              BC A - BCA
       C AB - CA B - CAB
              CB A - CBA
"""

def recPermutate(soFar, rest):
    #print "recPermutate({}, {})".format(soFar, rest)
    if len(rest) == 0:
        print "Permutation:{}".format(soFar)
    else:
        for i in xrange(len(rest)):
            rems = rest[0:i]
            reme = rest[i+1:len(rest)]
            rem = rems + reme
            nxt = soFar + rest[i]
            print "recPermutate i:{} rest:{} rems:{} reme:{} rem:{} nxt:{}".format(i, rest, rems, reme, rem, nxt)
            recPermutate(nxt, rem)

recPermutate("","abc")
