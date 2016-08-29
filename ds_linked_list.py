"""

Data Structure: Linked Lists

    linkedList.root --> node.data, node.next --> node.data, node.next --> etc...

    What are linked lists good for ?

	Big O:
	Access  Search  Insert  Delete  Access  Search  Insert  Deletion  Space
	O(n)    O(n)    O(1)    O(1)    O(n)    O(n)    O(1)    O(1)      O(n)

	Note: deleting is O(1) after you find the node to delete which would take O(n) time

"""

class linkedList(object):

    """
     The root object
     methods:
      getsize()
      find(data)
      add(data)
      remove(data)
    """

    def __init__(self, next = None):
        self.root = next
        self.size = 0

    def printList(self):
        # loop through all linked nodes and return result
        temp = self.root
        while temp:
            print temp.data
            temp = temp.next

    def get_size(self):
        return self.size

    def find(self, data):
        temp = self.root
        while temp:
            if temp.data == data:
                # found it return the node
                return temp
            temp = temp.next
        return None

    def add(self, data):
        """
         new node goes in front @ self.root, new_node.next = self.root
         increment self.size
        """
        if data:
            self.root = Node(data, self.root)
            self.size += 1

    def remove(self, data):
        """
         find and remove node
         decrement self.size

         (temp)|prev|data|next| --> (next)|prev|data|next|
        """
        prev = None
        temp = self.root
        while temp:

            if temp.data == data:
                if prev:
                    prev.next = temp.next
                else:
                    self.root = temp.next
                self.size -= 1
                return True

            prev = temp
            temp = temp.next

        return False

        # # version 001
        # prev = None
        # temp = self.root
        # while temp:
        #     if temp.data == data:
        #         # found it , connect previous and next
        #         if prev:
        #             # has previous, not root
        #             if temp.next:
        #                 # found a next, connect prev.next to temp.next - this disconnects temp
        #                 prev.next = temp.next
        #                 temp = None
        #                 self.size -= 1
        #                 return True
        #             else:
        #                 # no next, this is the end - reset prev.next
        #                 prev.next = None
        #                 temp = None
        #                 self.size -= 1
        #                 return True
        #         else:
        #             # no previous, this is root
        #             if temp.next:
        #                 # connect root to next
        #                 self.root = temp.next
        #                 temp = None
        #                 self.size -= 1
        #                 return True
        #             else:
        #                 # no next, removing root
        #                 self.root = None
        #                 temp = None
        #                 self.size -= 1
        #                 return True
        #
        #     prev = temp
        #     temp = temp.next
        #
        # # nothing removed
        # return False

class Node(object):

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    # get it and set it
    def get_next (self):
        return self.next

    def set_next (self, n):
        self.next = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

if __name__ == '__main__':

    llist = linkedList()
    llist.add(5)
    llist.add(6)
    llist.add(7)
    llist.add(8)
    llist.add(9)
    llist.add(10)

    print "size:{}".format(llist.get_size())

    print "removed:{}".format(llist.remove(5))
    #print "removed:{}".format(llist.remove(5))

    print "size:{}".format(llist.get_size())

    findNode = llist.find(5)
    if findNode:
        if findNode.next:
            print "found! - data:{}, next:{}".format(findNode.data, findNode.next.data)
        else:
            print "found! - data:{}, next:None".format(findNode.data)

    print "linked list..."
    llist.printList()
