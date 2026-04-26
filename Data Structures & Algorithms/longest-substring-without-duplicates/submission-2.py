class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        maxL = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] not in counter:
                counter[s[r]] = 1
                maxL = max(r - l + 1, maxL)
                r += 1
            else:
                del counter[s[l]]
                l += 1

        return maxL

        