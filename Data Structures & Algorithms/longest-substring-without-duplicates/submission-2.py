class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0

        l = r = 0

        setC = set()

        while r < len(s):

            if s[r] not in setC:
                res = max(res, r - l + 1)
                setC.add(s[r])
                r += 1
            else:
                setC.remove(s[l])
                l += 1

        return res
        