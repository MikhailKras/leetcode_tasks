# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def get_letter(num: int) -> str:
            return chr(num + 97)

        stack = [[root, get_letter(root.val)]]
        min_str = None
        while stack:
            cur, val = stack.pop()
            if cur.left is None and cur.right is None:
                if min_str is None:
                    min_str = val
                else:
                    min_str = min(min_str, val)
            else:
                for child in (cur.left, cur.right):
                    if child:
                        stack.append([child, get_letter(child.val) + val])
        
        return min_str

