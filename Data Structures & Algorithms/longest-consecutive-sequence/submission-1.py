class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cnt = 1
        max_cnt = 1
        i = 0
        while i < (len(nums)-1):
            if nums[i+1]==nums[i]+1:
                cnt+=1
                max_cnt = max(cnt, max_cnt)
            elif nums[i+1]==nums[i]:
                pass
            else:
                cnt = 1
            i+=1

        return max_cnt 


        

