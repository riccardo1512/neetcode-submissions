class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0

        l, r = 0, len(heights) - 1

        while l < r:

            area = min(heights[l], heights[r]) * (r - l)

            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            # 1, 2, 10, 2, 2, 2, 10
            # area = 10 * 4 = 40
            # indexes = 2, 6 ---> 6 - 2 = 4
        return res
        