# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        MPS = root.val

        def dfs(root): # compute max path sum from this node without split
            nonlocal MPS

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            MPS = max(MPS, leftMax + rightMax + root.val)
            
            
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return MPS