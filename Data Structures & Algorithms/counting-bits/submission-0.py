class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            bits = 0

            while i:
                bits += 1
                i = i & (i - 1)
            res.append(bits)
        return res