# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root.left is None and root.right is None:
            return False
        stack, visited = [root], set()
        while stack:
            cur = stack.pop()
            if k - cur.val in visited:
                return True
            visited.add(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
        
