# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue, res_dict = [[root, 0]], {}
        while queue:
            cur, level = queue.pop(0)
            if level in res_dict:
                res_dict[level][0] += cur.val
                res_dict[level][1] += 1
            else:
                res_dict[level] = [cur.val, 1]
            if cur.left:
                queue.append([cur.left, level + 1])
            if cur.right:
                queue.append([cur.right, level + 1])
        return [val/count for val, count in res_dict.values()]

