# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = k
        
        def dfs(node):
            nonlocal count, res
            if not node:
                return

            dfs(node.left)
            if not count:
                return
            count -= 1
            if count == 0:
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res


            