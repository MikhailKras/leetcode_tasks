# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = deque()

    def get_inorder(self, root: TreeNode) -> List:
        if root:
            self.get_inorder(root.left)
            self.values.append(root.val)
            self.get_inorder(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.get_inorder(root)
        init_node = TreeNode(val=self.values.popleft())
        cur_node = init_node
        while self.values:
            cur_node.right = TreeNode(val=self.values.popleft())
            cur_node = cur_node.right
        return init_node

