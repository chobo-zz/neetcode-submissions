# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(root):
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            
            res = root.val

            if root.left:
                res += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                res += dfs(root.right.left) + dfs(root.right.right)
            
            memo[root] = max(res, dfs(root.left) + dfs(root.right))
            return memo[root]
        
        return dfs(root)