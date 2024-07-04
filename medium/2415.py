# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        is_odd = False
        cur_level = deque()
        level_values = deque()
        queue = deque([root, None])
        while queue:
            cur = queue.popleft()
            if cur is None:
                if is_odd:
                    for node, val in zip(cur_level, level_values):
                        node.val = val
                cur_level = deque()
                level_values = deque()
                is_odd = not is_odd
                if queue:
                    queue.append(None)
            else:
                cur_level.append(cur)
                level_values.appendleft(cur.val)
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
        return root

