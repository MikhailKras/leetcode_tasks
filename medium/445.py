# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_reverse_list(lst: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = lst
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        
        new_prev, new, head = None, None, None
        cur1, cur2 = get_reverse_list(l1), get_reverse_list(l2)
        remain = 0
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            new_val = (val1 + val2 + remain) % 10
            new = ListNode(val=new_val)
            if not head:
                head = new
            if new_prev:
                new_prev.next = new
            new_prev = new
            remain = (val1 + val2 + remain) // 10
            cur1 = cur1 if cur1 is None else cur1.next
            cur2 = cur2 if cur2 is None else cur2.next
        else:
            if remain:
                new_prev.next = ListNode(val=remain)
        return get_reverse_list(head)

