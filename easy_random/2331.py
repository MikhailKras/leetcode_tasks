# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> int:
        if root.left and root.right:
            l = self.postorderTraversal(root.left)
            r = self.postorderTraversal(root.right)
            root.val = l or r if root.val == 2 else l and r
            return root.val
        else:
            return root.val

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        self.postorderTraversal(root)
        return bool(root.val)
        
