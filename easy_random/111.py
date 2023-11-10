# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        start = (root, 1)
        depth = 10 ** 5 + 1
        stack = [start]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur not in visited:
                visited.add(cur)
                left, right = cur[0].left, cur[0].right
                if left is None and right is None:
                    depth = min(depth, cur[1])
                if left:
                    stack.append((left, cur[1] + 1))
                if right:
                    stack.append((right, cur[1] + 1))
        return depth

