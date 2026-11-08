class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        resLen = float("inf")
        res = (0, 0)

        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1

        need = len(count)
        have = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] == 0:
                    have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = min(resLen, r - l + 1)
                    res = (l, r)

                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        have -= 1
                
                l += 1
        
        return s[res[0] : res[1] + 1] if (resLen < float("inf")) else ""

        