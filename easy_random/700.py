# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = []
        start = root
        stack = [start]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            if cur.val == val:
                return cur
            visited.add(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return None

