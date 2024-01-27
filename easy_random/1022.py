# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert_binary_to_decimal(self, bin: str) -> int:
        n = len(bin)
        res = 0
        for i in range(n):
            res += 2 ** (n - 1 - i) * int(bin[i])
        return res

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack, paths = [[root, [root.val]]], []
        while stack:
            cur = stack.pop()
            node, path = cur[0], cur[1]
            if node.left is None and node.right is None:
                paths.append(path)
            else:
                if node.left:
                    stack.append([node.left, path + [node.left.val]])
                if node.right:
                    stack.append([node.right, path + [node.right.val]])
        return sum([self.convert_binary_to_decimal(bin) for bin in paths])

