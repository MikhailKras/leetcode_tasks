# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_diff = float('inf')
        self.arr = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper_inorder(root):
            if root:
                helper_inorder(root.left)
                self.arr.append(root.val)
                if len(self.arr) > 1:
                    self.min_diff = min(self.min_diff, self.arr[-1] - self.arr[-2])
                helper_inorder(root.right)
            return self.min_diff
        return helper_inorder(root)

