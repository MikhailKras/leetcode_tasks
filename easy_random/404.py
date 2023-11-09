# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        start, res = (root, 'r'), 0
        stack = [start]
        visited = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            left, right = cur[0].left, cur[0].right
            if left is None and right is None:
                if cur[1] == 'l':
                    res += cur[0].val
            else:
                if left:
                    stack.append((left, 'l'))
                if right:
                    stack.append((right, 'r'))
        return res
        
