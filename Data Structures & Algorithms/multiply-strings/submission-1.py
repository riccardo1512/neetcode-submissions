class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                mul = d1 * d2

                p_sum = mul + res[i + j + 1]

                res[i + j + 1] = p_sum % 10
                res[i + j] += p_sum // 10

        start = 0
        while start < m + n and res[start] == 0:
            start += 1
        
        return ''.join(map(str, res[start:]))