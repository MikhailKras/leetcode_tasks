# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def insert_node(head, node) -> ListNode:
        cur = head
        prev = None
        while cur:
            if cur.val > node.val:
                if prev:
                    prev.next = node
                else:
                    head = node
                node.next = cur
                break
            if cur.next is None:
                cur.next = node
                break
            prev = cur
            cur = cur.next
        return head

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort_list = ListNode(val=head.val)
        cur = head.next
        while cur:
            sep_cur = cur
            cur = cur.next
            sep_cur.next = None
            sort_list = self.insert_node(sort_list, sep_cur)
        return sort_list

