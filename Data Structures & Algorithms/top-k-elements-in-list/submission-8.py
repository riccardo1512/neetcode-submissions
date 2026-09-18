class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # Bucket Sort (freq: number) --> normally it's index: freq
        freq = [[] for i in range(len(nums) + 1)] # the index of the array is the frequency

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
