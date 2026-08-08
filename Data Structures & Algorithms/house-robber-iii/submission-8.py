# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {} # stores max robbed starting from a node downwards
        def dfs(root): # returns max robbable amount starting from this node downwards
            if not root:
                return 0
            
            if root in memo:
                return memo[root]
            res = root.val
            if root.left:
                res += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                res += dfs(root.right.right) + dfs(root.right.left)

            memo[root] = max(res, dfs(root.left) + dfs(root.right))
            return memo[root]

        return dfs(root)
