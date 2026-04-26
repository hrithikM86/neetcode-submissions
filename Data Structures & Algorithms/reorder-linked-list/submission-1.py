# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
    #     if not head or not head.next:
    #         return

    #     list1, list2 = self.split_ll(head)
    #     self.merge_ll(list1, list2)

    # def length_ll(self, head):
    #     count, cur = 0, head
    #     while cur:
    #         count += 1
    #         cur = cur.next
    #     return count
    
    # def split_ll(self, head):
    #     count = self.length_ll(head)

    #     cur = head
    #     i = 0

    #     while i < (count // 2) - 1:
    #         cur = cur.next
    #         i += 1

    #     r = cur.next
    #     r = self.reverse_ll(r)
    #     cur.next = None

    #     return head, r

    # def reverse_ll(self, head):
    #     prev = None
    #     cur = head

    #     while cur:
    #         temp = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = temp

    #     return prev

    # def merge_ll(self, list1, list2):
    #     cur1, cur2 = list1, list2

    #     while cur1 and cur2:
    #         temp1 = cur1.next
    #         temp2 = cur2.next

    #         cur1.next = cur2
    #         if not temp1:
    #             break

    #         cur2.next = temp1

    #         cur1 = temp1
    #         cur2 = temp2




        