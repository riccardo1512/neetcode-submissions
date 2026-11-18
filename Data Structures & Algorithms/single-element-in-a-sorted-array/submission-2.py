class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1

        while l < r:
            m = (r + l) // 2

            if (m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 > len(nums) or nums[m] != nums[m + 1]):
                return nums[m]

            if m % 2 != 0:
                m -= 1


            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m
        return nums[r]