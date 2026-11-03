from collections import defaultdict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        dp = [[0] * n for _ in range(m)]

        def recursion(i, j):
            # return the number of unique paths
            if i == m - 1 and j == n - 1:
                dp[i][j] = 0
            elif (i == m - 1 and j != n - 1) or (i != m - 1 and j == n - 1):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                recursion(i, j)
        return dp[0][0]
