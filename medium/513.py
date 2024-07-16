# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        is_start_level = False
        queue = deque([root, None])
        res = root.val
        while queue:
            cur = queue.popleft()
            if cur is None:
                is_start_level = True
                if queue:
                    queue.append(None)
            else:
                if is_start_level:
                    res = cur.val
                    is_start_level = False
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
        return res

