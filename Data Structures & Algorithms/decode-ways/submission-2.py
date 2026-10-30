class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        valid_list = [str(i) for i in range(1, 27)]

        def valid(s):
            if len(s) == 0:
                return 1
            
            if s in dp:
                return dp[s]
            
            count = 0

            if len(s) >= 1:
                if s[0] in valid_list:
                    count += valid(s[1:])

            if len(s) >= 2:
                if s[:2] in valid_list:
                    count += valid(s[2:])

            dp[s] = count
            return count

        return valid(s)