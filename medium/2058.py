# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first, last = None, None
        res = [-1, -1]
        prev, cur = head, head.next
        i = 0
        while cur.next:
            if prev.val < cur.val > cur.next.val or prev.val > cur.val < cur.next.val:
                if first is None:
                    first = i
                if last is not None:
                    res[0] = min(i - last, res[0]) if res[0] != -1 else i - last
                last = i
            i += 1
            prev = cur
            cur = cur.next
        if first != last:
            res[1] = last - first
        return res

