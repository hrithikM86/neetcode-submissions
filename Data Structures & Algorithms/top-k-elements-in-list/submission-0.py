class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {}
        for n in nums:
            present = hsh.get(n, False)
            if present:
                hsh[n] += 1
            else:
                hsh[n] = 1

        sorted_lst = sorted(hsh.items(), key = lambda x:x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(sorted_lst[i][0])

        return res
        


        