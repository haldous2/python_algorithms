"""
 Cracking the coding interview
 Practice questions
 Part 4. Trees & Graphs
"""

"""
 Helper Code

 # Test Graph 1 g1

        A     E
       / \    |
      B - C - F
       \ /
        D
"""

# no path from A to E
g1 = {'A': ['B', 'C'],
      'B': ['C', 'D'],
      'C': ['D'],
      'D': ['C'],
      'E': ['F'],
      'F': ['C']}

# path from A to E
g2 = {'A': ['B', 'C'],
      'B': ['C', 'D'],
      'C': ['D', 'F'],
      'D': ['C'],
      'E': ['F'],
      'F': ['C', 'E']}

def bfsSearchGraph(graph=None, start=None, end=None):

    """
     BFS Traversal / Search
     end is optional - return True or False if end found
     if end is None, return visited
    """
    if not graph or not start:
        return False

    queue = [start]
    visited = [start]

    while queue:

        node = queue.pop(0)

        if node == end:
            return True

        for adjacent in [x for x in graph[node] if x not in visited]:
            visited.append(adjacent)
            queue.append(adjacent)

    if end is None:
        return visited
    else:
        return False

#print bfsSearchGraph(g2, 'A')

def bfsPaths(graph=None, start=None, end=None):

    """
     BFS Traversal / Search - Return Paths
     Returns a list of paths
    """

    if not graph or not start or not end:
        return []

    # maintain a queue of paths
    queue = [[start]]
    paths = []

    while queue:

        # get the first path from the queue
        #print "queue:", queue
        path = queue.pop(0)

        # get the last node from the path
        node = path[-1]

        # path found
        if node == end:
            # return shortest pat
            #return path
            # build list of paths
            paths.append(path)

        # enumerate all adjacent nodes, construct a new path and push it into the queue
        if graph[node]:
            for adjacent in [x for x in graph[node] if x not in path]:
                # build new sub-path for each vertex
                new_path = list(path)
                new_path.append(adjacent)
                #print "path:", path, "new_path:", new_path
                queue.append(new_path)

    return paths

# depth first search - stack and stacks
def dfsSearchGraph(graph=None, start=None, end=None):

    """
     DFS Traversal / Search [Graph - input graph, start and end value: return Bool or visits]
     end is optional - return True or False if end found
     if end is None, return visited
    """
    if not graph or not start:
        return False

    queue = [start]
    visited = [start]

    while queue:

        node = queue.pop()

        if node == end:
            return True

        for adjacent in [x for x in graph[node] if x not in visited]:
            visited.append(adjacent)
            queue.append(adjacent)

    if end is None:
        return visited
    else:
        return False

def dfsSearchTree(root=None, find=None):

    """
     DFS Traversal / Search [Tree - input root of tree and value to find, return node]
     Node: no visit tracker since a loop will not occur in a tree
    """
    if not root or not find:
        return False

    queue = [root]

    while queue:

        node = queue.pop()

        if node.data == find:
            return node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return None

class Node(object):

    def __init__(self, data):
        self.data = data
        self.parent = None  # for use with successor, predacessor
        self.left = None
        self.right = None

"""
 4.1
 Find a path in a graph

 First thoughts: using BFS, build paths until end node is found
  BFS is best for finding shortest paths
      more memory intensive, slower than DFS
"""

#print "path from A to E:", bfsPaths(g2, 'A', 'E')

"""
 4.2
 Build Binary Search Tree from ordered list - maintain level height (balanced)

 [0,1,2,3,4,5,6,7,8,9] - first thoughts, start from middle - that is root, right is right tree, left is left tree
 ** Will need to have insertion methods
 ** Node class
 ** print method to see end result
"""

l1 = [0,1,2,3,4,5,6,7,8]

def bstList(l):

    if not l:
        return

    length = len(l) - 1
    mid = length / 2

    # get this party started
    node = bstListWorkerV2(l, 0, length)

    # Test
    printBST(node)
    #print node.data
    #print node.left.data, node.right.data
    #print node.left.left.data, node.left.right.data, node.right.left.data, node.right.right.data
    #print "None", node.left.right.right.data, "None", node.right.right.right.data

# print BST as DFS pre-order (easier on the eyes)
def printBST(node):
    print node.data
    if node.left:
        printBST(node.left)
    if node.right:
        printBST(node.right)

# looks a lot like quick-sort.
# partition is a calculated midpoint
# also tracking a node to return back
def bstListWorkerV2(l, s=None, e=None):

    if s > e:
        return None

    # s + ((e - s) / 2) same as (s + e) / 2
    #mid = s + ((e - s) / 2)
    mid = (s + e) / 2

    n = Node(l[mid])

    n.left = bstListWorkerV2(l, s, mid - 1)
    n.right = bstListWorkerV2(l, mid + 1, e)

    return n

# Version 2 - a bit more verbose and complicated
def bstListWorkerV1(l, s=None, e=None, n=None, dir=None):

    if s <= e:

        # mid
        mid = s + ((e - s) / 2)

        if not n:
            n = Node(l[mid])
            #print "start node:", l[mid]
        else:
            if s == e:
                # s equals to e, last and only element - add node
                new_node = Node(l[e])
            else:
                # mid point is the new node
                new_node = Node(l[mid])

            if dir == 'left':
                n.left = new_node
                #print "node.left:", new_node.data
            else:
                n.right = new_node
                #print "node.right:", new_node.data
            n = new_node

        #print "s:{} e:{} mid:{} dir:{}".format(s, e, mid, dir)

        #left
        bstListWorkerV1(l, s, mid - 1, n, 'left')

        # right
        bstListWorkerV1(l, mid + 1, e, n, 'right')

        #return n
        return Tree

#bstList(l1)


"""
 4.3
 Using a binary tree, create linked lists for each level of said tree
 A tree of depth 3 will create 3 linked lists
"""

