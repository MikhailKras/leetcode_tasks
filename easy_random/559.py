"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        visited = set()
        max_depth = 1
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            if cur[0].children:
                for child in cur[0].children:
                    stack.append((child, cur[1] + 1))
            else:
                max_depth = max(max_depth, cur[1])
        return max_depth

