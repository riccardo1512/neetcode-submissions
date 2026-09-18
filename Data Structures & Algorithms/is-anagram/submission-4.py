class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ms = defaultdict(int)
        mt = defaultdict(int)

        for i in range(len(s)):
            ms[s[i]] = ms[s[i]] + 1
            mt[t[i]] = mt[t[i]] + 1
        

        return ms == mt
        