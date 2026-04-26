class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {}
        for n in nums:
            hsh[n] = hsh.get(n, 0) + 1

        return [nums for nums,_ in sorted(hsh.items(), key = lambda x:x[1], reverse = True)[:k]]
        


        