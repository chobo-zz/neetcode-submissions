# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftVal, rightVal): # returns if BST starting at this node
            if not node:
                return True
            
            if not leftVal < node.val < rightVal:
                return False
            
            return dfs(node.left, leftVal, node.val) and dfs(node.right, node.val, rightVal)
        
        return dfs(root, float("-inf"), float("inf"))
            
        
