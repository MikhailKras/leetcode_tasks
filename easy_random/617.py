# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        merge_root = TreeNode()
        stack = [[root1, root2, merge_root]]
        while stack:
            cur1, cur2, cur_merge_root = stack.pop()
            res_val = 0
            if cur1:
                res_val += cur1.val
            if cur2:
                res_val += cur2.val
            cur_merge_root.val = res_val
            
            if (cur1 and cur1.left) or (cur2 and cur2.left):
                cur_merge_root.left = TreeNode()
                stack.append([cur1.left if cur1 else None, cur2.left if cur2 else None, cur_merge_root.left])
            if (cur1 and cur1.right) or (cur2 and cur2.right):
                cur_merge_root.right = TreeNode()
                stack.append([cur1.right if cur1 else None, cur2.right if cur2 else None, cur_merge_root.right])
        return merge_root

