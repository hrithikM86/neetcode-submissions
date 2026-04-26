class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in nums_set:
                length = 1
                while (n+length) in nums_set:
                    length+=1
                longest = max(length, longest)
        return longest






        # if not nums:
        #     return 0
        # nums.sort()
        # cnt = 1
        # max_cnt = 1
        # i = 0
        # while i < (len(nums)-1):
        #     if nums[i+1]==nums[i]+1:
        #         cnt+=1
        #         max_cnt = max(cnt, max_cnt)
        #     elif nums[i+1]==nums[i]:
        #         pass
        #     else:
        #         cnt = 1
        #     i+=1
        # return max_cnt 


        

