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

        def dfs(node): # returns MPS from this node without split
            nonlocal MPS

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            MPS = max(MPS, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return MPS