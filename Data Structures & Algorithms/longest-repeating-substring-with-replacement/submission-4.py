class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        l = r = 0
        m = defaultdict(int) # letter: freq

        while r < len(s):

            m[s[r]] += 1

            if (sum(m.values()) - max(m.values())) <= k:
                res = max(res, r - l + 1)
            else:
                while not ((sum(m.values()) - max(m.values())) <= k) and l < r:
                    m[s[l]] -= 1
                    l += 1
            
            r += 1
        
        return res