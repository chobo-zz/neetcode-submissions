# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, maxSeen):
            nonlocal res
            if not root:
                return
            
            res += 1 if root.val >= maxSeen else 0
            maxSeen = max(maxSeen, root.val)

            dfs(root.left, maxSeen)
            dfs(root.right, maxSeen)

        dfs(root, root.val)
        return res