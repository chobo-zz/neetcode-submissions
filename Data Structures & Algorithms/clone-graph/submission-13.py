"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToCopy = {}

        def dfs(node):
            if node in oldToCopy:
                return oldToCopy[node]
            
            oldToCopy[node] = Node(node.val)

            for neighbor in node.neighbors:
                oldToCopy[node].neighbors.append(dfs(neighbor))
            
            return oldToCopy[node]
        
        return dfs(node)