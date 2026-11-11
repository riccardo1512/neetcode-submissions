class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        def dfs(i):
            if i >= len(s):
                res.append(cur.copy())
                return

            for j in range(i, len(s)):
                if palindrome(i, j):
                    cur.append(s[i : j + 1])
                    dfs(j + 1)
                    cur.pop()
        dfs(0)
        return res
        