# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        MPS = root.val # stores MPS with a split

        def dfs(root): # MPS starting from root without split
            nonlocal MPS
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            MPS = max(MPS, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return MPS