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
                if not d[c]:
                    matched += 1
            
            while r - l + 1 > len(s1):
                if s2[l] in d:
                    if d[s2[l]] == 0:
                        matched -= 1
                    d[s2[l]] += 1
                l += 1
            
            if matched == len(d):
                return True
            
        return False