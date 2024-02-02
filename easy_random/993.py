# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [[root, 0]]
        px, py, lx, ly = None, None, None, None
        while stack:
            cur, level = stack.pop()
            if cur.left:
                if cur.left.val == x:
                    px, lx = cur, level + 1
                elif cur.left.val == y:
                    py, ly = cur, level + 1
                stack.append([cur.left, level + 1])
            if cur.right:
                if cur.right.val == x:
                    px, lx = cur, level + 1
                elif cur.right.val == y:
                    py, ly = cur, level + 1
                stack.append([cur.right, level + 1])
        return (px != py and lx == ly)
        
