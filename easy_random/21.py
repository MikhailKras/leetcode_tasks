# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        cur1, cur2, new = list1, list2, ListNode()
        head_new = new
        while cur1 and cur2:
            if cur1.val < cur2.val:
                new.val = cur1.val
                cur1 = cur1.next
            else:
                new.val = cur2.val
                cur2 = cur2.next
            new.next = ListNode()
            new = new.next
        if cur1:
            new.val = cur1.val
            new.next = cur1.next
        elif cur2:
            new.val = cur2.val
            new.next = cur2.next
        return head_new
        
