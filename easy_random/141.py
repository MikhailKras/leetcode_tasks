# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_val = 10 ** 5 + 1
        next_node = None
        cur = head
        while cur:
            if cur.val == seen_val:
                return True
            cur.val = seen_val
            next_node = cur.next
            cur = next_node
        return False

