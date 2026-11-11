class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [[]]
        m = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        } # number : List(string)

        for d in digits:
            temp = []
            for arr in res:
                for c in m[d]:
                    temp.append(arr + [c])
            res = temp
        
        res = [''.join(s) for s in res]
        return res
        