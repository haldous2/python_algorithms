#!/usr/local/bin/python

# Turn on debug mode. (for html mode)
#import cgitb
#cgitb.enable()

import sys
import random
import resource
from collections import deque

# Print necessary headers.
#print "Content-Type: text/html\n\n"

"""
Binary Tree Search

Big-O Average: O(log(n)) Worst: O(n) Space: O(n)

Adding: will always be a leaf - just follow the trail left or right until a spot is open

Deleting: 3 scenarios will decide how element is removed
  1. has no left or right nodes (is a leaf node)
     --> found node is removed
  2. has a left or right node (is a root node)
     --> found node is removed, said left or right node moves up to root
  3. has two nodes attached (is a root node)
     --> replace root with lowest value in right node
         .. start in right node, iterate through lefts until end (a leaf)
         .. which should be the lowest on the right

Search: follow nodes down by layout rules smaller nodes on the left, larger on the right

Traversal:

     Preorder
      Root, left, right

     Inorder
      Left, root, right

     Postorder
      left, right, root

Note: Tree vs min or max Heap
      Tree is ordered and best for searching @ O(logN) time. Insert time O(logN)
      A Heap is best for finding the min and max value @ O(1)time. Insert time O(logN)

"""

class Node(object):

    def __init__(self, val):
        self.value = val    # value of Node - root, left or right
        self.left = None    # Node object for left
        self.right = None   # Node object for right

    def insert(self, data):
        if self.value == data:
            # this value already exists
            # don't allow duplicates
            return False
        elif data < self.value:
            # insert left of root
            if self.left:
                # already has left
                # insert data into that left child
                return self.left.insert(data)
            else:
                # add a new node with data as the left child
                self.left = Node(data)
                return True
        else:
            # insert right of root
            if self.right:
                # already has right
                # insert data into that right child
                return self.right.insert(data)
            else:
                # add a new node with data as the right child
                self.right = Node(data)
                return True

    def findNode(self, data):
        # return Node if found
        #        False if not
        if self.value == data:
            return self
        elif data < self.value:
            if self.left:
                # search the left node recursively
                return self.left.findNode(data)
            else:
                # no more nodes to search
                # didn't find the data
                return False
        else:
            if self.right:
                # search the right node recursively
                return self.right.findNode(data)
            else:
                # no more nodes to search
                # didn't find the data
                return None

    def findMin(self):
        if self.left:
            return self.left.findMin()
        else:
            # return root value if no left or no more left nodes
            return self.value

    def preOrder(self):
        # pre order: root, left, right
        if self:
            print (str(self.value))
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()

    def inOrder(self):
        # in order: left, root, right
        if self:
            if self.left:
                self.left.inOrder()
            print (str(self.value))
            if self.right:
                self.right.inOrder()

    def postOrder(self):
        # post order: left, right, root
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print (str(self.value))

