class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = curMax = 1

        for n in nums:
            temp = curMax
            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, curMin * n, temp * n)

            res = max(res, curMax)

        return res
            