# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p1 = min(p.val,q.val)
        q1 = max(p.val,q.val)
        
        if root.val < p1:
            return self.lowestCommonAncestor(root.right, p, q)

        if root.val > q1:
            return self.lowestCommonAncestor(root.left, p, q)


        return root

        

        

        