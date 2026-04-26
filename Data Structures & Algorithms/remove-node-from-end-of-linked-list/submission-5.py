# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not (head and head.next):
            return

        length = self.length_ll(head)
        n_start = length - n

        cur, i = head, 0
        if n_start == 0:
            return cur.next

        while i < n_start - 1:
            cur = cur.next
            i += 1

        cur.next = cur.next.next
        return head

        



    def length_ll(self, head):
        cur, count = head, 0

        while cur:
            count+=1
            cur = cur.next
        return count