class Tree(object):

    def __init__(self):
        self.root = None    # store root Node here

    def insert(self, data):
        if self.root:
            # insert recursively to Node.insert
            return self.root.insert(data)
        else:
            # initialize new node to root
            self.root = Node(data)
            return True

    def test(self, data):

        # root!
        print "********** TESTING **********"
        print "looking for:{}".format(data)

        self.traverse(self.root)

        # Not the root, apply regular rules
        # Keep track of parent in case we need to reattach
        # if has parent, then isn't the root - otherwise ... root!
        parent = None
        current = self.root
        node = None
        while current:

            # root is the node
            if data == current.value:
                node = current
                break

            # the parent, little left or right couldn't exist without the parent
            parent = current

            # let's find that data, gather up all that data
            if data < current.value:
                if current.left:
                    current = current.left
                    if current.value == data:
                        node = current
                        break
                else:
                    break
            else:
                if current.right:
                    current = current.right
                    if current.value == data:
                        node = current
                        break
                else:
                    break

        if node:

            print "node found! value:{}".format(node.value)
            if parent is None:
                print "no parent - this is the ROOT node!"
            else:
                print "parent value:{}".format(parent.value)

            if node.left and node.right:

                ## Test Node 85

                print "node has left:{} and right:{}".format(node.left.value, node.right.value)

                # find minimum value in right subtree - start in right, traverse all left to end
                # keep track of previous in case we need to reattach
                delNodeParent = node
                delNode = node.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left

                print "delNode (lowest in right) is:{} with a parent @:{}".format(delNode.value, delNodeParent.value)

                # move delNode to found node (the node we're deleting)
                print "set node:{} = delNode:{}".format(node.value, delNode.value)
                node.value = delNode.value

                # status of delNode
                # shouldn't have any left nodes since we found the min
                if delNode.right:
                    # might have a right node though, this is where we'd connect delnode.right to parent.left or parent.right
                    if delNode.value < delNodeParent.value:
                        print "set delNodeParent.left:{} = delNode.right:{}".format(delNodeParent.left.value, delNode.right.value)
                        delNodeParent.left = delNode.right
                    else:
                        print "set delNodeParent.right:{} = delNode.right:{}".format(delNodeParent.right.value, delNode.right.value)
                        delNodeParent.right = delNode.right
                else:
                    # if no right node in delNode, set parent.left or parent.right to None
                    if delNode.value < delNodeParent.value:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None

                # **cleanup - remove delNode
                delNode = None

            elif node.left:

                print "node has left:{}".format(node.left.value)
                if parent is None:
                    # root node - move left to root
                    self.root = node.left
                else:
                    # sub node - set parent left or right to node.left
                    #if node.left.value < node.value:
                    if node.value < parent.value:
                        parent.left = node.left
                    else:
                        parent.right = node.left

            elif node.right:

                print "node has right:{}".format(node.right.value)
                if parent is None:
                    # root node - move right to root
                    self.root = node.right
                else:
                    # sub node - set parent left or right to node.right
                    if node.value < parent.value:
                        parent.left = node.right
                    else:
                        parent.right = node.right

            else:

                print "node doesn't have any right or left nodes"
                if parent is None:
                    self.root = None
                else:
                    if node.value < parent.value:
                        parent.left = None
                    else:
                        parent.right = None

        else:
            print "not found - wa, wa, waaaaa"

        self.traverse(self.root)

        print "*****************************"

    # Delete node by rules of BST - recursively
    def rDelete(self, data):
        self.rDelete_util(self.root, data)

    def rDelete_util(self, node, data):
        print "Deleting:{}".format(data)
        if node is None:
            return node
        elif data < node.value:
            # go left and left links reordered in this step
            node.left = self.rDelete_util(node.left, data)
        elif data > node.value:
            # go right and right links reordered in this step
            node.right = self.rDelete_util(node.right, data)
        else:
            if node.left is None and node.right is None:
                # no children
                node = None
            elif node.left is None:
                # only right child
                node = node.right
            elif node.right is None:
                # only left child
                node = node.left
            else:
                # has right and left children
                min = self.findMin(node.right)
                node.value = min.value
                print "setting {}={}".format(node.value, min.value)
                print "delete {}".format(min.value)
                # remove and reorder right link
                node.right = self.rDelete_util(node.right, min.value)

        if node is None:
            print "returning node:None"
        else:
            print "returning node:{}".format(node.value)
        return node

    # Delete node iteratively - this is a mess!
    def delete(self, data):

        # Note the root, apply regular rules
        # Keep track of parent in case we need to reattach
        # if has parent, then isn't the root - otherwise ... root!
        parent = self.root
        current = self.root
        node = None
        while current:

            # root is the node
            if data == current.value:
                node = current
                break

            # the parent, left or right couldn't exist without the parent
            parent = current

            # let's find that data, gather up all that data
            if data < current.value:
                if current.left:
                    current = current.left
                    if current.value == data:
                        node = current
                        break
                else:
                    break
            else:
                if current.right:
                    current = current.right
                    if current.value == data:
                        node = current
                        break
                else:
                    break

        if node:

            if node.left and node.right:

                # find minimum value in right subtree - start in right, traverse all left to end
                # keep track of previous in case we need to reattach
                delNodeParent = node
                delNode = node.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left

                # move delNode to found node (the node we're deleting)
                node.value = delNode.value

                # status of delNode
                # shouldn't have any left nodes since we found the min
                if delNode.right:
                    # might have a right node though, this is where we'd connect delnode.right to parent.left or parent.right
                    if delNode.value < delNodeParent.value:
                        delNodeParent.left = delNode.right
                    else:
                        delNodeParent.right = delNode.right
                else:
                    # if no right node in delNode, set parent.left or parent.right to None
                    if delNode.value < delNodeParent.value:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None
                delNode = None
            elif node.left:
                if parent is None:
                    # root node - move left to root
                    self.root = node.left
                else:
                    # sub node - set parent left or right to node.left
                    if node.value < parent.value:
                        parent.left = node.left
                    else:
                        parent.right = node.left
            elif node.right:
                if parent is None:
                    # root node - move right to root
                    self.root = node.right
                else:
                    # sub node - set parent left or right to node.right
                    if node.value < parent.value:
                        parent.left = node.right
                    else:
                        parent.right = node.right
            else:
                # Leaf node - remove links
                if parent is None:
                    self.root = None
                else:
                    if node.value < parent.value:
                        parent.left = None
                    else:
                        parent.right = None
            return True
        else:
            return False

    def successorInOrder(self, data):
        node = self.findNode(data)
        if node is None:
            return None
        if node.right is not None:
            # return minimum from right - dunzo
            return self.findMin(node.right)
        else:
            # no right leg, gotta look for the ancesor
            # connected to left leg in O(h) time
            current = self.root
            successor = None
            while current is not node:
                if node.value < current.value:
                    # looking left - this is an ancestor
                    successor = current
                    current = current.left
                else:
                    # looking right
                    current = current.right
            return successor

    def predecessorInOrder(self, data):
        node = self.findNode(data)
        if node is None:
            return None
        if node.left is not None:
            return node.left
        else:
            return None

    def findNode(self, data):
        if self.root:
            return self.root.findNode(data)
        else:
            return False

    def findMin(self, node):
        # find iteratively in node
        if node:
            current = node
        elif self.root:
            current = self.root
        else:
            return False

        while current.left is not None:
            current = current.left
        return current

    def findMax(self):
        # find iteratively in node
        if self.root:
            current = self.root
            while current.right:
                current = current.right
            return current.value
        else:
            return False

    def isBST(self, node, min=-sys.maxint - 1, max=sys.maxint):
        """
         Setting ranges of min and max - lookup time is O(n)

             -inf to inf [100]
                         /  \
          -inf to 100 [98]  [101] 100 to inf
                      /  \
        -inf to 98 [97]  [99] 98 to 100
        """
        if node is None:
            return True
        if (node.value > min and
            node.value < max and
            self.isBST(node.left, min, node.value) and
            self.isBST(node.right, node.value, max)):
            return True
        else:
            return False

    def traverse(self, rootnode):

        if rootnode is None:

            print "no Nodes to see here - they're all gone"

        else:

            thislevel = [rootnode]
            while thislevel:
                nextlevel = list()
                for n in thislevel:
                    print n.value,
                    if n.left: nextlevel.append(n.left)
                    if n.right: nextlevel.append(n.right)
                print
                thislevel = nextlevel

    def inOrder(self, node=None):
        if node is None:
            self.root.inOrder()
        else:
            node.inOrder()

    def preOrder(self):
        self.root.preOrder()

    def postOrder(self):
        self.root.postOrder()


