# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        cur = head
        lenght = 0
        while cur:
            lenght += 1
            stack.append(cur.next)
            cur = stack.pop()

        max_len = (lenght - 1) // 2
        cur = head
        stack = []
        while max_len:
            max_len -= 1
            stack.append(cur.next)
            cur = stack.pop()
        else:
            center = cur
        
        prev = None
        cur = center.next

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        while prev and head:
            if not (prev.val == head.val):
                return False
            prev = prev.next
            head = head.next
        return True

