# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        cur = head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return int(''.join(res), 2)
        
