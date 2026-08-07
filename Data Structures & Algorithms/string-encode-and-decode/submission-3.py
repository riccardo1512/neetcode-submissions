class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        
        res = []
        count = 0

        i = 0

        num = ""

        while i < len(s):

            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            i = j + 1

            res.append(s[i: i+length])

            i += length


        return res