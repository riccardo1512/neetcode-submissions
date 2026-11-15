class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick_select(nums, k):
            pivot = nums[len(nums) // 2]

            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]

            if k < len(left):
                return quick_select(left, k)
            elif k < len(left) + len(middle):
                return pivot
            else:
                return quick_select(right, k - len(left) - len(middle))

        return quick_select(nums, len(nums) - k)
        