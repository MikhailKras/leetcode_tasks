# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)
        cur_depth = 1
        queue = deque([root, None])
        cur_level = []
        while queue:
            cur = queue.popleft()
            if cur is None:
                cur_depth += 1
                if cur_depth == depth:
                    for node in cur_level:
                        l, r = node.left, node.right
                        node.left, node.right = TreeNode(val=val, left=l), TreeNode(val=val, right=r)
                    break
                cur_level = []
                if queue:
                    queue.append(None)
            else:
                cur_level.append(cur)
                for child in (cur.left, cur.right):
                    if child:
                        queue.append(child)
        return root

