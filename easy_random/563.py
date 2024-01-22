# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt = 0

    def get_tilt_of_tree(self, root: Optional[TreeNode]):
        if root:
            left, right = 0, 0
            if root.left:
                left = self.get_tilt_of_tree(root.left)
            if root.right:
                right = self.get_tilt_of_tree(root.right)
            self.tilt += abs(left - right)
            return left + right + root.val
        return 0
        
        return root.val + self.get_sum_of_tree(root.left) + self.get_sum_of_tree(root.right)

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.get_tilt_of_tree(root)
        return self.tilt

