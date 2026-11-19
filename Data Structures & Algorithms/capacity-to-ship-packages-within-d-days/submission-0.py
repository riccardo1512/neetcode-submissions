class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2

            d = 1
            amount = 0
            for w in weights:
                if amount + w > m:
                    d += 1
                    amount = 0
                amount += w

            if d <= days:
                r = m
            else:
                l = m + 1
 
        return r