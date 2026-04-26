class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i, n in enumerate(nums):
            res[:i] = [x * n for x in res[:i]]
            res[i+1:] = [x * n for x in res[i+1:]]
        return res
            






        # pdt = 1
        # zero_count = 0
        # zero_index = -1

        # for i, n in enumerate(nums):
        #     if n:
        #         pdt *= n
        #     else:
        #         zero_count += 1
        #         zero_index = i

        # if zero_count > 1:
        #     return [0] * len(nums)

        # if zero_count == 1:
        #     res = [0] * len(nums)
        #     res[zero_index] = pdt
        #     return res

        # return [pdt // x for x in nums]
