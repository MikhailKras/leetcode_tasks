class Solution:
    def check(self,node):
        stack=[node]
        while stack:
            cur = stack.pop()
            if cur.val == 1:
                return False
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return True
                
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.check(root):
            return None
        res = root
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                if self.check(cur.left):
                    cur.left=None
                else:
                    stack.append(cur.left)
            if cur.right:
                if self.check(cur.right):
                    cur.right=None
                else:
                    stack.append(cur.right)
        return res

