from collections import defaultdict


class Solution:  # Memonizaion - use a dictionary to store values
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = defaultdict()

        def recursion(s):
            if len(s) == 0:
                return True

            if s in memo:
                return memo[s]

            for word in wordDict:
                len_w = len(word)

                if len_w <= len(s) and s[:len_w] == word:
                    if recursion(s[len_w:]):
                        memo[s] = True
                        return True
                    else:
                        memo[s] = False

            return False

        return recursion(s)
