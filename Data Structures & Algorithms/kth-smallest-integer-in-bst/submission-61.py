# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = -1
        def dfs(root):
            nonlocal kth, k

            if not root:
                return 

            dfs(root.left)
            k -= 1
            if not k:
                kth = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return kth
            
