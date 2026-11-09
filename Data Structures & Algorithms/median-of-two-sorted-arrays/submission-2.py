class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = nums1 + nums2
        arr.sort()

        l = len(arr)

        if len(arr) % 2 == 1:
            return arr[l // 2]
        
        return (arr[l // 2 - 1] + arr[l // 2]) / 2
        