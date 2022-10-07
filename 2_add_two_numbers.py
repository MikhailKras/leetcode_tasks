# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = ListNode.serialize(l1)
        l2 = ListNode.serialize(l2)
        l1 = [x for x in l1 if x.isdigit()]
        l2 = [x for x in l2 if x.isdigit()]
        l1.reverse(), l2.reverse()
        l1 = int(''.join(l1))
        l2 = int(''.join(l2))
        res = list(str(l1 + l2))
        res.reverse()
        return ListNode._array_to_list_node(res)