def bfsDepth(n):

    """
     Breadth First Search (BFS)
     Iterative approach
     time complexity O(n), space O(n)
    """
    queue = [[n,1]]     # first node, level 1
    visited = []

    while queue:

        vertex, level = queue.pop(0)
        visited.append(vertex)
        if vertex.left and vertex.left not in visited:
            queue.append([vertex.left, level + 1])
        if vertex.right and vertex.right not in visited:
            queue.append([vertex.right, level + 1])

    print "level:", level, " visited:", [node.data for node in visited] # visits list comprehension

def bfsDepthRecurse(n, v=[], q=[], l=1):
    """
     Yeah right!
     Recursion is a stack and a stack is used for dfs.
     Easier to implement recursion for dfs (over bfs).
     Iterative is easier for me to implement for both dfs and dfs
    """
    pass

def dfsDepth(n):

    stack = [[n,1]]     # first node, level 1
    visited = []

    while stack:

        vertex, level = stack.pop()
        visited.append(vertex)
        if vertex.left and vertex.left not in visited:
            stack.append([vertex.left, level + 1])
        if vertex.right and vertex.right not in visited:
            stack.append([vertex.right, level + 1])

    print "level:", level, " visited:", [node.data for node in visited] # visits list comprehension

def dfsDepthRecurse(n, v=[], l=1):
    """
     DFS in-order traversal
     n = node
     v = visited
     l = level
    """
    if n is None: return
    v.append(n)
    if n.left and n.left not in v:
        bfsDepthRecurse(n.left, v, l + 1)
    if n.right and n.right not in v:
        bfsDepthRecurse(n.right, v, l + 1)

    print "level:", l, " visited:", [node.data for node in v] # visits list comprehension

# Tests - build nodes, test algorithm
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)

#bfsDepth(root)
#bfsDepthRecurse(root)
#dfsDepth(root)
#dfsDepthRecurse(root)

"""
 4.4
 Check if a binary tree is balanced
 balanced means the shortest branch is no more than 1 level shorter than the longest arm
"""

def dfsDepthGauge(n):

    """
     Depth First Search with level counter
    """

    stack = [[n,1]]     # first node, level 1
    visited = []        # track nodes visited (shouldn't be an issue with a tree)

    while stack:

        vertex, level = stack.pop()
        visited.append(vertex)
        if vertex.left and vertex.left not in visited:
            stack.append([vertex.left, level + 1])
        if vertex.right and vertex.right not in visited:
            stack.append([vertex.right, level + 1])

    return level

def binaryTreeIsBalanced(n):

    if n.left:
        level_left = dfsDepthGauge(n.left)
    else:
        level_left = 0

    if n.right:
        level_right = dfsDepthGauge(n.right)
    else:
        level_right = 0

    if level_left > level_right:
        if level_left - level_right > 1:
            return False
    else:
        if level_right - level_left > 1:
            return False

    return True

def binaryTreeIsBalancedRecursiveWorker(n, msg=None, prev=None):

    """
     Recursive depth finder - this is twisting my brain
     Basically counts heights in the tree which could have also been done with split dfs

     for tree
         1
        / \
       2   3
      /
     4

     L n = 1
     L n = 2
     L n = 4
     L @ 4 n = null -> return -1 as L(left)
     R @ 4 n = null -> return -1 as R(right)
     max of (-1, -1) + 1 = 0 - return 0 to next in stack (2) as L
     R @ 2 n = null -> return -1
     max of (0, -1) + 1 = 1 - return ===1=== to next in stack (1) as L

     R @ 1 n = 3
     L @ 3 n = null -> return -1 as L(left)
     R @ 3 n = null -> return -1 as R(right)
     max of (-1, -1) + 1 = 0 - return ===0=== to next in stack (1) as R
     diff at this point is L:1 - R:0 = 1.. checks out! not > 1!!

    """

    print msg

    if n is None:
        print "prev:", prev.data
        return -1
    if n.left:
        sLeft = str(n.left.data)
    else:
        sLeft = "None"
    left = binaryTreeIsBalancedRecursiveWorker(n.left, "left @ " + str(n.data) + " to " + sLeft, n)
    if n.right:
        sRight = str(n.right.data)
    else:
        sRight = "None"
    right = binaryTreeIsBalancedRecursiveWorker(n.right, "right @ " + str(n.data) + " to " + sRight, n)

    diff = abs(left - right)
    print "l:", left, "r:", right, "diff:", diff
    if abs(diff) > 1:
        return False
    else:
        print "======= returning ", max(left, right) + 1
        return max(left, right) + 1

def binaryTreeIsBalancedRecursive(n):
    if binaryTreeIsBalancedRecursiveWorker(n) != False:
        return True
    else:
        return False

# balanced tree
r1 = Node(1)
r1.right = Node(2)
r1.right.right = Node(4)
r1.left = Node(3)

# un-balanced tree
r2 = Node(1)
r2.left = Node(2)
r2.left.left = Node(4)
r2.left.left.right = Node(6)
r2.left.right = Node(5)
r2.right = Node(3)

#print binaryTreeIsBalanced(r1)
#print binaryTreeIsBalancedRecursive(r1)

"""
 4.5
 Validate BST

 Binary Search Tree - everything left of parent is less than, right of parent greater than for each node

 Brute Force - since we know there is a left and right child, compare and bfs queue up, then compare each node...

 Other thoughts - In-Order DFS should return elements in order if a BST

"""

def bstValidRangeUtil(n, min, max):

    """
     Using a range min and max. Easiest to implement, works with duplicates.
     Runtime O(n), Space None

     Ranges diagram:
                   [5]
        (-i, 5)[3]     [6](5, i)
      (-i, 3)[2] [4](3, 5)

    """
    if not n: return True

    # Version 1
    # if (n.data > min
    #     and n.data < max
    #     and bstValidRangeUtil(n.left, min, n.data)
    #     and bstValidRangeUtil(n.right, n.data, max)):
    #     return True
    # else:
    #     return False

    # Version 2
    if n.data < min or n.data > max:
        return False

    if not bstValidRangeUtil(n.left, min, n.data):
        return False
    if not bstValidRangeUtil(n.right, n.data, max):
        return False

    return True

