class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        start = 0
        maxlen = 1

        dp = [[False]*n for _ in range(n)]

        for length in range(1, n+1):
            for i in range(n-length+1):
                j = i + length - 1

                if length == 1:
                    dp[i][j] = True
                
                elif length == 2:
                    dp[i][j] = s[i] == s[j]

                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

                
                if length > maxlen:
                    maxlen = length
                    start = i

        return sum(sum(row) for row in dp)
                



        











        