# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        is_odd = root.val % 2 == 1
        if not is_odd:
            return False
        queue = deque([root, None])
        last_val = None
        while queue:
            cur = queue.popleft()
            if cur is None:
                is_odd = not is_odd
                last_val = None
                if queue:
                    queue.append(None)
            else:
                if is_odd:
                    if cur.val % 2 != 1 or (last_val and cur.val <= last_val):
                        return False
                else:
                    if cur.val % 2 != 0 or (last_val and cur.val >= last_val):
                        return False
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
                last_val = cur.val
        return True

