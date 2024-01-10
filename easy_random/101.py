# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_symmetric(self, l, r) -> bool:
        if l is None and r is None:
            return True
        if (l is None and r is not None) or (r is None and l is not None):
            return False
        if l.val == r.val:
            return self.check_symmetric(l.left, r.right) and self.check_symmetric(l.right, r.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.check_symmetric(root.left, root.right)
        return True
            
