# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, is_visited=None):
        self.val = val
        self.next = next
        self.is_visited = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur:
            if cur.is_visited:
                return True
            cur.is_visited = True
            cur = cur.next
        return False



        