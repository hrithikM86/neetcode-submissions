class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_t = {}
        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1

        hash_s = {}
        minStr = ''
        l, r = 0, 0

        while r < len(s):
            hash_s[s[r]] = hash_s.get(s[r], 0) + 1

            while all(hash_s.get(k, 0) >= v for k, v in hash_t.items()):
                if not minStr or len(minStr) > r - l + 1:
                    minStr = s[l:r+1]

                hash_s[s[l]] -= 1
                # if hash_s[s[l]] == 0:
                #     del hash_s[s[l]]
                l += 1

            r += 1

        return minStr

        