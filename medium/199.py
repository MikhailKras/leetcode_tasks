# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root, None])
        prev = None
        while queue:
            cur = queue.popleft()
            if cur is None:
                res.append(prev.val)
                if queue:
                    queue.append(None)
            else:
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
                prev = cur
        return res

