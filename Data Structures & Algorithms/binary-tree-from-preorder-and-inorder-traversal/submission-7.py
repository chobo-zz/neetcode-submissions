# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = { value: index for index, value in enumerate(inorder) }
        globalIndex = 0

        def dfs(l, r):
            nonlocal globalIndex
            if l > r:
                return None

            node = TreeNode(preorder[globalIndex])
            globalIndex += 1
            mid = indices[node.val]

            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)

            return node
        
        return dfs(0, len(inorder) - 1)