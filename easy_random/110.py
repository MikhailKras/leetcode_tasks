# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 1
        while stack:
            cur = stack.pop()
            if cur[0].left is None and cur[0].right is None:
                depth = max(depth, cur[1])
            if cur[0].left:
                stack.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                stack.append((cur[0].right, cur[1] + 1))
        return depth

    def is_node_balanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.get_depth(root.left) - self.get_depth(root.right)) <= 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        while stack:
            cur = stack.pop()
            if not self.is_node_balanced(cur):
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return True

