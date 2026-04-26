class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            a = target - nums[i]
            if hashmap.get(a, None)!= None:
                return [hashmap[a],i]
            else:
                hashmap[nums[i]]=i
                # print(hashmap)