class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # present = False
        hashmap = {}
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        for i in range(len_t):
            letter_s = s[i]
            count = hashmap.get(letter_s, None)
            if count == None:
                hashmap[letter_s] = 1
            else:
                hashmap[letter_s] += 1

            letter_t = t[i]
            count = hashmap.get(letter_t, None)
            if count == None:
                hashmap[letter_t] = -1
            else:
                hashmap[letter_t] -= 1

        for count in hashmap.values():
            if count!=0:
                return False
        return True
            
            
            

        
        