def bstValidRange(n):
    return bstValidRangeUtil(n, -999, 999)

bstPrev = None
def bstValidInOrder(n):

    """
     DFS In-Order traversal should output elements in order
      caveat when there are duplicates, this only works when no duplicates
    """
    global bstPrev

    if n is None:
        return True

    if not bstValidInOrder(n.left):
        # kills recursion by returning false to the top of the stack
        print "l.Falsey"
        return False

    if bstPrev:
        print n.data, bstPrev.data
    else:
        print n.data, "None"

    if bstPrev and n.data < bstPrev.data:
        # send false flag up
        print "Falsey"
        return False

    bstPrev = n

    #return bstValidInOrder(n.right)
    if not bstValidInOrder(n.right):
        # kills recursion by returning false to the top of the stack
        print "r.Falsey"
        return False

    return True

# valid BST
#          5
#       3     7
#     2  4  6  8
r1 = Node(5)
r1.left = Node(3)
r1.left.left = Node(2)
r1.left.right = Node(4)
r1.right = Node(7)
r1.right.left = Node(6)
r1.right.right = Node(8)

# non-valid BST
#          5
#       3     8
#     2  4  7  6
r2 = Node(5)
r2.left = Node(3)
r2.left.left = Node(2)
r2.left.right = Node(4)
r2.right = Node(8)
r2.right.left = Node(7)
r2.right.right = Node(6)

#print "bst validator inorder:", bstValidInOrder(r1)
#print "bst validator inorder:", bstValidInOrder(r2)
#print "bst validator range:", bstValidRange(r1)
#print "bst validator range:", bstValidRange(r2)

"""
 4.6
 Find in-order Successor of a given node. Assume each node has a link to it's parent

 Node:
   data
   next
   parent

 I think this is asking what comes after a node...
 with link to parent should be able to traverse backwards easy enough
 otherwise, treversing bst down and keeping track of prev

             8
        6         9
     4     7
   3   5

 successor of:
  3 = 4
  4 = 5
  5 = 6
  6 = 7
  7 = 8
  8 = 9
  9 = None

 Rules:
  1. If right, go right to find min. right, then as left as possible
     e.g., min of node 4 is 5
  2. If no right, back track via parent to first left connected node
     e.g., successor of 5 is 6, back track from 5 to 4 (right connected), then 6 (left connected)
     if parent is None (root), successor is None (then stop)
"""

def bstFindMin(n):
    """
     From node n, traverse right then left to find min in right
    """

    if n is None:
        return None

    min = None

    if n.right:
        cur = n.right
        while cur:
            min = cur
            cur = cur.left
        return min
    else:
        return None

def bstSuccessor(n):
    """
     From node n, apply rules of successor
    """
    if not n:
        return None
    if n.right:
        # Right leg find min trick
        return bstFindMin(n)
    else:
        # No right leg, traverse parents
        if n.parent:
            cur = n.parent
            prv = n
            while cur:
                # check if parent left is previous node
                if cur.left == prv:
                    return cur
                prv = cur
                cur = cur.parent

def bstPrintNode(n):
    if n:
        print n.data
    else:
        print "None"

# valid BST
#            8
#        6       9
#     4    7
#    3 5
n9 = Node(9)
n8 = Node(8) # das rooten
n7 = Node(7)
n6 = Node(6)
n5 = Node(5)
n4 = Node(4)
n3 = Node(3)

n9.parent = n8
n8.parent = None
n8.left = n6
n8.right = n9
n7.parent = n6
n6.parent = n8
n6.left = n4
n6.right = n7
n4.parent = n6
n4.left = n3
n4.right = n5
n3.parent = n4
n5.parent = n4

# bstPrintNode(bstSuccessor(n9)) # should return None
# bstPrintNode(bstSuccessor(n8)) # should return 9
# bstPrintNode(bstSuccessor(n7)) # should return 8
# bstPrintNode(bstSuccessor(n6)) # should return 7
# bstPrintNode(bstSuccessor(n5)) # should return 6
# bstPrintNode(bstSuccessor(n4)) # should return 5
# bstPrintNode(bstSuccessor(n3)) # should return 4

"""
 Just for fun - predecessor

              8
         6         9
      4     7
    3   5

  predecessor of:
   3 = None
   4 = 3
   5 = 4
   6 = 5
   7 = 6
   8 = 7
   9 = 8

  Rules:
  1. If left, go left to find max. left, then as right as possible
     e.g., max of 6 is 5
  2. predecessor is parent! - easy peasy!

"""

def bstFindMax(n):
    """
     From node n, traverse left then right to find max in left
    """

    if n is None:
        return None

    max = None

    if n.left:
        cur = n.left
        while cur:
            max = cur
            cur = cur.right
        return max
    else:
        return None

def bstPredecessor(n):
    """
     From node n, apply rules of predecessor
    """
    if not n:
        return None
    if n.left:
        # Left leg find max trick
        return bstFindMax(n)
    else:
        # No left leg, traverse parents
        if n.parent:
            cur = n.parent
            prv = n
            while cur:
                # check if parent right is previous node
                if cur.right == prv:
                    return cur
                prv = cur
                cur = cur.parent

# bstPrintNode(bstPredecessor(n9)) # should return 8
# bstPrintNode(bstPredecessor(n8)) # should return 7
# bstPrintNode(bstPredecessor(n7)) # should return 6
# bstPrintNode(bstPredecessor(n6)) # should return 5
# bstPrintNode(bstPredecessor(n5)) # should return 4
# bstPrintNode(bstPredecessor(n4)) # should return 3
# bstPrintNode(bstPredecessor(n3)) # should return None


"""
 4.7
 Topological Sort - DFS - sorting dependencies (graph)

 Note: Topological sort can only be performed on a directed graph with no cycles
       As soon as a cycle is detected, exit and return empty list or error


 A few ways to tackle this
 DFS Modified - for each node go to end and mark. Look for cycles and create topo list
 Kahn's -
 Reverse Kahns ?
"""

