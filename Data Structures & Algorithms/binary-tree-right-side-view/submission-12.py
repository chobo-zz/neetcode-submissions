# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            lastNode = None
            for _ in range(len(q)):
                lastNode = q.popleft()

                if lastNode.left:
                    q.append(lastNode.left)
                if lastNode.right:
                    q.append(lastNode.right)
            res.append(lastNode.val)
        
        return res