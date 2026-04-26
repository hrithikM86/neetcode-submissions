class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # present = False
        hashmap = {}

        for n in s:
            count = hashmap.get(n, None)
            if count == None:
                hashmap[n] = 1
            else:
                hashmap[n] += 1

        for n in t:
            count = hashmap.get(n, None)
            if (count == None) or (count <= 0):
                return False
            if count>0:
                hashmap[n] -= 1

        for letters, count in hashmap.items():
            if count>0:
                return False
        return True
            
            
            

        
        