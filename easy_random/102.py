# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root, None]
        res = []
        cur_level = []
        while queue:
            cur = queue.pop(0)
            if cur is None:
                res.append(cur_level)
                cur_level = []
                if queue:
                    queue.append(None)
            else:
                cur_level.append(cur.val)
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
        return res