def topo_sort_dfs_print(t):
    """
     Input tracker, elements needed to print topology is the end count
    """
    if not t:
        return
    print "========== dfs topological sort =========="
    print t
    output = {}
    topord = []
    for s in t:
        # build new hash table to be sorted
        # 'end time:node'
        output[t[s][2]] = s

    # output should be {8:'a',7:'b',etc...}
    for s in sorted(list(output)):
        topord.append(output[s])

    # topord should be reversed topological order
    topord.reverse()
    print topord

def topo_sort_dfs_visit(g={}, s=None, track={}):
    """
    DFS Recursive Search
    ---- This is your standard recursive dfs algorighm with added (start, end) tracking
    """
    if not s:
        return

    global time

    track[s][0] = 'Visit'
    track[s][1] = time
    time += 1

    for v in g[s]:

        #if track[v][0] == 'Visit':
        #    print "already visited, cycle found @ {}".format(v)

        if track[v][0] is None:     # not visited yet
            topo_sort_dfs_visit(g, v, track)

    track[s][0] = 'Done'
    track[s][2] = time
    time += 1

def topo_sort_dfs(g):
    """
    Depth First Search Topological Sort
    track start and end times. end times become topology
    Note: will work for directed acyclic, and undirected graphs
          will not work for directed with cycles
    Note: track is a hash table 'Node:[status(None, Visit, Done), start count, end count]'
    """
    if not g:
        return []
    track = {n:[None,0,0] for n in g}   # pre-load tracker
    global time
    time = 1
    for s in g:                 # track all elements in graph
        if track[s][0] is None:
            topo_sort_dfs_visit(g, s, track)

    topo_sort_dfs_print(track)

def topo_sort_kahn(g):
    """
    Topological sort for DAG (Direct Acyclic Graphs)
    Note: removing nodes with no incoming edges can only be done with DAG's
    """
    # build tracker for incoming counts
    # format: 'A':0
    track = {s:len(g[s]) for s in g}

    o = [] # topology output of nodes
    # init l queue with zero node(s)
    q = []
    for s in track:
        if track[s] == 0:
            q.append(s)
    DAG = True

    while q:

        u = q.pop(0)
        o.append(u)

        # look for l nodes in graph neighbors
        for n in g: # nodes in graph
            #print "test: if {} in {}".format(s, g[n])
            if u in g[n]:           # test if zero node in node neighbors if 'A' in ['A','B','C']
                #print "decrementing track[{}] -= 1".format(n)
                track[n] -= 1       # decrement tracker
                if track[n] == 0:
                    q.append(n)

    if len(o) == len(g):
        print o
    else:
        print "cycle found or not DAG"

def topo_sort_kahn_reversed(g):
    """
     Topological sort
     Removes nodes with no outgoing vertices, tracks them and repeats process

     e.g., ['a']->['b']->['c']->['d']->[] will yield d,c,b,a. d is first with nothing going out, remove etc...
    """
    g_sorted = []
    count = 0
    while g:
        acyclic = False
        for node, edges in g.items():
            count += 1
            print "============================"
            #print "node:{} edges:{} g:{}".format(node, edges, g)
            for edge in edges:
                print "({}): test --- for node:{}... if {} in {}".format(count, node, edge, g)
                if edge in g:
                    print "{} found ... breaking".format(edge)
                    break
            else: # no edges found, remove node
                print "({}): deleting node:{} from g".format(count, node)
                acyclic = True
                del g[node]
                g_sorted.append((node, edges))

        if not acyclic:
            print "error - cycle found"
            break

    print g_sorted

# unordered graph
# visit order: A,B,F,G,C,J,I,H,D,E
# topo  order: A,B,F,I,H,D,E,G,J,C
g1 = {
'A':['B','E'],
'B':['A','F'],
'C':['G'],
'D':['E','H'],
'E':['A','D','H'],
'F':['B','G','I','J'],
'G':['C','F','J'],
'H':['D','E','I'],
'I':['F','H'],
'J':['F','G']
}

# directed acyclic graph DAG
g2 = {
'A':['E'],
'B':['A','E'],
'C':['A'],
'D':['G'],
'E':[],
'F':['A','B','C'],
'G':[]
}

# directed acyclic graph DAG
g3 = {
'A':['B','C'],
'B':['D'],
'C':['D'],
'D':[]
}

#topo_sort_dfs(g1)
#topo_sort_kahn(g2)
#topo_sort_kahn_reversed(g3)


"""
4.8
"""

# Binary Tree
#            1
#       2         3
#    4     5   6     7
#  8  9  10 11

r2 = Node(1)
r2.left = Node(2)
r2.left.left = Node(4)
r2.left.left.left = Node(8)
r2.left.left.right = Node(9)
r2.left.right = Node(5)
r2.left.right.left = Node(10)
r2.left.right.right = Node(11)
r2.right = Node(3)
r2.right.left = Node(6)
r2.right.right = Node(7)

def bfsTreePaths(root=None, end=None):

    """
     BFS Traversal / Search - Return Paths
     Returns a list of paths
    """

    if not root or not end:
        return []

    # maintain a queue of paths
    queue = [[root]]
    paths = []

    while queue:

        # get the first path from the queue
        path = queue.pop(0)

        # get the last node from the path
        node = path[-1]

        # path found
        if node.data == end:
            # build list of paths
            #paths.append(path)
            # should be able to break since a tree should only have one path to goal
            paths = list(path)
            break

        # build new_path from path + adjacent and add to queue
        if node.left:
            # build new sub-path for each vertex
            new_path = list(path)
            new_path.append(node.left)
            queue.append(new_path)

        if node.right:
            # build new sub-path for each vertex
            new_path = list(path)
            new_path.append(node.right)
            queue.append(new_path)

    # Test print paths
    # print "bfs paths:"
    # for p in paths:
    #   print p.data

    return paths