## Insert order 100,102,103,70,65,85,84,95,64,93,97

#tr = Tree()

#tr.insert(100)
#tr.insert(102)
#tr.insert(103)
#tr.insert(70)
#tr.insert(65)
#tr.insert(85)
#tr.insert(84)
#tr.insert(95)
#tr.insert(64)
#tr.insert(93)
#tr.insert(97)

def test_remove_not_found():
    tr = Tree()
    tr.insert(100)  #root
    tr.test(10)

def test_remove_root_with_no_leaf():
    tr = Tree()
    tr.insert(100)  #root
    tr.test(100)

def test_remove_root_with_left_leaf_only():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.test(100)

def test_remove_root_with_right_leaf_only():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.test(100)

def test_remove_root_with_left_and_right_leaf():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.test(100)

def test_remove_node_with_no_leaf():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.test(64)

def test_remove_node_with_left_leaf_only():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.test(65)

def test_remove_node_with_right_leaf_only():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(94)   # added 94 to test if moved up for delNode
    tr.insert(97)
    tr.test(93)

def test_remove_node_with_right_and_left_leaf():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.test(85)

def test_remove_node_with_right_and_left_leaf_no_left_min():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    #tr.insert(93)  # removed 93 to test if min starts in right leg (min should be 95)
    tr.insert(97)
    #tr.test(85)
    tr.rDelete(64)
    tr.inOrder()

def test_successor_inorder():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    SIO = tr.successorInOrder(84)
    if SIO is None:
        print "SIO:None"
    else:
        print "SIO:{}".format(SIO.value)

def test_predecessor_inorder():
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    PIO = tr.predecessorInOrder(84)
    if PIO is None:
        print "PIO:None"
    else:
        print "PIO:{}".format(PIO.value)

def test_inorder_traversal():
    print "in order traversal..."
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.inOrder()

def test_preorder_traversal():
    print "pre order traversal..."
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.preOrder()

def test_postorder_traversal():
    print "post order traversal..."
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    tr.postOrder()

# Test if a Binary Search Tree (BST)
def test_is_bst():
    print "post order traversal..."
    tr = Tree()
    tr.insert(100)  # root
    tr.insert(102)  # rights
    tr.insert(103)
    tr.insert(70)   # lefts
    tr.insert(65)
    tr.insert(85)
    tr.insert(84)
    tr.insert(95)
    tr.insert(64)
    tr.insert(93)
    tr.insert(97)
    print "root.node.value:{}".format(tr.root.value)
    print "isBST:{}".format(tr.isBST(tr.root))

def test_min_and_max():
    tr = Tree()
    tr.insert(100)
    tr.insert(1)
    tr.insert(1000)
    print "Just for fun..."
    print "Min:{}".format(tr.findMin())
    print "Max:{}".format(tr.findMax())

#test_remove_not_found()

#test_remove_root_with_no_leaf()
#test_remove_root_with_left_leaf_only()
#test_remove_root_with_right_leaf_only()
#test_remove_root_with_left_and_right_leaf()

#test_remove_node_with_no_leaf()
#test_remove_node_with_left_leaf_only()
#test_remove_node_with_right_leaf_only()
#test_remove_node_with_right_and_left_leaf()
#test_remove_node_with_right_and_left_leaf_no_left_min()

test_successor_inorder()
test_predecessor_inorder()
#test_inorder_traversal()
#test_preorder_traversal()
#test_postorder_traversal()

#test_is_bst()

#test_min_and_max()
