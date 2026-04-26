# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #BFS
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            lst = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    lst.append(node.left)
                if node.right:
                    lst.append(node.right)
            queue.extend(lst)
            depth +=1
        return depth

            


        
        

        


        