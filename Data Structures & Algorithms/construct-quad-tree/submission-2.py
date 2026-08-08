"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        
        def dfs(n, r, c):
            if n == 1:
                return Node(grid[r][c] == 1, True)
            
            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            botLeft = dfs(n, r + n, c)
            botRight = dfs(n, r + n, c + n)

            if (topLeft.isLeaf and topRight.isLeaf and botLeft.isLeaf and botRight.isLeaf 
                and topLeft.val == topRight.val == botLeft.val == botRight.val):
                return Node(topLeft.val, True)
            
            return Node(-1, False, topLeft, topRight, botLeft, botRight)
        
        return dfs(len(grid), 0, 0)