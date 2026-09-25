class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i = len(nums) - 1

        j = i - 1
        while i > 0 and j >= 0:
            if j + nums[j] >= i:
                i = j
            j -= 1

        return i == 0