# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur, i = list1, 0
        while cur:
            if i == a - 1:
                parent_a = cur
            elif i == b + 1:
                node_b = cur
            cur = cur.next
            i += 1
        
        cur = list2
        while cur:
            if cur.next is None:
                end_list2 = cur
            cur = cur.next
        
        parent_a.next, end_list2.next = list2, node_b
        return list1
            
