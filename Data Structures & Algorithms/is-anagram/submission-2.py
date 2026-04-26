class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # present = False
        hashmap = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            letter_s = s[i]
            hashmap[letter_s] = hashmap.get(letter_s, 0) + 1

            letter_t = t[i]
            hashmap[letter_t] = hashmap.get(letter_t, 0) - 1
    
        return all(count == 0 for count in hashmap.values())

            
            
            

        
        