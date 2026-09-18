class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # no zeros --> no problem
        # 1 zero --> we can calculate the totProd without the zero and avoid it
        # 2 or more zeros --> everything will be zero

        totProd = 1
        zero = 0

        for n in nums:
            if n != 0:
                totProd *= n
            else:
                zero += 1

        res = [0] * len(nums)

        if zero >= 2:
            return res

        for i in range(len(nums)):
            if zero and nums[i] == 0:
                res[i] = totProd
            elif zero and nums[i] != 0:
                res[i] = 0
            else:
                res[i] = totProd // nums[i]

        return res
        