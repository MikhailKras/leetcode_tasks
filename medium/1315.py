# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        root.parent = None
        stack = [root]
        res = 0
        while stack:
            cur = stack.pop()
            for child in (cur.left, cur.right):
                if child:
                    child.parent = cur
                    if cur.parent is not None and cur.parent.val % 2 == 0:
                        res += child.val
                    stack.append(child)
        return res

