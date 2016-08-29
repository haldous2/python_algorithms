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

Hash a key to index value in list (array index)
Store key, value pair in a list
Update key, value pairs when match on hash and item
Insert new list for all collision key, value pairs

"""

class hashMap(object):

    def __init__(self):
        self.size = 6
        self.table = [None] * self.size

        ## test
        #self.table[3] = [['Eric', 'Westman']]

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

            dup = False

            # range method
            for i in range(0, len(self.table[hash])):
                if self.table[hash][i][0] == key:
                    #print "duplicate data{} data.0:{} = key:{}".format(self.table[hash][i],self.table[hash][i][0],key)
                    dup = True
                    break

            # counter method
            i = 0
            for data in self.table[hash]:
                if data[0] == key:
                    #print "duplicate data{} data.0:{} = key:{}".format(data,data[0],key)
                    dup = True
                    break
                i += 1

            if dup is True:
                # updating
                #print "updating:{}@{}".format(key,i)
                self.table[hash][i] = [key, value]
            else:
                # adding
                #print "adding:{}".format(key)
                self.table[hash].append([key, value])

    def delete(self, key):
        hash = self._get_hash(key)
        if hash is None:
            return None
        if self.table[hash] is not None:

            # range method
            for i in range(0, len(self.table[hash])):
                #print "delete:{},{},{}".format(hash, i, self.table[hash][i][0])
                if self.table[hash][i][0] == key:
                    self.table[hash].pop(i)
                    break

            # counter method
            #i = 0
            #for data in self.table[hash]:
                ## need to remove a list inside a list
            #    if data[0] == key:
            #        self.table[hash].pop(i)
            #        break
            #    i += 1

            # reset column
            if len(self.table[hash]) == 0:
                self.table[hash] = None

        else:
            return None

    def show(self):
        i = 0
        for i in range(0, len(self.table)):
            if self.table[i] is not None:
                print "[{:03}]--{}".format(i, self.table[i])

hs = hashMap()

hs.add("Irce", "Mirksy")
hs.add("Cire", "Delish")
hs.add("Eric", "RovaLova")
hs.add("Eric", "Vestmer")
hs.add("Bob", "Zabowsky")
hs.add("George", "Carlin")

#hs.delete("Eric")

print hs._get_value('Bob')

hs.show()
