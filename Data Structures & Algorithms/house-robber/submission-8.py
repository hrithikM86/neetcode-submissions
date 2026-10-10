class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0]*(n+2)
        left = 0
        right = 0

        for i in range(n-1, -1, -1):
            dp = max(left, right + nums[i])
            right = left
            left = dp

        return left
            


        