class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        
        subSum = 0
        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            
            sum_bit = bit_a ^ bit_b ^ subSum
            res |= sum_bit << i

            subSum = (bit_a & bit_b) | (bit_a & subSum) | (bit_b & subSum)
        
        if (res >> 31) & 1:
            res = ~(res ^ 0xFFFFFFFF)

        return res