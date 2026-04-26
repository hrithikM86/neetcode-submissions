# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def post_order(root):
            if not root:
                return 0

            left_gain = max(post_order(root.left),0)
            right_gain = max(post_order(root.right),0)

            self.max_sum = max(self.max_sum, root.val + left_gain + right_gain)

            return root.val + max(left_gain, right_gain)

        post_order(root)
        return self.max_sum


            


        