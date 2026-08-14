# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return []
        
        res = []
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                root = q.popleft()

                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                
                level.append(root.val)
            res.append(level)
        
        return res