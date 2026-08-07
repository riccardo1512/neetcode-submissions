class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        arr = []

        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        output = []
        for i in range(k):
            output.append(arr.pop()[1])
        
        return output