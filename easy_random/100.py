# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            p_stack, q_stack = [p], [q]
            p_vis, q_vis = set(), set()
            while p_stack and q_stack:
                p_cur, q_cur = p_stack.pop(), q_stack.pop()
                if p_cur in p_vis:
                    continue
                p_vis.add(p_cur)
                q_vis.add(q_cur)
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

