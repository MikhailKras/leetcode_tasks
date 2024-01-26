# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        val = root.val
        while stack:
            cur = stack.pop()
            if cur.val != val:
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return True
        
