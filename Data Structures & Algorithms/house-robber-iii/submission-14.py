# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        res = 0
        memo = {}
        def dfs(root): # returns max money robbable starting from this node downwards
            if not root:
                return 0

            if root in memo:
                return memo[root]

            robbed = root.val
            if root.left:
                robbed += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                robbed += dfs(root.right.left) + dfs(root.right.right)
            
            memo[root] = max(robbed, dfs(root.left) + dfs(root.right))
            return memo[root]
        
        return dfs(root)
                