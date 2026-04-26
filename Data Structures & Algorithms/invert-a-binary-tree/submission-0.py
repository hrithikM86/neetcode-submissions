# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        if not curr:
            return
        else:
            curr.right, curr.left = curr.left, curr.right
        
        if curr.left:
            curr.left = self.invertTree(curr.left)
        if curr.right:
            curr.right = self.invertTree(curr.right)

        return curr
        