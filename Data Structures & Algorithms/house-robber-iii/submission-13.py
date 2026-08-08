# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(root): # returns max money robbed starting from this root downwards
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            
            takeCurrentRoot = root.val
            if root.left:
                takeCurrentRoot += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                takeCurrentRoot += dfs(root.right.left) + dfs(root.right.right)
            
            result = max(takeCurrentRoot, dfs(root.left) + dfs(root.right))
            memo[(root)] = result
            return result
        
        return dfs(root)