def dfsTreePaths(root=None, end=None):

    """
     DFS Traversal / Search - Return Paths
     Returns a list of paths
    """

    if not root or not end:
        return []

    # maintain a stack of paths
    stack = [[root]]
    paths = []

    while stack:

        # get the first path from the stack
        path = stack.pop()

        # get the last node from the path
        node = path[-1]

        # path found
        if node.data == end:
            # build list of paths
            #paths.append(path)
            # should be able to break since a tree should only have one path to goal
            paths = list(path)
            break

        # build new_path from path + adjacent and add to stack
        if node.left:
            # build new sub-path for each vertex
            new_path = list(path)
            new_path.append(node.left)
            stack.append(new_path)

        if node.right:
            # build new sub-path for each vertex
            new_path = list(path)
            new_path.append(node.right)
            stack.append(new_path)

    # Test print paths
    #print "dfs paths:"
    #for p in paths:
    #    print p.data

    return paths

def lowestCommonAncestorPaths(r, n1, n2):

    """
     Find lowest common ancestor of two node values in a binary tree
     using a dfs path find paths to nodes n1, n2 and then compare those paths
     lca will be where paths from start stop matching

     Note: r is tree root, n1 & n2 are values of nodes to find lca

     e.g. lca @ 2
     [1]->[2]->[3]->[4]
     [1]->[2]->[5]->[6]
    """

    path1 = dfsTreePaths(r, n1)
    path2 = dfsTreePaths(r, n2)

    # match paths
    if len(path1) > len(path2):
        patht = path1
        path1 = path2
        path2 = patht

    lca = None
    for i in xrange(len(path1)):
        if path1[i].data == path2[i].data:
            lca = path1[i]
        else:
            break

    if lca:
        print "lowest common ancestor:", lca.data
    else:
        print "did not find lowest common ancestor"


#bfsTreePaths(r2, 7)
#dfsTreePaths(r2, 7)
# lowestCommonAncestorPaths(r2, 2, 4)
# lowestCommonAncestorPaths(r2, 3, 4)
# lowestCommonAncestorPaths(r2, 2, 3)

# LCA take 2 - using DFS traversals in-order and post-order then comparing

def lowestCommonAncestorTraversal(r, n1, n2):

    print "lca of {} and {}".format(n1, n2)

    arrInOrder = []
    def inOrder(r):
        if r is None: return
        inOrder(r.left)
        arrInOrder.append(r)
        inOrder(r.right)

    arrRange = []
    def inRange(inRange=False):
        for n in arrInOrder:
            if n.data == n1:
                inRange = True
            if inRange is True:
                arrRange.append(n)
            if inRange is True:
                if n.data == n2:
                    inRange = False

    arrPostOrder = []
    def postOrder(r):
        if r is None: return
        postOrder(r.left)
        postOrder(r.right)
        arrPostOrder.append(r)

    inOrder(r)
    inRange()
    postOrder(r)

    #print [x.data for x in arrInOrder]
    #print [x.data for x in arrRange]
    #print [x.data for x in arrPostOrder]

    # process traversals...
    # everything between n1 & n2 in inorder gets compared to postorder

    # lca of 1 and 12.
    # compare everything between 1 and 12 to post order
    # highest index is the lca
    # [1, 2, 9, 3, 10, 4, 12, 5, 7, 8, 6] in-order
    # [1, 9, 2, 10, 12, 4, 3, 7, 6, 8, 5] post-order

    maxPost = -1
    for n in arrRange:
        for i in xrange(maxPost, len(arrPostOrder)):
            if arrPostOrder[i].data == n.data:
                if i > maxPost:
                    maxPost = i
    if maxPost >= 0:
        #print "maxPost:", maxPost
        print "lca:", arrPostOrder[maxPost].data
    else:
        print "lca: not found"

#lowestCommonAncestorTraversal(r2, 1, 12)

def lowestCommonAncestorBottomUp(r, n1, n2):

    """
     Recursion - stack - dfs like. runtime O(n)

                 1
           2           3
        4     5     6     7
      8   9 10 11

    looking for 9 & 11
    start: pass in binary tree (not bst)
    r = 2

    L = 2
    L |L = 4
      |L = 8
      |R = 9 -> return 9 up stack
    R |R = 5
      |L = 10 -> return 10 up stack

    """

    if not r: return None
    if r.data == n1 or r.data == n2: return r

    L = lowestCommonAncestorBottomUp(r.left, n1, n2)
    R = lowestCommonAncestorBottomUp(r.right, n1, n2)

    # found left and right values - this is the ancestor
    if L and R:
        return r

    # did not find both left and right, keep looking up stack
    if L:
        return L
    elif R:
        return R
    else:
        return None

#print "lca:", lowestCommonAncestorBottomUp(r2, 4, 10).data

"""
4.9
"""

def bstPermutations(r):

    """
     Not taking any credit for this solution - this is a conversion from java to python
     of CTCI chapter 4, exercise 9

     Helpful for understanding.
      reads tree from bottom up, builds sub-sequences
      prefix becomes the root for each sequence e.g., 2 when (1 <-- 2 --> 3)
      sequences build off of one another until top of stack is reached

     BST
             4
        2         5
     1     3

     left: []  right: []  prefix: [1]
     left: []  right: []  prefix: [3]
     left: [1]  right: [3]  prefix: [2]
     left: []  right: []  prefix: [5]
     left: [2, 1, 3]  right: [5]  prefix: [4]
     left: [2, 3, 1]  right: [5]  prefix: [4]

     ----- [4, 2, 1, 3, 5]
     ----- [4, 2, 1, 5, 3]
     ----- [4, 2, 5, 1, 3]
     ----- [4, 5, 2, 1, 3]
     ----- [4, 2, 3, 1, 5]
     ----- [4, 2, 3, 5, 1]
     ----- [4, 2, 5, 3, 1]
     ----- [4, 5, 2, 3, 1]

    """

    if not root:
        return

    def weaveLists(first=[], second=[], results=[], prefix=[]):

        # One list is empty.
        # Add the remainder to [a cloned] prefix and store result.
        if len(first) == 0 or len(second) == 0:
            result = list(prefix)
            result.extend(first)
            result.extend(second)
            results.append(result)
            return

        # Recurse with head of first added to the prefix. Removing the
        # head will damage first, so we'll need to put it back where we
        # found it afterwards.
        headFirst = first.pop(0)
        prefix.append(headFirst)
        weaveLists(first, second, results, prefix)
        prefix.pop()
        first.insert(0, headFirst)

		# Do the same thing with second, damaging and then restoring
		# the list.
        headSecond = second.pop(0)
        prefix.append(headSecond)
        weaveLists(first, second, results, prefix)
        prefix.pop()
        second.insert(0, headSecond)

    def allSequences(node=None):

        result = []

        if node is None:
            result.append([])
            return result

        prefix = []
        prefix.append(node.data)

        leftSeq = allSequences(node.left)
        rightSeq = allSequences(node.right)

        for left in leftSeq:
            for right in rightSeq:
                print "left:", left, " right:", right, " prefix:", prefix
                weaved = []
                weaveLists(left, right, weaved, prefix)
                result.extend(weaved)

        return result

    allSeq = allSequences(r)
    print "=============="
    count = 0
    for s in allSeq:
        count += 1
        print "-----", s
    print "sequences:", count

