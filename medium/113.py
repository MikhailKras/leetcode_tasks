# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def get_children(node: TreeNode) -> List[TreeNode]:
            res = []
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
            return res
        ans = []
        if not root:
            return ans
        stack = [[root, [root.val]]]
        while stack:
            node, prev_values = stack.pop()
            childrens = get_children(node)
            if not childrens:
                if sum(prev_values) == targetSum:
                    ans.append(prev_values)
            else:
                for child in childrens:
                    stack.append([child, prev_values + [child.val]])
        return ans

