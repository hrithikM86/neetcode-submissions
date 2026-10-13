class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resf = s[0]
        maxlen = 1

        if n == 1:
            return s

        for i in range(n):
            for even in [True, False]:
                if even:  # even
                    l = i
                    r = i+1
                    res = ''
                else:     # odd
                    l = i-1
                    r = i+1
                    res = s[i]

                while 0 <= l and r < n:
                    if s[l] == s[r]:
                        res = s[l] + res + s[r]

                        if r-l+1 > maxlen:
                            maxlen = r-l+1
                            resf = res

                        l = l-1
                        r = r+1
                    else:
                        break

        return resf