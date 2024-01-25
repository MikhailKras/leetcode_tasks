# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_value_sequence(self, root: Optional[TreeNode]) -> List:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left is None and cur.right is None:
                res.append(cur.val)
            else:
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return res
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaf_value_sequence(root1) == self.get_leaf_value_sequence(root2)

