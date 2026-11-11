class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            for i in range(len(res)):

                copy = res[i].copy()
                copy.append(n)
                res.append(copy)


        return res
        