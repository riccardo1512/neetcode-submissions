class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 2, 3, 0, 3, 0, 5

        # 1, 2, 6, 0, 0, 0
        # 0, 0, 0, 0, 5, 1


        # 1,2,4,6 --> prod = 48
        # 1,1,2,8
        # 48,24,6,1
        

        pref = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(pref[i] * suff[i])
        
        return res