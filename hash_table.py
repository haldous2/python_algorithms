#!/usr/local/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

import random
import resource

# Print necessary headers.
print "Content-Type: text/html\n\n"

"""
Hash Tables

Using lists and lists within lists
Note: could just use a dictionary, what fun would that be ?

when adding, will always be a leaf - just follow the trail left or right until a spot is open
when deleting, 3 scenarios will decide how element is removed
  1. has two elements attached (is a node)
  2. has one element attached
  3. has no elements (is a leaf
  )
"""

class hashMap(object):

    def __init__(self):
        self.size = 64
        self.table = [None] * self.size

        ## test
        self.table[3] = [['Eric', 'Westman']]

    def _get_hash(self, key):
        hash = 0
        if key:
            for c in str(key):
                hash += ord(c)
            return hash % self.size
        else:
            return None

    def _get_value(self, key):
        hash = self._get_hash(key)
        if hash is None:
            return None
        if self.table[hash] is not None:
            # traverse data in hash column
            for data in self.table[hash]:
                if data[0] == key:
                    return data[1]
        else:
            return None

    def add(self, key, value):
        hash = self._get_hash(key)
        if hash is None:
            return None
        if self.table[hash] is None:
            # no data - add new list
            self.table[hash] = [[key, value]]
        else:
            # list(s) found - look for dupicates, add or update
            i = 0
            dup = False
            for data in self.table[hash]:
                if data[0] == key:
                    dup = True
                    break
                i += 1
            if dup is True:
                # updating
                self.table[hash][i] = [key, value]
            else:
                # adding
                self.table[hash].append([key, value])

    def delete(self, key):
        hash = self._get_hash(key)
        if hash is None:
            return None
        if self.table[hash] is not None:
            i = 0
            for data in self.table[hash]:
                ## need to remove a list inside a list
                if data[0] == key:
                    self.table[hash].pop(i)
                    break
                i += 1
            # reset column
            if len(self.table[hash]) == 0:
                self.table[hash] = None

        else:
            return None

    def show(self):
        i = 0
        for hash in self.table:
            if hash is not None:
                print "[{:03}]--{}".format(i, hash)
            i += 1

hs = hashMap()

hs.add("Cire", "Delish")
hs.add("Eric", "RovaLova")
hs.add("Eric", "Vestmer")
hs.add("Bob", "Zabowsky")
hs.add("George", "Carlin")

hs.delete("Eric")

print hs._get_value('Eric')
print hs._get_value('Bob')
print hs._get_value('George')

hs.show()
