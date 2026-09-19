class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charMap = {} # char : index

        res = 0
        l = 0

        # bacaefgalop

        for r in range(len(s)):

            if s[r] in charMap:
                l = max(l, charMap[s[r]] + 1)

            charMap[s[r]] = r
            res = max(res, r - l + 1)
            

            
        
        return res