# Binary Search Tree
#            4
#       2         5
#    1     3

r2 = Node(4)
r2.left = Node(2)
r2.left.left = Node(1)
r2.left.right = Node(3)
r2.right = Node(5)

#bstPermutations(r2)

"""
4.10

Test if the smaller tree t2 is a subtree of t1

Using pre-order traversal in both recursive and string comparison cases.
"""

# n1 = dfsSearchTree(r2, 4)
# if n1:
#     print n1.data
# else:
#     print n1

def preOrderMatchSubstringUtil(r, l=['']):
    """
    input: r - head node of tree
           l - single value list to return
    note: this is nothing more than a pre-order traversal
          makes it so has to be in pre-order order. e.g.

              1                      1
            2   3  doesn't match   2   3  because node 4 is in pre-order
             5                    4 5     this doesn't make sense to me tho... hurm
    """
    if not r:
        l[0] += "X"
        return
    else:
        l[0] += str(r.data)

    preOrderMatchSubstringUtil(r.left, l)
    preOrderMatchSubstringUtil(r.right, l)

def preOrderMatchSubstring(r1, r2):
    """
    Note: I prefer this method. DFS search for first node in large tree O(logn), then compare string k(smaller tree) times
          Will require extra space though
    test if r2 is a subtree of r1
    where r1 is larger than r2
    note: no check to see if r1 bigger than r2
    """
    if not r1 or not r2:
        return None

    ls1 = ['']
    ls2 = ['']

    # sublist method
    # find r2 in r1
    n1 = dfsSearchTree(r1, r2.data)
    if n1:
        # building pre-order traversal strings
        preOrderMatchSubstringUtil(n1, ls1)
        preOrderMatchSubstringUtil(r2, ls2)
    else:
        print "didn't find comparison node"

    if len(ls1[0]) > 0 and len(ls2[0]) > 0:
        # look for substring match
        print "substring... is subtree:", ls2[0] in ls1[0]
    else:
        print "not enough data to compare"

# A utility function to check whether trees with roots
# as root 1 and root2 are indetical or not
def preOrderMatchCompareUtil(r1, r2):
    """
    input: r1 - found node in large tree
           r2 - comparison tree
    check whether trees with roots as r1 and r2 are indetical or not
    note: this is nothing more than a pre-order traversal
          makes it so has to be in pre-order order. e.g.

              1                      1
            2   3  doesn't match   2   3  because node 4 is in pre-order
             5                    4 5     this doesn't make sense to me tho... hurm
    """
    if r1 is None and r2 is None:       # match at edges
        return True
    elif r1 is None or r2 is None:      # one of the trees isn't the same size
        return False
    elif r1.data != r2.data:            # non matching nodes
        return False
    else:
        return preOrderMatchCompareUtil(r1.left , r2.left) and preOrderMatchCompareUtil(r1.right, r2.right)

def preOrderMatchCompare(r1, r2):

    if not r1 or not r2:
        return None

    n1 = dfsSearchTree(r1, r2.data)
    if n1:
        print "comparing... is subtree:", preOrderMatchCompareUtil(n1, r2)
    else:
        print "didn't find comparison node"

# Binary Tree R1
#            1
#       2         3
#    4     5         8
#  6  7
# 2,4,6,x,x,7,x,x,5,x,x - node + x,x can be

t1 = Node(1)
t1.left = Node(2)
t1.left.left = Node(4)
t1.left.right = Node(5)
t1.left.left.left = Node(6)
t1.left.left.right = Node(7)
t1.right = Node(3)
t1.right.right = Node(8)

# Binary Tree R1
#       2
#    4     5
#     7
# 2,4,x,7,x,x,5,x,x

t2 = Node(2) # 2
t2.left = Node(4) # 4
t2.left.left = Node(6) # adding left makes a match. don't understand why it needs a left other than traversal rules
t2.left.right = Node(7) # 7
t2.right = Node(5) # 5

#preOrderMatchSubstring(t1, t2)
#preOrderMatchCompare(t1, t2)

"""
4.11

Implement a binary search tree with methods: insert, find, delete and randomNode.
All nodes in BST should be equally likely of being returned by random.

Initial thoughts: for random, keeping track of length of BST, will use length and
internal python random number generator to pick node. the rest of the methods are
academic.

Insert: BST's are setup so that everything on left is less than root, and everything
        on right is greater than root. Everything inserted bubbles down
Search: using same logic as >< root - follow path until node found
Delete: find root, unlink - set prev.next to...
        three options:
          if leaf: set prev next to None
          if left or right only: set left or right to prev next
          if left and right: find smallest node in right subtree and set prev next to that node

Class BST():
  def __init__(self):
     self.head = None # head node, top of the pile, entry into the BST
     self.count = 0   # node counter kept up to date by insert, delete
"""

import random

