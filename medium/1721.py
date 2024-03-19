# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, i = head, 1
        while cur:
            if i == k:
                swap_value = cur.val
            i += 1
            cur = cur.next
        cur, j = head, 1
        while cur:
            if j == i - k:
                swap_value2 = cur.val
                cur.val = swap_value
            j += 1
            cur = cur.next
        cur, i = head, 1
        while cur:
            if i == k:
                cur.val = swap_value2
            i += 1
            cur = cur.next
        return head
        
