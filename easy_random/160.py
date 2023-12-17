# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA:
            curA = curA.next
            lenA += 1
        while curB:
            curB = curB.next
            lenB += 1
        if lenA > lenB:
            cur_long, cur_short = headA, headB
        else:
            cur_long, cur_short = headB, headA
        diff = abs(lenA - lenB)
        while diff:
            cur_long = cur_long.next
            diff -= 1
        
        inter = None
        while cur_long and cur_short:
            if inter is None:
                if cur_long is cur_short:
                    inter = cur_long
            else:
                if cur_long is not cur_short:
                    inter = None
            cur_long, cur_short = cur_long.next, cur_short.next
        return inter

