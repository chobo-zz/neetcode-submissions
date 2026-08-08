# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, maxSeen):
            if not root:
                return 0
            
            res = 1 if root.val >= maxSeen else 0
            maxSeen = max(maxSeen, root.val)

            res += dfs(root.left, maxSeen)
            res += dfs(root.right, maxSeen)

            return res
        
        return dfs(root, root.val)