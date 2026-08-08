# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {v: i for i, v in enumerate(inorder)}
        globalIndex = 0

        def dfs(l, r):
            nonlocal globalIndex

            if l > r:
                return
            
            root = TreeNode(preorder[globalIndex])
            globalIndex += 1
            m = indices[root.val]
            root.left = dfs(l, m - 1)
            root.right = dfs(m + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)

            
