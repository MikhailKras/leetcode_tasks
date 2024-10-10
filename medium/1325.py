# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def is_leave(node: TreeNode) -> bool:
            return node.left is None and node.right is None
        
        def delete_node_child(node: TreeNode) -> None:
            if node is None:
                return
            if node.left and node.left.val == target and is_leave(node.left):
                node.left = None
            if node.right and node.right.val == target and is_leave(node.right):
                node.right = None
            delete_node_child(node.parent)

        root.parent = None
        stack = [root]
        while stack:
            cur = stack.pop()
            if is_leave(cur):
                delete_node_child(cur.parent)
            else: 
                for child in (cur.left, cur.right):
                    if child:
                        child.parent = cur
                        stack.append(child)
        return None if is_leave(root) and root.val == target else root

