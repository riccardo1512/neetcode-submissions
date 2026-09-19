class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = set()

        for i in range(len(nums) - 2):

            l = i + 1 
            r = len(nums) - 1

            while l < r:

                if nums[l] + nums[i] + nums[r] > 0:
                    r -= 1
                    continue
                if nums[l] + nums[i] + nums[r] < 0:
                    l += 1
                    continue
                if nums[l] + nums[i] + nums[r] == 0:
                    res.add((nums[l], nums[i], nums[r]))
                    l += 1
                    r -= 1

        return [list(i) for i in res]