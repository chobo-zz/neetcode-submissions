# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSeen):
            if not node:
                return 0
            
            res = 1 if node.val >= maxSeen else 0
            maxSeen = max(maxSeen, node.val)
            res += dfs(node.left, maxSeen)
            res += dfs(node.right, maxSeen)

            return res
        
        return dfs(root, root.val)
                