# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        start = (root, f"{root.val}")
        stack = [start]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            if cur[0].left is None and cur[0].right is None:
                res.append(cur[1])
            if cur[0].left:
                stack.append((cur[0].left, f"{cur[1]}->{cur[0].left.val}"))
            if cur[0].right:
                stack.append((cur[0].right, f"{cur[1]}->{cur[0].right.val}"))
        return res

