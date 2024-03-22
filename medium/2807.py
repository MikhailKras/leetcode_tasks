# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            a, b = cur.val, cur.next.val
            while a != 0 and b != 0:
                if a > b:
                    a = a % b
                else:
                    b = b % a
            divisor_node = ListNode(val=a + b, next=cur.next)
            cur.next = divisor_node
            cur = divisor_node.next
        return head

