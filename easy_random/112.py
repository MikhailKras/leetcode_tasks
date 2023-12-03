# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, root.val)]
        while stack:
            node, path_sum = stack.pop()
            if node.left is None and node.right is None:
                if targetSum == path_sum:
                    return True
            for child in (node.left, node.right):
                if child:
                    stack.append((child, path_sum + child.val))
        return False
        
