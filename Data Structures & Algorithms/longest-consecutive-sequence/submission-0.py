class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        res = 0
        
        for n in numSet:
            if n - 1 in numSet:
                pass
            else:
                count = 1
                while n + count in numSet:
                    count += 1
                
                res = max(res, count)
        
        return res
            