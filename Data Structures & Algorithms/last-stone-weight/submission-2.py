class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1
        
        first = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            second = first - 1
            while second > 0 and bucket[second] == 0:
                second -= 1
            if not second:
                return first
            
            
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1

            first = max(first - second, second)
        return first