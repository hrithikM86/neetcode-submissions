class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        len_nums = len(heights)

        for i in range(len_nums):
            for j in range(i+1, len_nums):
                ini_volume = (min(heights[i], heights[j]))*(i-j)
                volume = max(abs(ini_volume), volume)

        return volume




        