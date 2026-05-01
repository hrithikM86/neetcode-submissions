class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtracking(start,current):
            if sum(current) == target:
                results.append(current[:])
                return
            if sum(current) > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtracking(i, current)
                current.pop()

        backtracking(0, [])
        return results



        