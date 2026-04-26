# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not (head and head.next):
            return

        dummy = ListNode(0, head)
        length = self.length_ll(dummy)

        cur, i = dummy, 0
        while i < length - n - 1:
            cur, i = cur.next, i + 1

        cur.next = cur.next.next
        return dummy.next


    def length_ll(self, head):
        cur, count = head, 0

        while cur:
            count+=1
            cur = cur.next
        return count
