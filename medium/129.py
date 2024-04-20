# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack, res = [[root, [str(root.val)]]], 0
        while stack:
            node, digits = stack.pop()
            if node.left is None and node.right is None:
                res += int(''.join(digits))
            else:
                if node.left:
                    stack.append([node.left, digits + [str(node.left.val)]])
                if node.right:
                    stack.append([node.right, digits + [str(node.right.val)]])
        return res

