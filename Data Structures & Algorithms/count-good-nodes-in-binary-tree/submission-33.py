# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dfs(root, maxValSeen):
            if not root:
                return
            nonlocal goodNodes

            if root.val >= maxValSeen:
                goodNodes += 1
            maxValSeen = max(maxValSeen, root.val)

            dfs(root.left, maxValSeen)
            dfs(root.right, maxValSeen)
        
        dfs(root, root.val)
        return goodNodes