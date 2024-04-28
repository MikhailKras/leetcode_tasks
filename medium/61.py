# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        length = 0
        cur = head
        while cur:
            if cur.next is None:
                end = cur
            cur = cur.next
            length += 1
        cur = head
        i = 0
        k = k % length
        if k == 0:
            return head

        while i != length - k - 1:
            cur = cur.next
            i += 1
        new_first = cur.next
        cur.next = None
        end.next = head

        return new_first

