class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            if hashmap.get(target - nums[i], None)!= None:
                return [hashmap[target - nums[i]],i]
            else:
                hashmap[nums[i]]=i
                # print(hashmap)