class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        curMax = nums[0]
        
        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            curMax = max(curMax, curSum)
        
        return curMax
        