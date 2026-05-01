class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()          

        def backtrack(start, current):
            if sum(current) == target:
                results.append(current[:])
                return
            if sum(current) > target:
                return

            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                backtrack(i + 1, current)   
                current.pop()

        backtrack(0, [])
        return results