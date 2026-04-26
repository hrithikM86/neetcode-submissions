class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for n in nums:
            index = dic.get(n, None)
            if index is None:
                dic[n] = 1
            else:
                return True

        return False

        