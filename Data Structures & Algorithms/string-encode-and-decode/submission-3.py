class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += (str(len(st)) + '#' + st)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        lst = []
        i = 0
        while i<len(s):
            count = ''
            while s[i] != '#':
                count += s[i]
                i+=1
            st = s[i+1:i+int(count)+1]
            lst.append(st)
            i+=(int(count)+1)
        return lst



