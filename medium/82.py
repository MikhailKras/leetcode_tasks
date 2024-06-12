# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head.next
        prev = head
        seen = set()
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                seen.add(cur.val)
            else:
                prev = cur
            cur = cur.next
        
        cur = head
        prev = None
        while cur:
            if cur.val in seen:
                if prev is None:
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

