# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        parents = { root: None }
        visited = set()
        while stack:
            node = stack.pop()

            if not node.left and not node.right and node.val == target:
                parent = parents[node]
                if not parent:
                    return None
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
            elif node not in visited:
                stack.append(node)
                visited.add(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node
        
        return root
                

                    