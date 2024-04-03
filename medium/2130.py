# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list_len = 0
        cur = head
        while cur:
            cur = cur.next
            list_len += 1
        twin_sum = []
        cur, i = head, 0
        while i < list_len // 2:
            twin_sum.append(cur.val)
            cur = cur.next
            i += 1
        twin_sum = twin_sum[::-1]
        j = 0
        while cur:
            twin_sum[j] += cur.val
            cur = cur.next
            j += 1
        return max(twin_sum)

