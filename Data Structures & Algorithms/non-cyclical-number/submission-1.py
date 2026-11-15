class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            res = 0

            while n:
                digit = n % 10
                res += digit * digit
                n //= 10

            return res

        slow, fast = n, get_next(n)

        while slow != fast:
            fast = get_next(get_next(fast))
            slow = get_next(slow)

        return fast == 1