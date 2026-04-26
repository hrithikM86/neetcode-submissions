# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        lst = self.to_list(head)

        return self.to_linked_list(lst)


    def to_list(self, head):
        lst = []
        itr = head
        while itr:
            lst.append(itr.val)
            itr = itr.next
        return lst[::-1]

    def to_linked_list(self, lst):
        self.head = ListNode(lst[0], None)
        itr = self.head
        
        for i in range(1, len(lst)):
            itr.next = ListNode(lst[i], None)
            itr = itr.next

        return self.head


        