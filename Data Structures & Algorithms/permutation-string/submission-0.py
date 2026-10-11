class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        d = {}
        for c in s1:
            d[c] = d.get(c, 0) + 1
            
        l = 0
        matched = 0 
        
        for r in range(len(s2)):
            c = s2[r]
            
        
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    matched += 1 
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in d:
                    if d[left_char] == 0:
                        matched -= 1
                    d[left_char] += 1
                l += 1
                
            if matched == len(d):
                return True
                
        return False