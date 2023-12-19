# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        len_list = 0
        while cur:
            len_list += 1
            cur = cur.next
        count, mid = 0, len_list // 2
        cur = head
        while count < mid:
            count += 1
            cur = cur.next
        
        return cur

