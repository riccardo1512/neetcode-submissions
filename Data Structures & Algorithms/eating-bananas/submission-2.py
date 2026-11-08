class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        l = 1
        r = max(piles)

        while l <= r:

            m = (l + r) // 2
            time = 0

            for i in range(len(piles)):
                time += piles[i] // m + (1 if (piles[i] % m) else 0)

            if time <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res