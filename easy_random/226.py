# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left and cur.right:
                cur.left, cur.right = cur.right, cur.left
                stack.extend([cur.left, cur.right])
            elif cur.left:
                cur.right = cur.left
                cur.left = None
                stack.append(cur.right)
            elif cur.right:
                cur.left = cur.right
                cur.right = None
                stack.append(cur.left)
        return root

