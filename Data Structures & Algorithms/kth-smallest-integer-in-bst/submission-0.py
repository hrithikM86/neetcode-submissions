# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def in_order(root):
            result = []

            if root.left:
                result += in_order(root.left)
            result.append(root.val)
            if root.right:
                result += in_order(root.right)
            return result

        return in_order(root)[k-1]
        