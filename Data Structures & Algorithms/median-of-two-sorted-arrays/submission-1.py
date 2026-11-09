class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = nums1 + nums2
        arr.sort()

        l = len(arr) - 1

        if len(arr) % 2:
            return arr[l // 2]
        
        return (arr[l // 2] + arr[l // 2 + 1]) / 2
        