# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Two pointer solution
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev














# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return
#         return self.to_linked_list(self.to_list(head))

#     def to_list(self, head):
#         arr, cur = [], head
#         while cur:
#             arr.append(cur.val)
#             cur = cur.next
#         return arr[::-1]

#     def to_linked_list(self, arr):
#         head = cur = ListNode(arr[0])
#         for v in arr[1:]:
#             cur.next = ListNode(v)
#             cur = cur.next
#         return head


        