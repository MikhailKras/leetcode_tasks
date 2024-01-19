# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        seen, max_seen = {}, 0
        stack = [root]
        while stack:
            cur = stack.pop()
            seen[cur.val] = seen.get(cur.val, 0) + 1
            max_seen = max(max_seen, seen[cur.val])
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return [node for node in seen if seen[node] == max_seen]
        
