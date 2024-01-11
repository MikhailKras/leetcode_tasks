# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p and q:
            p_stack, q_stack = [p], [q]
            while p_stack and q_stack:
                p_cur, q_cur = p_stack.pop(), q_stack.pop()
                if (
                        (p_cur.left if p_cur.left is None else p_cur.left.val),
                        (p_cur.right if p_cur.right is None else p_cur.right.val)
                    )\
                    !=\
                    (
                        (q_cur.left if q_cur.left is None else q_cur.left.val),
                        (q_cur.right if q_cur.right is None else q_cur.right.val)
                    ):
                    return False
                if p_cur.left:
                    p_stack.append(p_cur.left)
                if p_cur.right:
                    p_stack.append(p_cur.right)
                if q_cur.left:
                    q_stack.append(q_cur.left)
                if q_cur.right:
                    q_stack.append(q_cur.right)
            return True if p_stack == [] and q_stack == [] else False
        else:
            return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                if self.isSameTree(cur, subRoot):
                    return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False
        
