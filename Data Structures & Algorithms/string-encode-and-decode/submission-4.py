class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += (str(len(st)) + '#' + st)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.index('#', i)        
            length = int(s[i:j])         
            i = j + 1
            res.append(s[i:i+length])    
            i += length
        return res



