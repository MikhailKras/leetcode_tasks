# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        mins = [float('inf'), float('inf')]
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val < mins[0]:
                mins[0] = cur.val
            elif cur.val < mins[1] and cur.val != mins[0]:
                mins[1] = cur.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return mins[1] if mins[1] != float('inf') else -1
            
