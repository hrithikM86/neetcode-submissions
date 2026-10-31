class Solution: #Maximum error at the end of the array we are checking...
    def maxProduct(self, nums: List[int]) -> int:
        def product(nums):
            max_pdt = nums[0]
            min_pdt = nums[0]
            result = nums[0]

            for num in nums[1:]:
                temp_max = max(min_pdt*num, max_pdt*num, num)
                temp_min = min(min_pdt*num, max_pdt*num, num)

                max_pdt = temp_max
                min_pdt = temp_min

                result = max(result, max_pdt)

            return result


        return product(nums)

                


        