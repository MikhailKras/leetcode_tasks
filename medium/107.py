# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = deque()
        queue = deque([root, None])
        cur_level = []
        while queue:
            cur = queue.popleft()
            if cur is None:
                res.appendleft(cur_level)
                cur_level = []
                if queue:
                    queue.append(None)
            else:
                cur_level.append(cur.val)
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
        return list(res)

