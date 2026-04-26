class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       hsh = {}
       for s in strs:
        s_sort = ''.join(sorted(s)) 
        present=hsh.get(s_sort, False)
        if present:
            hsh[s_sort].append(s)
        else:
            hsh[s_sort]=[s]
        lst = [x for x in hsh.values()]
       return lst






        