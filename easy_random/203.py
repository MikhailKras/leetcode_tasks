# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        if cur.val == val:
            while cur and cur.val == val:
                head = cur = cur.next
        if not head:
            return head
        
        prev, cur = ListNode(), head
        while cur:
            if cur.val == val:
                prev.next, cur = cur.next, cur.next
            else:
                prev, cur = cur, cur.next
        
        return head

