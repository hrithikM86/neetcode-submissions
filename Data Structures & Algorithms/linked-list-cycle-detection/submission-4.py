# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#         # self.is_visited = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        slow_ptr = head
        fast_ptr = head.next

        while fast_ptr and fast_ptr.next:
            if fast_ptr == slow_ptr:
                return True
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return False
            







        # cur = head
        # while cur:
        #     if cur.is_visited:
        #         return True
        #     cur.is_visited = True
        #     cur = cur.next
        # return False



        