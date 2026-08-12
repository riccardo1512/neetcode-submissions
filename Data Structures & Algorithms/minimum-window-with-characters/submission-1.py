class Solution:
    def minWindow(self, s: str, t: str) -> str:   
        res = ""
        resLen = float("inf")
        l = r = 0
        count = len(t)
        m = defaultdict(int) # char : count

        for c in t:
            m[c] += 1

        while l <= r < len(s):

            if m[s[r]] > 0:
                count -= 1
            
            m[s[r]] -= 1

            while count == 0:
                
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                m[s[l]] += 1
                if m[s[l]] > 0:
                    count += 1
                
                l += 1
            
            r += 1

        if res:
            resl, resr = res
            return s[resl : resr + 1] 
        else:
            return res