class BST(object):

    def __init__(self):
        """
        bst container for head and counter
        """
        self.head = None
        self.count = 0

    def printRandomInt(self):
        print random.random()

    def updateCountUtil(self, n):
        """
        update bst.self.count(er)
        dfs for fast counting
        """
        if not n:
            return

        count = 0
        stack = [n]

        while stack:
            count += 1
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return count

    def updateCount(self):
        count = self.updateCountUtil(self.head)
        self.count = count
        print "node count:", count

    def findRandom(self):
        if self.count == 0:                         # cannot return random of nothing!
            return None
        # random.randint doesn't seem to be very random
        #print "picking a random int from {} to {}".format(1, self.count)
        random.seed(random.randint(1, 999999))
        randint = random.randint(1, self.count)     # random int from 1 to number of nodes in tree
        randnod = self.findNthNode(randint)
        if randnod:
            print "random node found:", randnod.data
        else:
            print "random node not found"

    def findNthNode(self, i):
        """
        Find and return nth node determined by integer i
        using DFS to walk through nodes all the while tracking a count
        """
        if not i:
            return

        count = 0
        n = self.head

        stack = [n]

        while stack:
            count += 1
            cur = stack.pop()
            if i == count:
                return cur
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

    def findMin(self, n):
        """
        find minimum for deletion
        looking for smallest from right. go right, then all lefts
        """
        if not n or type(n) is not Node:
            return None
        if not n.right:
            return None
        n = n.right
        while n:
            min = n
            n = n.left
        return min

    def findPrev(self, next):
        """
        find previous node to n and return it
        this wouldn't be necessary if node class had parent link built in
        input:
        """
        if not self.head or not next or type(next) is not Node:
            return None
        v = next.data
        prev = None
        n = self.head
        while n:
            if v < n.data:
                prev = n
                n = n.left
            elif v > n.data:
                prev = n
                n = n.right
            else:
                # found matching value
                return prev

        # nothing found
        return None

    def findNode(self, v):
        """
        find node in bst by value
        """
        if not self.head or not v:
            return None
        n = self.head
        while n:
            if v < n.data:
                n = n.left
            elif v > n.data:
                n = n.right
            else:
                # found matching value
                return n

        # nothing found
        return None

    def deleteNode(self, v):
        """
        delete node in bst by node
        options when deleting:
        1. leaf node, just remove previous link
        2. one child - move child up to previous link
        3. two children - find minimum and move min up to previous link
        """

        n = self.findNode(v)
        if not n:
            raise ValueError("Node @ {} not found.".format(v))
        if type(n) is not Node:
            raise ValueError("Node @ {} is not a valid Node".format(v))

        self.count -= 1

        if n.left and n.right:

            # two children - find minimum and set previous

            # min:
            # could have a right child. move this to parent of min
            m = self.findMin(n)         # will always find min in node that has a right
            pm = self.findPrev(m)       # find previous of min. will always find this since min in front of start node
            if m.right:                 # min might have a trailing right
                if pm.left == m:
                    pm.left = m.right   # prev.left to mid. connect right straggler
                else:
                    pm.right = m.right  # prev.right to mid. connect right straggler
            else:
                if pm.left == m:
                    pm.left = None      # prev.left to mid. reset
                else:
                    pm.right = None     # prev.right to mid. reset

            # node:
            n.data = m.data             # setting node value. no need to move node, only difference is value

        elif n.left or n.right:

            # one child - find next brach
            if n.left:
                next = n.left
            else:
                next = n.right

            # node
            p = self.findPrev(n)
            if p:                       # might not find previous. could be @ root
                if p.left == n:
                    p.left = next       # prev.left to node. connect next
                else:
                    p.right = next      # prev.right to node. connect next
            else:
                self.head = next        # no prev. set head to next

        else:

            # leaf node! - disconnect prev
            p = self.findPrev(n)
            if p:                       # might not find previous. could be @ root
                if p.left == n:
                    p.left = None       # prev.left to node. set to None
                else:
                    p.right = None      # prev.right to node. set to None
            else:
                self.head = None        # no prev. set head to None

    def insertNode(self, v):
        """
        Insert a node
        follow a path down. start @ head, compare values - less go left, greater go right
        when the end of a path is found - put that thing in there
        """
        if not v:
            return

        self.count += 1

        n = self.head

        if not n:               # no root yet. plant a tree
            self.head = Node(v)
            return              # we are done. get out of here

        while n:                # compare-arator - follow the path

            if v < n.data:
                # look left
                if n.left is None:
                    n.left = Node(v)
                    return
                else:
                    n = n.left
            else:               # assume >= put it on the right - allow duplicates
                # look right
                if n.right is None:
                    n.right = Node(v)
                    return
                else:
                    n = n.right

    def minVal(self):
        pass

    def maxVal(self):
        pass

    def preOrderUtil(self, n):
        if n:
            print n.data
            self.preOrderUtil(n.left)
            self.preOrderUtil(n.right)

    def preOrder(self, n=None):
        print "===== pre-order results ====="
        self.preOrderUtil(n)

# BSTies
#          5
#      3       7
#    2   4   6   8
#  1               9

# brute force build tree
bst = BST()
bst.head = Node(5)
bst.head.left = Node(3)
bst.head.right = Node(7)
bst.head.left.left = Node(2)
bst.head.left.left.left = Node(1)
bst.head.left.right = Node(4)
bst.head.right.left = Node(6)
bst.head.right.right = Node(8)
bst.head.right.right.right = Node(9)

