class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def f(nums):
            n = len(nums)
            left = 0
            right = 0

            for i in range(n-1,-1,-1):
                dp = max(left, right + nums[i])
                right, left = left, dp

            return left
    
        
        return max(nums[0], f(nums[:-1]), f(nums[1:]))


        