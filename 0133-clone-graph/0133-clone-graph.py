"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        DFS
        T:O(n)
        S:O(n)
        """
        if not node: return node
        if node.val == 0: return Node(node.val)
        nodemap = {}

        def clone(node):
            if node in nodemap:
                return nodemap[node]
            
            copy = Node(node.val)
            nodemap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
            
        return clone(node)