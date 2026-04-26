class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Please view the default dict solution too
        hsh = {}
        for s in strs:
            lst = [0] * 26
            for letter in s:
                lst[ord(letter) - ord('a')] += 1
            
            lst = tuple(lst)
            if hsh.get(lst, False):
                hsh[lst].append(s)
            else:
                hsh[lst] = [s]

        return [x for x in hsh.values()]