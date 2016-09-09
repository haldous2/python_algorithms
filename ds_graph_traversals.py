#!/usr/local/bin/python

import time

"""
Fun with data structures - graphs

Searches: BFS:Breadth First & DFS:Depth First Search

Depth First using a stack or set, FIFO
Breadth First using a queue, FILO

"""

# Graph - Adjacency List
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

"""
iterative dfs
"""
def dfs_iterative(v):
    stack = [v]
    visited = []
    while len(stack) > 0:
        print stack
        u = stack.pop()
        if u not in visited:
            visited.append(u)
        for subnode in [x for x in graph[u] if x not in visited]:
            stack.append(subnode)
    print "dfs_iterative visited:{}".format(visited)

dfs_iterative('A')

"""
 recursive dfs
"""
def dfs_visited(graph, node, visited = None):

    if visited is None:
        visited = []

    if node in visited:
        # we've come full circle, time to leave - we're done!
        return

    # add node to visited tracker
    visited.append(node)

    # recurse and follow deep each child from first node
    for subnode in [x for x in graph[node] if x not in visited]:
        #print "dfs_visited(graph, {}, {}) set:{}".format(subnode, visited, graph[node])
        dfs_visited(graph, subnode, visited)

    # return list of visited nodes - should be all in dfs order
    return visited

print "dfs_visited"
# timeS = time.time()
print dfs_visited(graph, 'A', None)
# timeE = time.time()
# timeT = timeE - timeS
# print "time to run: {:.15f} micro seconds".format(timeT)

"""
 recursive dfs paths - not shortest first, bfs is best for that
"""
def dfs_paths(graph, node, target, path = None):

    if path is None:
        path = [node]

    if node == target:
        yield path

    # recurse and follow each to build paths to target
    for v in [x for x in graph[node] if x not in path]:
        #print "recurse dfs_paths vertex:{}, target:{}, path:{} + [{}])".format(v, target, path, v)
        for p in dfs_paths(graph, v, target, path + [v]):
            yield p
            #print "yield p:{}".format(p)
            break

# print "dfs_paths"
# timeS = time.time()
# dfs_path = dfs_paths(graph, 'A', 'F', None)
# dfs_shortest = None
# for x in dfs_path:
#     if dfs_shortest is None:
#         dfs_shortest = x
#     elif len(x) < len(dfs_shortest):
#         dfs_shortest = x
#     print "x is:{}".format(x)
# print "shortest non-weighted path is:{}".format(dfs_shortest)
# timeE = time.time()
# timeT = timeE - timeS
# print "time to run: {:.15f} micro seconds".format(timeT)

"""
iterative breadth first search traversal
O(V+E) time depending on conections to node
"""
def bfs_iterative(v, s = None):
    queue = [v]
    visited = []
    while len(queue) > 0:
        print queue
        u = queue.pop(0)
        if u not in visited:
            visited.append(u)
        if s is not None and s == u:
            print "found {}!".format(s)
            break
        #for subnode in [x for x in sorted(graph[u],reverse=True) if x not in visited]:
        for subnode in [x for x in graph[u] if x not in visited]:
            queue.append(subnode)
    print "bfs_iterative visited:{}".format(visited)

bfs_iterative('A','C')

"""
 iterative breadth first search traversal return paths
 O(V+E) time depending on connections to start
"""
def bfs_paths(graph, start, target):

    visited = []
    queue = [start]

    while len(queue) > 0:

        # current is a path (list)
        current = queue.pop(0) # First In First Out, queued (entire path)
        # last element of current path
        node = current[-1]

        if node not in visited:
            visited.append(node)

        if node == target:
            #print "visited:{}".format(visited)
            return current

        #for c in [x for x in graph[node] if x not in visited]:
        for c in graph[node]:
            new_path = list(current)
            new_path.append(c)
            queue.append(new_path)

    return paths

#print "shortest path via bfs:{}".format(bfs_paths(graph, 'A', 'E'))

def bfs_paths_all(graph, start, target):

    visited = []
    paths = []
    queue = [start]

    while len(queue) > 0:

        # current is a path (list)
        current = queue.pop(0) # First In First Out, queued (entire path)
        # last element of current path
        node = current[-1]

        if node == target:
            paths.append(current)
        else:
            # not tracking end so we can find all paths
            if node not in visited:
                visited.append(node)

        for c in [x for x in graph[node] if x not in visited and x not in current]:
        #for c in graph[node]:
            new_path = list(current)
            new_path.append(c)
            queue.append(new_path)

    return paths

#print "all paths via bfs:{}".format(bfs_paths_all(graph, 'A', 'E'))
