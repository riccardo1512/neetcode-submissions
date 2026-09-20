class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT, window = {}, {}
        
        res = [-1, -1]
        resLen = float("infinity")

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT.keys()) 

        l = 0
        for r in range(len(s)):

            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT:
                if window[s[r]] == countT[s[r]]:
                    have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1
        
        return s[res[0] : res[1] + 1] if resLen < float("infinity") else ""