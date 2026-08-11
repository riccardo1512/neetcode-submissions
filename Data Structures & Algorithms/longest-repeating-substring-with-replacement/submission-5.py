class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        l = r = 0
        m = defaultdict(int) # letter: freq
        maxf = 0

        for r in range(len(s)):

            m[s[r]] += 1
            maxf = max(maxf, m[s[r]])
            
            while not ((r - l + 1) - maxf <= k):
                m[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            
        return res