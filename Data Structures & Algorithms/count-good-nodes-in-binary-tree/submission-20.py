# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxSeen):
            nonlocal res
            if not node:
                return 
            
            maxSeen = max(node.val, maxSeen)
            if node.val >= maxSeen:
                res += 1

            dfs(node.left, maxSeen)
            dfs(node.right, maxSeen)

        dfs(root, root.val)

        return res
