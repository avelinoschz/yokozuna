# Depth-First Search

# https://www.algoexpert.io/questions/depth-first-search

# Easy

# You're given a `Node` class that has a `name` and an array of optional `children` nodes. When put together, nodes form an acyclic tree-like structure.

# Implement the `depthFirstSearch` method on the `Node` class, which takes in an empty array, traverses the tree using the Depth-first Search 
# approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

# If you're unfamiliar with Depth-first Search, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

# Sample Input

# graph
#
#        A
#      / | \
#     B  C  D
#    / \    / \
#   E   F  G   H
#      / \  \
#     I   J  K

# Sample Output
# ["A", "B", "E", "F", "I", "J", "C", "D", "G", "К", "H"]

# Solution 1: Iteratively
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):        
        stack = []
        stack.append(self)
        
        while stack:
            current = stack.pop()
            array.append(current.name)

            # backwards because of the push behavior
            for i in range(len(current.children)-1, -1, -1):
                stack.append(current.children[i])   

        return array
        
# Solution 2: Recursion
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def depthFirstSearch(self, array):
        array.append(self.name)
        
        for ch in self.children:
            ch.depthFirstSearch(array)

        return array

# Time complexty: O(v + e) where v is the number of vertices and e is the number of edges in the graph
# Space complexity: O(v) where v is the number of vertices in the graph or O(d) where d is the depth of the graph (in case of recursive implementation)

# For a dense graph, the time complexity is O(v^2) because there are v vertices and each vertex can have up to v-1 edges. For a sparse graph, the time complexity is O(v + e) because there are v vertices and e edges.