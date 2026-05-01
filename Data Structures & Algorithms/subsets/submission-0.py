class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtracking(start, current):
            results.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtracking(i+1, current)
                current.pop()

        backtracking(0, [])
        return results

        