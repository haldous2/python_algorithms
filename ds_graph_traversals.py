#!/usr/local/bin/python

import time

"""
Fun with data structures - graphs

Building graphs with the stack data type

Breadth First & Depth First

Depth First using a stack or set
stack:  A B D B
output: A -> B -> D -> E -> F -> C
"""

# Graph data
# Note: using a set the order of children will be unreliable
#       that shouldn't matter much for dfs
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

# recursive dfs visited
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

# print "dfs_visited"
# timeS = time.time()
# print dfs_visited(graph, 'A', None)
# timeE = time.time()
# timeT = timeE - timeS
# print "time to run: {:.15f} micro seconds".format(timeT)

# recursive dfs paths - not shortest first, bfs is best for that
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
def bfs(graph, node):

    visited = []
    queue = [node]

    while len(queue) > 0:

        current = queue.pop(0) # First In First Out, queued
        if current not in visited:
            visited.append(current)

        for c in [x for x in graph[current] if x not in visited and x not in queue]:
            queue.append(c)

    return visited

print "traversal via bfs:{}".format(bfs(graph, 'A'))

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

print "shortest path via bfs:{}".format(bfs_paths(graph, 'A', 'E'))

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

print "all paths via bfs:{}".format(bfs_paths_all(graph, 'A', 'E'))
