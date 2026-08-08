# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(0, left)
            rightMax = max(0, right)
            res = max(res, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res