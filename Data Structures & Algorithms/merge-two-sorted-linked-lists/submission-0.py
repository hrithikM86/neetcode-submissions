# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur1 = list1
            cur2 = list2.next

        cur = head
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next
        
        cur.next = cur1 if cur1 else cur2

        return head


        