# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, res = [root], 0
        while stack:
            cur = stack.pop()
            if low <= cur.val <= high:
                res += cur.val
            left, right = cur.left, cur.right
            if left:
                stack.append(left)
            if right:
                stack.append(right)
        return res

