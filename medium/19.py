# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        i, cur = 0, head

        if i > length - n - 1:
            return head.next

        while i < length - n - 1:
            cur = cur.next
            i += 1
        prev = cur
        next_node = cur.next.next
        prev.next = next_node

        return head
