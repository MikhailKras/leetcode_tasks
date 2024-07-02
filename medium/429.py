"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [root, None]
        res, cur_level = [], []
        while queue:
            cur = queue.pop(0)
            if cur is None:
                res.append(cur_level)
                cur_level = []
                if queue:
                    queue.append(None)
            else:
                cur_level.append(cur.val)
                for child in cur.children:
                    if child:
                        queue.append(child)
        
        return res
        
