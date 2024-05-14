# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def get_all_values(root):
            res = []
            if root:
                stack = [root]
                while stack:
                    cur = stack.pop()
                    res.append(cur.val)
                    for child in (cur.left, cur.right):
                        if child:
                            stack.append(child)
            return res
        
        return sorted(get_all_values(root1) + get_all_values(root2))

