# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        # return max path without split
        def dfs(node):
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # edge case to make sure we don't include negative values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # calculate max from current root WITH split
            nonlocal res
            res = max(res, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res
            