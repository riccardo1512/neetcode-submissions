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
                if d[c]:
                    matched += 1
                d[c] -= 1
            
            while r - l + 1 > len(s1):
                if s2[l] in d:
                    d[s2[l]] += 1
                if s2[l] in d and d[s2[l]]:
                    matched -= 1
                l += 1
            
            if matched == len(s1):
                return True
            
        return False