"""

Data Structure: Double Linked Lists

    linkedList.root <--> node.data, node.next <--> node.data, node.next <--> etc...

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
            # root is new node with next of node in root and previous of next in root
            add_node = Node(data, self.root)
            if self.root:
                self.root.prev = add_node
            self.root = add_node
            self.size += 1

    def remove(self, data):
        """
         find and remove node
         decrement self.size

         (prev)|prev|data|next| <--> (temp)|prev|data|next| <--> (next)|prev|data|next|
        """
        temp = self.root
        while temp:

            if temp.data == data:

                if temp.next:
                    temp.next.prev = temp.prev

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.root = temp.next
                self.size -= 1
                return True

            temp = temp.next

        return False

class Node(object):

    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next

if __name__ == '__main__':

    llist = linkedList()
    llist.add(5)
    llist.add(6)
    llist.add(7)
    llist.add(8)
    llist.add(9)
    llist.add(10)

    print "size:{}".format(llist.get_size())

    print "removed:{}".format(llist.remove(10))
    print "removed:{}".format(llist.remove(9))
    print "removed:{}".format(llist.remove(5))


    print "size:{}".format(llist.get_size())

    findNode = llist.find(5)
    if findNode:
        if findNode.next:
            print "found! - data:{}, next:{}".format(findNode.data, findNode.next.data)
        else:
            print "found! - data:{}, next:None".format(findNode.data)

    print "linked list..."
    llist.printList()
