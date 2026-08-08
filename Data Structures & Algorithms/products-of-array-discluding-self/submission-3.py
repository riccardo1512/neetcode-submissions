class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

    # [1,2,4,6]
    # [48,24,12,8]

    # [1, 1, 2, 8]
    # [48, 24, 6, 1]

        res = [0] * len(nums)

        prefix, suffix  = [0] * len(nums), [0] * len(nums)

        p = 1
        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res