# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        stack = deque([[root, 0]])
        leaves = []
        while stack:
            node, level = stack.pop()
            if node.right is None and node.left is None:
                leaves.append([node, level])
            else:
                max_level = max(max_level, level + 1)
                if node.left:
                    stack.append([node.left, level + 1])
                if node.right:
                    stack.append([node.right, level + 1])
        res = 0
        for node, level in leaves:
            if level == max_level:
                res += node.val
        return res
        
