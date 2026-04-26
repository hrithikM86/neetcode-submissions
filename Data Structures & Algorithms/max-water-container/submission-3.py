class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        volume = 0

        while l < r:
            ini_volume = abs((l-r)*(min(heights[l], heights[r])))
            volume = max(ini_volume, volume)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return volume







        # volume = 0
        # len_nums = len(heights)

        # for i in range(len_nums):
        #     for j in range(i+1, len_nums):
        #         ini_volume = (min(heights[i], heights[j]))*(i-j)
        #         volume = max(abs(ini_volume), volume)

        # return volume




        