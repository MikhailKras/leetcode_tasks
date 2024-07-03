# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        num_level = 1
        cur_sum = 0
        max_val, max_level = root.val, 1
        queue = [root, None]
        while queue:
            cur = queue.pop(0)
            if cur is None:
                if cur_sum > max_val:
                    max_val, max_level = cur_sum, num_level
                cur_sum = 0
                num_level += 1
                if queue:
                    queue.append(None)
            else:
                cur_sum += cur.val
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
        return max_level

