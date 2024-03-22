# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        cur = self.head
        i = 0
        while cur:
            cur = cur.next
            i += 1
        node_number = choice(range(i))
        cur = self.head
        j = 0
        while j != node_number:
            cur = cur.next
            j += 1
        return cur.val
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
