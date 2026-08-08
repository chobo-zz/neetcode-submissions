# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal to process nodes in ascending order
        res = -1
        def dfs(node):
            nonlocal k, res
            if not node:
                return
            
            dfs(node.left)
            if not k:
                return
            k -= 1
            if not k:
                res = node.val
                return
            
            dfs(node.right)
        
        dfs(root)
        return res