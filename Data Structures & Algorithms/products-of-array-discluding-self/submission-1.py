class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdt, cnt_zero, ind_zero = 1, 0, 0
        for i, n in enumerate(nums):
            if n!=0:
                pdt*=n
            else:
                cnt_zero+=1
                ind_zero+=i

        if cnt_zero >=2:
            return [0]*len(nums)
        if cnt_zero ==1:
            res = [0]*len(nums)
            res[ind_zero] = pdt
            return res
        
        return [int(pdt/x) for x in nums]

        
        
        
        


        