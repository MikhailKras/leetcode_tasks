"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        prev = None
        queue = deque([root, None])
        while queue:
            cur = queue.popleft()
            if cur is None:
                if prev:
                    prev.next = None
                if queue:
                    queue.append(None)
            else:
                if prev:
                    prev.next = cur
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
            prev = cur
        return root

