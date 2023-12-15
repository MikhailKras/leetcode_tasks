# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        while cur.next:
            next_node = cur.next
            if next_node.val == cur.val:
                cur.next = next_node.next
            else:
                cur = next_node
        return head

