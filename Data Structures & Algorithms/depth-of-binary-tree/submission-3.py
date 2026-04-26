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
        # if not root:
        #     return 0

        # queue, depth = deque([root]), 0

        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     depth +=1
        # return depth

        #DFS

        if not root:
            return 0
        stack = [(root, 1)]
        result = 0  # start at 0, max handles the rest
        while stack:
            node, level = stack.pop()
            result = max(result, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return result


        
        

        


        