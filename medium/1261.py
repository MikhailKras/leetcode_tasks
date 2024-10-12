# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        queue = deque([root])
        self.seen = {root.val}
        while queue:
            cur = queue.popleft()
            if cur.left:
                cur.left.val = 2 * cur.val + 1
                queue.append(cur.left)
                self.seen.add(cur.left.val)
            if cur.right:
                cur.right.val = 2 * cur.val + 2
                queue.append(cur.right)
                self.seen.add(cur.right.val)
        self.root = root
            
    def find(self, target: int) -> bool:
        return target in self.seen
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

