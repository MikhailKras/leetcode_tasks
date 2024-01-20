# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    
    def helper(self, root):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left, right = 0, 0
        if root.left:
            left = self.helper(root.left)
        if root.right:
            right = self.helper(root.right)
        self.diameter = max(self.diameter, left + right)
        if left > right:
            return left + 1
        return right + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.diameter

