class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxL = 0
        counts = {}

        while r < len(s):
            counts[s[r]] = counts.get(s[r], 0) + 1

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1

            maxL = max(maxL, r - l + 1)
            r += 1

        return maxL




        