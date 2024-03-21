# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        res = head.next
        while cur and cur.next:
            next_cur = cur.next.next
            first, second = cur, cur.next
            first.next, second.next = next_cur, first
            cur = next_cur
            if next_cur and next_cur.next:
                first.next = next_cur.next
        return res

