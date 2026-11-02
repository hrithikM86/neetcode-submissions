from collections import defaultdict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            count = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    count = max(count, 1 + dp[j])

            dp[i] = count

        return max(dp.values())
