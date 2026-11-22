class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = 0
        minLen = min([len(x) for x in strs])

        for i in range(minLen):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return strs[0][:res]

            res += 1

        return strs[0][:res]