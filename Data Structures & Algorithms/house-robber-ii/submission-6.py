class Solution:
    def rob(self, nums: List[int]) -> int:

        def houseRob(nums):
            rob1, rob2 = 0, 0
            
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], houseRob(nums[1:]), houseRob(nums[:-1]))