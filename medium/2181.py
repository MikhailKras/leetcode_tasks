# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        between_sum, cur_zero = 0, None
        while cur:
            if cur.val == 0:
                if cur_zero:
                    cur_zero.val = between_sum
                    cur_zero.next = cur if cur.next else None
                between_sum = 0
                cur_zero = cur
            else:
                between_sum += cur.val
            cur = cur.next
        return head