# bst_node = bst.findNode(8)
# if bst_node:
#
#     print "found node:", bst_node.data
#
#     bst_min = bst.findMin(bst_node)
#     if bst_min:
#         print "min:", bst_min.data
#     else:
#         print "min not found - must go right, then left to find min"
#
#     bst_prev = bst.findPrev(bst_node)
#     if bst_prev:
#         print "prev:", bst_prev.data
#     else:
#         print "prev not found... waa waa"
#
# else:
#     print "node not found"
#
# bst.updateCount()
#
# bst.preOrder(bst.head)
# bst.deleteNode(5)
# bst.deleteNode(3)
# bst.deleteNode(7)
# bst.deleteNode(2)
# bst.deleteNode(4)
# bst.deleteNode(6)
# bst.deleteNode(8)
# bst.deleteNode(1)
# #bst.deleteNode(1) # error - node not found
# print "bst count:", bst.count
# bst.deleteNode(9)
# print "bst count:", bst.count
#
# bst.preOrder(bst.head)
#
# bst.insertNode(5)
# bst.insertNode(3)
# bst.insertNode(7)
# bst.insertNode(2)
# bst.insertNode(4)
# bst.insertNode(6)
# bst.insertNode(8)
# bst.insertNode(1)
# bst.insertNode(9)
# print "bst count:", bst.count
#
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
# bst.findRandom()
#
# bst.preOrder(bst.head)

"""
4.12

Sum paths in Binary Tree

Initial thoughts:
dfs paths to target, where target is a sum. when sum is larger or smaller keep on truckin'
"""

def sumTreePaths(r, v):
    """
    List all paths with sum in binary tree.
    Runtime around O(nlogn) n for nodes in tree,
    """

    if not r or not v:
        return []

    stack = [[r]]                       # stacks as nodes - convert only on comparison
    path = None
    paths = []                          # return paths when sum found
    logic_count = 0

    while stack:

        path = stack.pop()              # last path in stack e.g. [[1],[1,2],[1,2,3]] -> [1,2,3]
        node = path[-1]                 # last node in path e.g. [1,2,3] -> 3

        # testing out some sum checks
        # first is default for finding end(sum in this case) from root
        #if sum([x.data for x in path]) == v:
        #    paths.append(path)

        tval = None
        tsum = 0
        tpath = []

        for i in range(len(path)):      # growth of 1 to n ..
            logic_count += 1
            tval = path[-(i+1)].data    # value of path element in reverse e.g. [1,2,3] @ -1 = 3
            tsum += tval                # temp sum tracker
            tpath = [tval] + tpath      # temp path tracker (new path checking reverse, appending reverse)
            if tsum == v:
                 paths.append(tpath)
                 break

        if node.left:
            lpath = list(path)          # new path object so original path isn't effected
            lpath.append(node.left)
            stack.append(lpath)

        if node.right:
            lpath = list(path)          # new path object so original path isn't effected
            lpath.append(node.right)
            stack.append(lpath)

    print "logical count:", logic_count
    return paths

def countPathsWithSumIterative(root, targetSum):
    """
    Iterative approach to track sums through a tree
    When sum minus target is found in hash increment total paths and decrement hash value

    Note:    running sums in parens (x)
             with target of e.g. 6, temp sum in brackets []. temp sum = running sum - target
             default hash {0:1} for root element

    Results: node 1 has a sum of 5, matching hash 5 += total paths
             node 6 has a sum of -2, matching hash -2 += total paths
             node 8 has a sum of 0, matching hash (default) 0 += total paths

                       5 (5)[-1]
               /                   \
              3 (8)[2]             -7 (-2)[-8]
           /        \              /          \
          2 (10)[4]  4 (12)[6]     6 (4)[-2]*  8 (6)[0]*
        /                                       \
       1 (11)[5]*                                9 (15)[9]

    """
    if not root:
        return 0

    stack = [[root, 0]]
    totalPaths = 0
    sumHash = {0:1}                         # default hash

    while stack:                            # dfs traversal

        node, runningSum = stack.pop()

        runningSum += node.data
        if runningSum in sumHash:
            sumHash[runningSum] += 1
        else:
            sumHash[runningSum] = 1

        if node.left:
            stack.append([node.left, runningSum])

        if node.right:
            stack.append([node.right, runningSum])

        tsum = runningSum - targetSum
        if tsum in sumHash:
            totalPaths += sumHash[tsum]
            sumHash[runningSum] -= 1        # cleanup hash that has already been counted

    print sumHash, totalPaths

"""
Book answer - same as above except this is recursive.
the iterative approach seems easier to read to me
"""
def incrementHashTable(hash, key, delta):
    if key in hash:
        hash[key] += delta
    else:
        hash[key] = delta
    #print "hash:", hash, " key:", key, " delta:", delta

def countPathsWithSum(node, targetSum, runningSum, paths):
    """
    """
    if not node:
        return 0

    #print "runningSum:{} += node.data:{} = {}".format(runningSum, node.data, (runningSum + node.data))
    runningSum += node.data
    incrementHashTable(paths, runningSum, 1)

    sum = (runningSum - targetSum)
    #print "=====> sum:{} = runningSum:{} - targetSum:{}".format(sum, runningSum, targetSum)
    print "=====> node:", node.data, " runningSum:", runningSum, " sum:", sum
    if sum in paths:
        print "!!!!! sum {} found in hash {}".format(sum, paths)
        totalPaths = paths[sum]
    else:
        totalPaths = 0

    totalPaths += countPathsWithSum(node.left, targetSum, runningSum, paths)
    totalPaths += countPathsWithSum(node.right, targetSum, runningSum, paths)

    incrementHashTable(paths, runningSum, -1)
    return totalPaths

def countPathWithSum(root, targetSum):
    """
    Find the number of paths that sum to targetSum
    """
    if not root:
        return 0
    paths = {}
    incrementHashTable(paths, 0, 1)                                 # needed if target starts @ root... init hash
    number_paths = countPathsWithSum(root, targetSum, 0, paths)
    return number_paths

# BSTies - supposed to be a binary tree, we use a bst!
#          5
#      3       7
#    2   4   6   8
#  1               9

# brute force build tree
tsum = Node(5)
tsum.left = Node(3)
tsum.left.left = Node(2)
tsum.left.right = Node(4)
tsum.left.left.left = Node(1)
tsum.right = Node(-7)
tsum.right.left = Node(6)
tsum.right.right = Node(8)
tsum.right.right.right = Node(9)

print sumTreePaths(tsum, 6)
print countPathWithSum(tsum, 6)
countPathsWithSumIterative(tsum, 6)
